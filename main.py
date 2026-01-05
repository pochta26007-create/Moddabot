import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Sizning bot tokeningiz
TOKEN = "8316049030:AAHtWlkYh1p0HawQn-dcTyUem-KcEjnH-68"

bot = telebot.TeleBot(TOKEN)

# Bu funksiya har qanday xabar kelganda ishlaydi
def send_welcome(message):
    # Tugmani yaratamiz
    markup = InlineKeyboardMarkup()

    # Tugma ichidagi yozuv va silka (URL)
    btn = InlineKeyboardButton(text="📲 Ilovaga kirish", url="https://t.me/moddacheck_bot/check")

    # Tugmani menyuga qo'shamiz
    markup.add(btn)

    # Javob xabarini yuboramiz
    bot.reply_to(message, "Ushbu botdan foydalanish uchun quyidagi web ilovaga kiring:", reply_markup=markup)

# /start bosilganda ishlaydi
@bot.message_handler(commands=['start'])
def start_handler(message):
    send_welcome(message)

# Boshqa har qanday matn yozilganda ham ishlaydi
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    send_welcome(message)

print("Bot ishga tushdi! Telegramda tekshirib ko'ring...")
bot.infinity_polling()