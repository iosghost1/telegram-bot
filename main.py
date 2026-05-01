import os
import random
import string
import logging
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Loget
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

@app.route('/')
def home():
    return "Bot is Alive!", 200

def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    URL = "https://onrender.com"
    PORT = int(os.environ.get("PORT", 10000))

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("code", code))

    # Ky rresht e mban botin ndezur dhe i pergjigjet Render-it
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
