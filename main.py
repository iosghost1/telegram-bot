import os
import random
import string
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

# KJO ZHDUK GABIMIN 404
@app.route('/')
def index():
    return "Bot is Alive! ✅"

def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    URL = "https://telegram-bot-mpya.onrender.com"
    PORT = int(os.environ.get("PORT", 10000))

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("code", code))

    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
