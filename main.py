import os
import random
import string
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Funksioni për komandën /code
async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

# Merr variablat nga Render
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
PORT = int(os.environ.get("PORT", 10000))

# Ndërtimi i Botit
application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("code", code))

# Nisja me Webhook (Mënyra zyrtare e librarisë)
if __name__ == "__main__":
    # Kjo metodë rregullon automatikisht portin dhe lidhjen me Render
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}"
    )
