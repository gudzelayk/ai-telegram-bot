async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    ai_response = ask_gpt(text)
    add_entry_to_sheet(ai_response)
    await update.message.reply_text(f"Ваш запис подано: {ai_response}")
