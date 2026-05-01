import os
import random
import string
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Funksioni për gjenerimin e kodit
async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

# Konfigurimet kryesore
TOKEN = os.getenv("BOT_TOKEN")
# Këtu vendosëm linkun tënd direkt për të shmangur gabimin "failed to resolve host"
MY_URL = "https://telegram-bot-mpya.onrender.com"
PORT = int(os.environ.get("PORT", 10000))

# Ndërtimi i aplikacionit të botit
application = ApplicationBuilder().token(TOKEN).build()

# Shtimi i komandës /code
application.add_handler(CommandHandler("code", code))

if __name__ == "__main__":
    # Nisja e Webhook-ut
    # Kjo do të lidhë https://onrender.com me Telegramin
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{MY_URL}/{TOKEN}"
    )
