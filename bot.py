import telebot
import requests
import os  # برای دریافت توکن از متغیر محیطی

TOKEN = os.getenv("BOT_TOKEN")  # دریافت توکن از Railway
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من یه ربات ایردراپ هستم.")

bot.polling()
