from telebot import TeleBot
from os import path, mkdir
import json


with open(path.dirname(__file__)+'/TelegramBotTOKEN.json', 'r') as file:
    TOKEN = json.load(file)['TelegramBotTOKEN']

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_reply(message):
    bot.send_message(message.chat.id, 'Я помогу тебе вспонить про днюхи')


class UserForgotter:

    def __init__(self, user_id_telegram):
        self.id = user_id_telegram

    def create_user_dirrectory(self):
        directory = path.join(path.dirname(__file__), 'user_data',
                              str(self.id), ''
                              )
        if path.exists(directory):
            pass
        else:
            mkdir(directory)


@bot.message_handler(content_types='text')
def user_dir_creation(message):
    user_id_telegram = message.from_user.id
    newuser = UserForgotter(user_id_telegram)
    newuser.create_user_dirrectory()


@bot.message_handler(func=lambda x: True)
def replt_to_u(message):
    bot.reply_to(message, 'Обрабатываю только картинку')


bot.polling()
