from flask import Flask, request
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace with your actual bot token
TOKEN = '7205713684:AAEFtrxxIjHvMEBg-Vd3fki_YgopbJfVcU0'

# Flask web server initialization
app = Flask(__name__)

# Bot initialization
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define your handlers here
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your bot.")

# Command handler
dispatcher.add_handler(CommandHandler("start", start))

# Function to set up webhook
def set_webhook():
    webhook_url = 'https://your-webhook-url/'  # Replace with your actual webhook URL
    updater.bot.set_webhook(webhook_url + TOKEN)

# Flask route to set up webhook
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook() -> str:
    """Webhook endpoint for Telegram updates."""
    update = Update.de_json(request.get_json(force=True), updater.bot)
    dispatcher.process_update(update)
    return 'ok'

if __name__ == '__main__':
    # Set webhook before starting Flask server
    set_webhook()
    # Start Flask server
    app.run(port=8443)