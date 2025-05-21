import google.generativeai as genai
import os

# Немає dotenv — ключ має бути заданий безпосередньо в середовищі або коді
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gpt(prompt):
    response = model.generate_content(prompt)
    return response.text
