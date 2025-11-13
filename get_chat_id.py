from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

# ---------------- BOT TOKEN ----------------
# BotFather থেকে নেওয়া টোকেন বসাও
BOT_TOKEN = os.environ.get("BOT_TOKEN", "আপনার_bot_token")

if BOT_TOKEN == "" or BOT_TOKEN == "আপনার_bot_token":
    print("❌ BOT_TOKEN নেই। Environment variable এ ঠিক মতো বসাও।")
    exit()

# ---------------- Handler ----------------
async def print_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_text(f"✅ এই গ্রুপের Chat ID:\n{chat_id}")
    print("Chat ID:", chat_id)

# ---------------- Main ----------------
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # সকল Text message handle করবে
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), print_chat_id))
    
    print("🚀 Bot started. গ্রুপে কোনো message পাঠালে Chat ID দেখাবে।")
    app.run_polling()

if __name__ == "__main__":
    main()
