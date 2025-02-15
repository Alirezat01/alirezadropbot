import telebot
import requests
import os  # برای دریافت توکن از متغیر محیطی

TOKEN = os.getenv("7689008198:AAFj2rjuRcqSramnQTqJGAp_R8OM0rmKymE")  # دریافت توکن از Railway
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! من یه ربات ایردراپ هستم.")

bot.polling()
