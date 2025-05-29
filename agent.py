import google.generativeai as genai
from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def ask_gpt(user_message):
    full_prompt = (
        "Ти — асистент для допомоги у подачі записок на церковні служби. "
        "Користувач може писати довільно: прохання, імена, дати, уточнення. "
        "Твоє завдання — допомогти йому правильно підготувати запис: "
        "чітко виокремити тип (за здоров’я, за упокій, на службу), імена, дату (якщо є). "
        "Відповідай зрозумілою, людською мовою, підтверджуючи прийнятий запит. "
        "Не додавай вигаданих імен або даних, не змінюй суть повідомлення. "
        f"Ось повідомлення користувача: {user_message}"
    )
    try:
        response = model.generate_content(full_prompt)
        print(f"AI raw response: {response}")
        return response.text
    except Exception as e:
        print(f"❌ Помилка при виклику GPT: {e}")
        return "Вибачте, сталася помилка при обробці вашого запиту."
