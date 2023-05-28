import telebot
import webbrowser
from key import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}")


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://youtube.com')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, "<b>Help information</b>", parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == "hello":
        bot.send_message(
            message.chat.id, f"Hello, {message.from_user.first_name} {message.from_user.last_name}")
    elif message.text.lower() == 'id':
        bot.reply_to(message, f"ID: {message.from_user.id}")


bot.polling(none_stop=True)
