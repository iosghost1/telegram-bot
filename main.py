import os
import random
import string
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

valid_codes = set()

async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    valid_codes.add(new_code)
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("code", code))

@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    await bot_app.process_update(update)
    return "ok"

@app.route("/")
def home():
    return "Server is running ✅"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot_app.initialize())
    loop.run_until_complete(
        bot_app.bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")
    )

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
