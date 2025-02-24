# Complete Backend Code: Affinda + Hugging Face Integration

from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv()

# API keys
AFFINDA_API_KEY = os.getenv('AFFINDA_API_KEY')
AFFINDA_ENDPOINT = 'https://api.affinda.com/v3/documents'

# Initialize Hugging Face text generation
generator = pipeline('text-generation', model='gpt2')

# Initialize Flask
app = Flask(__name__)

# Upload and parse resume using Affinda
def parse_resume(file_path):
    headers = {'Authorization': f'Bearer {AFFINDA_API_KEY}'}
    files = {'file': open(file_path, 'rb')}
    data = {}  # Replace with your workspace ID
    response = requests.post(AFFINDA_ENDPOINT, headers=headers, files=files, data=data)
    return response.json()

# Optimize resume using Hugging Face
def optimize_resume(parsed_data):
    prompt = f"""
    Optimize the following parsed resume data into a professional, user-friendly format:
    {parsed_data}
    Provide a clear and concise summary, including key skills, experience, and achievements.
    """
    result = generator(prompt, max_length=500, num_return_sequences=1)
    return result[0]['generated_text']

# Route to handle resume upload and optimization
@app.route('/upload', methods=['POST'])
def upload_resume():
    try:
        file = request.files['resume']
        if file:
            file_path = f"uploads/resume-ex.pdf"
            file.save(file_path)

            # Step 1: Parse resume
            parsed_data = parse_resume(file_path)

            # Step 2: Optimize resume using Hugging Face
            optimized_resume = optimize_resume(parsed_data)

            return jsonify({"optimized_resume": optimized_resume}), 200
        else:
            return jsonify({"error": "No file provided"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
