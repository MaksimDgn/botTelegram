#!env3/bin/python

#coding=utf-8


"""
КАК СОЗДАТЬ ТЕЛЕГРАМ-БОТА НА PYTHON ЗА 10 МИНУТ?
https://youtu.be/iCHzulEKR3k
"""
from subprocess import Popen
from subprocess import PIPE

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from config import TG_TOKEN
# import requests
# import os
# import pprint
# pip install requests[socks] pyTelegramBotAPI
# bpython
# pprint.pprint(r.json())


def ftok():
    f = open('token.txt')
    tok = f.read()
#    print(tok)
    f.close()
    return tok
""" menu bot 
start - запуск
help - помощь
time - узнать серверное время
"""
TOKEN = ''
# print(TOKEN)
""" Обработчики событий от телеграма """
def do_start(update, context ):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Отправь мне что-нибудь")

    
def do_help(update, context):
    chat_id = update.message.chat_id
    text = "Это учебный бот\nСписок доступных команд есть в меню\nТак же я отвечаю на любое сообщение"
    context.bot.send_message(chat_id=update.message.chat_id, text=text)

    
def do_time(update, context):
    """Узнать серверное время"""
    process = Popen(["date"], stdout=PIPE)
    text, error = process.communicate() # подождать результат
    
    if error:
        text = "Произошла ошибка, время неизвестно"
    else:
        # Декодировать ответ команды из процесса
        text = text.decode("utf-8")

    context.bot.send_message(chat_id=update.message.chat_id, text=text)


def do_echo(update, context):
    chat_id = update.message.chat_id
    text = "Ваш ID = {}\n\n{}".format(chat_id, update.message.text)
    context.bot.send_message(chat_id=update.message.chat_id, text=text)

    
def main():

#    print(TG_TOKEN)
    bot = Bot(token=TG_TOKEN)
    updater = Updater(bot=bot)

    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
    time_handler = CommandHandler("time", do_time)
    message_handler = MessageHandler(Filters.text, do_echo)


    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__=='__main__':
    main()
    
    
# for i in list:
#     print(i
