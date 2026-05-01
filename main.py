import os
import random
import string
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ky aktivizon loget që të shohim çfarë ndodh te Render
logging.basicConfig(level=logging.INFO)

async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Kjo do shfaqet te Logs kur dikush shkruan /code
    print("Komanda /code u mor!") 
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

TOKEN = os.environ.get("BOT_TOKEN")
URL = "https://onrender.com"
PORT = int(os.environ.get("PORT", 10000))

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("code", code))

    # Kjo duhet të jetë fiks kështu
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
