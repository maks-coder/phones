import telebot
bot = telebot.TeleBot('853431161:AAExT6S_YE6ab64sA4hxX4fDZYTNvPrlQWo')
@bot.message_handler(content_types=['text'])
def send_welcome(message):
    bot.send_message(message, "lol")

bot.polling()