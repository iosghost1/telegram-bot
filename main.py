import os
import random
import string
import asyncio
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

valid_codes = set()

# command /code
async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    valid_codes.add(new_code)
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Kontrollo që URL-ja nuk ka "/" në fund
if WEBHOOK_URL and WEBHOOK_URL.endswith("/"):
    WEBHOOK_URL = WEBHOOK_URL[:-1]

bot_app = ApplicationBuilder().token(TOKEN).build()
bot_app.add_handler(CommandHandler("code", code))

# webhook route
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot_app.bot)
        # Përdor loop-in ekzistues për procesimin
        asyncio.run_coroutine_threadsafe(bot_app.process_update(update), loop)
        return "ok"
    return "error"

# test route
@app.route("/")
def home():
    return "Server is running ✅"

# START
if __name__ == "__main__":
    # Krijojmë një loop global për asyncio
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def setup_webhook():
        await bot_app.initialize()
        # Vendosja e webhook
        success = await bot_app.bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")
        print(f"Webhook set status: {success}")

    loop.run_until_complete(setup_webhook())

    # Nisim Flask
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
