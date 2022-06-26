import telebot

bot = telebot.TeleBot('5162863791:AAG2K1o6pMKdPIaB_RO7mrh5D_Lp--jUE54', parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hi, Gleb! How are you doing?')


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
