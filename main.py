import os
import random
import string
import asyncio
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import Application

# Konfigurimi
TOKEN = os.getenv("BOT_TOKEN")
URL = "https://onrender.com"

app = Flask(__name__)
# Krijojmë aplikacionin e botit
application = Application.builder().token(TOKEN).build()

# Funksioni për /code
async def generate_code(update):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

@app.route(f'/{TOKEN}', methods=['POST'])
async def webhook():
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), application.bot)
        
        # Kontrollojmë nëse mesazhi është /code
        if update.message and update.message.text == "/code":
            await generate_code(update)
            
        return "ok", 200

@app.route('/')
def index():
    return "Bot is running..."

async def set_webhook():
    bot = Bot(token=TOKEN)
    await bot.set_webhook(url=f"{URL}/{TOKEN}")

if __name__ == '__main__':
    # Vendosim webhook-un kur niset
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_webhook())
    
    # Nisim serverin
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
