import os
import random
import string
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ky aktivizon loget që të shohim gabimet te Render
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Funksioni /code
async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

# Variablat nga Render
TOKEN = os.environ.get("BOT_TOKEN")
# Linku yt pa slash në fund
URL = "https://onrender.com"
PORT = int(os.environ.get("PORT", 10000))

def main():
    # Ndërtimi i aplikacionit
    application = ApplicationBuilder().token(TOKEN).build()

    # Shto komandën /code
    application.add_handler(CommandHandler("code", code))

    # Nisja e webhook
    # Render kërkon që boti të dëgjojë në 0.0.0.0
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{URL}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
