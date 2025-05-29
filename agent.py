import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gpt(user_message):
    full_prompt = (
        "Ти — асистент подачі записок на церковні служби. "
        "Твоє єдине завдання — з будь-якого повідомлення користувача формувати запис для Google Sheets. "
        "Видавай відповідь лише у форматі: ‘дата, тип, імена’. "
        "Наприклад: ‘29.05.2025, Здоров’я, Іван, Марія’ або ‘29.05.2025, Упокій, Петро, Олена’. "
        "Не додавай пояснень, не вставляй додатковий текст, відповідай тільки цим рядком.\n\n"
        f"Вхідне повідомлення користувача: {user_message}"
    )
    response = model.generate_content(full_prompt)
    return response.text
