import sqlite3

# Connect to the existing database
conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

# List of new responses to add
new_responses = [
    ("How do I improve my resume?", "Highlight your skills, experience, and achievements clearly."),
    ("What are some good career options?", "It depends on your interests! Some fields include tech, healthcare, and finance."),
    ("How can I prepare for an interview?", "Research the company, practice common questions, and dress professionally."),
    ("What are the top programming languages?", "Python, Java, JavaScript, and C++ are widely used."),
    ("How do I switch careers?", "Gain relevant skills, network, and start with small projects."),
    ("What is networking in a career?", "Building professional relationships to find opportunities."),
    ("How can I improve my communication skills?", "Practice speaking, listen actively, and seek feedback."),
    ("What is a good way to find jobs?", "Use LinkedIn, job portals, and referrals."),
    ("Should I go for higher studies?", "It depends on your career goals and the field you want to enter."),
    ("How do I negotiate a salary?", "Research industry salaries, be confident, and justify your worth."),
    ("What certifications are useful?", "Depends on your field! AWS, PMP, and Google certifications are popular."),
    ("How can I get an internship?", "Apply early, build a good resume, and reach out to recruiters."),
    ("Is freelancing a good career choice?", "Yes, if you prefer flexibility and independence."),
    ("What are the benefits of working abroad?", "Exposure to new cultures, better salaries, and career growth."),
    ("How do I choose a college major?", "Consider your interests, job prospects, and skill strengths."),
    ("What are some in-demand jobs?", "Data science, cybersecurity, and AI engineering are trending."),
    ("How do I build a portfolio?", "Showcase your best work, keep it updated, and make it visually appealing."),
    ("Is remote work a good option?", "It offers flexibility but requires discipline."),
    ("How do I ask for a promotion?", "Prove your value, take initiative, and communicate with your manager."),
    ("What skills do I need for a startup?", "Problem-solving, leadership, and adaptability are key."),
]

# Ensure the table exists before inserting data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT UNIQUE,
        bot_response TEXT
    )
''')

# Insert the new responses into the database
cursor.executemany("INSERT OR IGNORE INTO responses (user_message, bot_response) VALUES (?, ?)", new_responses)

# Commit changes and close the connection
conn.commit()
conn.close()

print("New responses added successfully!")
