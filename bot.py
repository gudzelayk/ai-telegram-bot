from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from agent import ask_gpt
from config import TELEGRAM_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я допоможу вам підготувати записки на церковну службу. Напишіть прохання або імена.")

def analyze_message(text):
    if ("за здоров" in text or "здоров" in text):
        return "Здоров’я"
    if "упок" in text:
        return "Упокій"
    return None

def extract_names(text):
    names_part = text.split("—")[-1]
    names = [name.strip() for name in names_part.split(",") if name.strip()]
    return names

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    parts = text.split(";")
    
    for part in parts:
        type_detected = analyze_message(part)
        names = extract_names(part)
        
        if type_detected and names:
            summary = f"{type_detected}: {', '.join(names)}"
            await send_confirmation(update, context, summary)
        else:
            ai_response = ask_gpt(part)
            await update.message.reply_text(f"AI допомога: {ai_response}")

async def send_confirmation(update, context, summary):
    keyboard = [
        [InlineKeyboardButton("✅ Так, підтверджую", callback_data='confirm')],
        [InlineKeyboardButton("📝 Ні, змінити", callback_data='edit')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f"Ваш запис: {summary}\nВсе вірно?", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'confirm':
        await query.edit_message_text(text="✅ Ваш запис підтверджено та буде передано.")
    elif query.data == 'edit':
        await query.edit_message_text(text="📝 Будь ласка, напишіть змінений запис.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if __name__ == "__main__":
    main()
