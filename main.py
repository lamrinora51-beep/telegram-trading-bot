import telebot
import requests
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def get_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    return float(data["price"])

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🤖 البوت يعمل!")

@bot.message_handler(commands=['price'])
def price(message):
    p = get_price()
    bot.reply_to(message, f"💰 سعر BTC: {p}")

bot.infinity_polling()
