from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "BOT_TOKEN"  # এখানে BotFather থেকে নেওয়া টোকেন বসাও

async def print_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"এই গ্রুপের Chat ID:\n{chat_id}")
    print("Chat ID:", chat_id)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), print_chat_id))
app.run_polling()
