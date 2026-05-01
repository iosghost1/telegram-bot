import os
import random
import string
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Loget për të parë gabimet
logging.basicConfig(level=logging.INFO)

async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

def main():
    # Merr variablat nga Render
    TOKEN = os.environ.get("BOT_TOKEN")
    URL = "https://onrender.com"
    PORT = int(os.environ.get("PORT", 10000))

    if not TOKEN:
        print("GABIM: BOT_TOKEN nuk eshte vendosur ne Render!")
        return

    # Ndertimi i aplikacionit
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("code", code))

    # Nisja e Webhook
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
