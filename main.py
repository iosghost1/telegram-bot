import os
import random
import string
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# store valid codes
valid_codes = set()

# command /code
async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    valid_codes.add(new_code)
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

TOKEN = os.getenv("BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("code", code))

if __name__ == "__main__":
    app.run_polling()
