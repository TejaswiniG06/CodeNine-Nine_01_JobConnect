#code to import open ai"
#very first code to start with chatbot

---------
import openai

openai.api_key = "api key"

def get_career_advice(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a career guidance chatbot."},
                  {"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

user_query = "I am a software engineer with 3 years of experience in backend development. What career paths can I explore?"
print(get_career_advice(user_query))
