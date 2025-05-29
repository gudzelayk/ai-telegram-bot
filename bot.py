from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from agent import ask_gpt
from sheets import add_entry_to_sheet

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    ai_response = ask_gpt(text)
    await update.message.reply_text(f"Ваш запис подано: {ai_response}")
