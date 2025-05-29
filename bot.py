from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from agent import ask_gpt

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    ai_response = ask_gpt(text)
    await update.message.reply_text(f"Ваш запис подано: {ai_response}")
