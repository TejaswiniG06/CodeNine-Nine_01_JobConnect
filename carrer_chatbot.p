from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Function to initialize the database
def init_db():
    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT UNIQUE,
            bot_response TEXT
        )
    ''')
    sample_responses = [
        ("I need career advice", "Explore different fields and identify your interests."),
        ("Tell me about software engineering", "Software engineering involves designing, developing, and maintaining software."),
        ("What skills do I need for a job?", "You need technical skills, communication skills, and problem-solving abilities."),
    ]
    for user_message, bot_response in sample_responses:
        cursor.execute("INSERT OR IGNORE INTO responses (user_message, bot_response) VALUES (?, ?)", (user_message, bot_response))
    conn.commit()
    conn.close()

@app.route("/", methods=["GET"])
def home():
    return "Flask server is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400

    user_message = data["message"]

    conn = sqlite3.connect("chatbot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT bot_response FROM responses WHERE user_message = ?", (user_message,))
    result = cursor.fetchone()
    conn.close()

    response_text = result[0] if result else "I'm not sure about that. Try asking something else."
    return jsonify({"response": response_text})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)  # Listen on all network interfaces
