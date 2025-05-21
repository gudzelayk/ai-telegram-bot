import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "mistralai/mistral-7b-instruct"

def ask_gpt(prompt):
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": MODEL,
                "messages": [
                    {"role": "system", "content": "Ти AI-помічник."},
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()

        # Якщо є choices — повертаємо відповідь
        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        # Якщо є помилка — показуємо
        elif "error" in data:
            return f"API Помилка: {data['error']}"
        else:
            return f"Невідома відповідь: {data}"

    except Exception as e:
        return f"Помилка: {e}"
