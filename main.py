import os
import random
import string
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Aktivizojmë loget
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Gabim: {context.error}")

def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    URL = "https://onrender.com"
    PORT = int(os.environ.get("PORT", 10000))

    # Ndërtimi i aplikacionit
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("code", code))
    application.add_error_handler(error_handler)

    # Ky rresht është KRITIK për Render
    logger.info(f"Boti po niset në portin {PORT}")
    
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{URL}/{TOKEN}",
        drop_pending_updates=True
    )
if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("code", code))

    # Kjo metodë e thjeshtuar shmang gabimet e rrugës (path)
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=f"{URL}/{TOKEN}"
    )

