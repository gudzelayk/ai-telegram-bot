import google.generativeai as genai
import os
from dotenv import load_dotenv

# Завантаження змінних середовища з .env
load_dotenv()

# Конфігурація API-ключа
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Створення моделі
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gpt(prompt):
    response = model.generate_content(prompt)
    return response.text
