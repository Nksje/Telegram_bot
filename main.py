import telebot
from key import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, "<b>Help information</b>", parse_mode='html')


bot.polling(none_stop=True)
