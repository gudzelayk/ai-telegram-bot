import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def ask_gpt(prompt):
    try:
        response = model.generate_content(prompt)
        if hasattr(response, "text"):
            return response.text
        else:
            return "❗ Відповідь порожня або недоступна."
    except genai.types.BlockedPromptException:
        return "⚠️ Запит заблоковано політикою Google AI (недопустимий вміст)."
    except genai.types.RateLimitExceededError:
        return "⏳ Перевищено ліміт запитів. Спробуй пізніше."
    except genai.types.APIError as api_err:
        return f"🚫 API помилка: {api_err.message}"
    except Exception as e:
        return f"❌ Помилка: {e}"