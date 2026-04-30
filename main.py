from flask import Flask, request, jsonify
import os, random, string, threading
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

valid_codes = set()

# ===== WEBSITE =====
@app.route('/')
def home():
    return "Server is running"

@app.route('/verify')
def verify():
    code = request.args.get('code')
    if code in valid_codes:
        valid_codes.remove(code)
        return jsonify({'valid': True})
    return jsonify({'valid': False})

# ===== TELEGRAM =====
async def code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    valid_codes.add(new_code)
    await update.message.reply_text(f"Your code is: {new_code} 🔑")

def run_bot():
    TOKEN = os.getenv("BOT_TOKEN")
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("code", code))
    app_bot.run_polling()

# ===== START =====
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()

    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
