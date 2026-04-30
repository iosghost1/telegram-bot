from flask import Flask
import threading
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# TELEGRAM BOT
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot is ON 🔥")

def run_bot():
    TOKEN = os.getenv("BOT_TOKEN")
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.run_polling()

# RUN BOTH
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
