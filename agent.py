from config import GOOGLE_API_KEY
import google.generativeai as genai

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gpt(prompt):
    response = model.generate_content(prompt)
    return response.text
