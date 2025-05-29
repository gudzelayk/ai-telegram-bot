from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from agent import ask_gpt
from config import TELEGRAM_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я бот для подачі записок на церковні служби. Напиши свої імена.")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    ai_response = ask_gpt(text)
    await update.message.reply_text(f"Ваш запис подано: {ai_response}")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == "__main__":
    main()
