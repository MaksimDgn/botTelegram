#!env3/bin/python

#coding=utf-8


"""
КАК СОЗДАТЬ ТЕЛЕГРАМ-БОТА НА PYTHON ЗА 10 МИНУТ?
https://youtu.be/iCHzulEKR3k
КНОПКИ ДЛЯ TELEGRAM-БОТА НА PYTHON, ЧАСТЬ 1
https://youtu.be/XHGpmdPDMGQ?list=PLkeGs_OdUTP-uXDyLdCrn0yJeqsVAAjhY&t=158

ЧАСТЬ 2
https://youtu.be/Wg6brhq647Q
"""
from logging import getLogger
from datetime import datetime
from subprocess import Popen
from subprocess import PIPE

from telegram import Bot
from telegram import Update
from telegram import InlineKeyboardButton # отвечает за одну клавишу
from telegram import InlineKeyboardMarkup # вся клавиатура вместе
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler
from buttons import BUTTON1_HELP
from buttons import BUTTON2_TIME
from buttons import get_base_reply_keyboard
from buttons import get_my_inline_keyboard
from telegram import ReplyKeyboardRemove


from config import TG_TOKEN
from development import *
# import requests
# import os
# import pprint
# pip install requests[socks] pyTelegramBotAPI
# bpython
# pprint.pprint(r.json())



#config = load_config()

logger = logging.getLogger(__name__)

def debug_requests(f):
    """ Декоратор для отладки событий от телеграма
    """
    def inner(*args, **kwargs):
        try:
            logger.info(f"Обращение в функцию {f.__name__}")
            return f(*args, **kwargs)
        except Exception:
            logger.exception("Ошибка в обработчике {f.__name__}")
            raise

    return inner

#debug_requests = logger_factory(logger=logger)



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
button - показать кнопки
"""
TOKEN = ''
# print(TOKEN)

CALLBACK_BUTTON1_LEFT = "callback_button1_left"
CALLBACK_BUTTON2_RIGHT = 'callback_button2_right'
CALLBACK_BUTTON3_MORE = "callback_button3_more"
CALLBACK_BUTTON4_MY =  "callback_button4_my"
CALLBACK_BUTTON_HIDE_KEYBOARD = "Cпрятать/показать клавиатуру!"
CALLBACK_BUTTON_MYTEST = "callback_button_mytest"

TITLES = {CALLBACK_BUTTON1_LEFT:"Новое сообщение", CALLBACK_BUTTON2_RIGHT: 'Отредактировать', CALLBACK_BUTTON_HIDE_KEYBOARD: "спрятать/показать клавиатуру!",CALLBACK_BUTTON3_MORE: "Eще", CALLBACK_BUTTON4_MY: "callback_button4_my"}

def get_base_inline_keyboard():
    Titles = {CALLBACK_BUTTON1_LEFT:"Новое сообщение", CALLBACK_BUTTON2_RIGHT: 'send Foto/Отреда', CALLBACK_BUTTON_HIDE_KEYBOARD: "спрятать/показать клавиатуру", CALLBACK_BUTTON3_MORE: "Eще", CALLBACK_BUTTON4_MY: "Моя новая клава"}
    keyboard = [
        [InlineKeyboardButton(Titles[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT),
#         InlineKeyboardButton("Option ---", calback_data='2'),
         InlineKeyboardButton(Titles[CALLBACK_BUTTON2_RIGHT], callback_data=CALLBACK_BUTTON2_RIGHT),
         InlineKeyboardButton("Option 3 more", callback_data=CALLBACK_BUTTON3_MORE),
        ],
        [
         InlineKeyboardButton("CALLBACK_BUTTON4_MY", callback_data=CALLBACK_BUTTON4_MY),
         InlineKeyboardButton("Option 5", callback_data='5'),
         InlineKeyboardButton(Titles[CALLBACK_BUTTON_HIDE_KEYBOARD] , callback_data=CALLBACK_BUTTON_HIDE_KEYBOARD ),
        ],
        ]
#            InlineKeyboardButton(TITLES[CALLBACK_BUTTON2_RIGHT], calback_data=CALLBACK_BUTTON2_RIGHT),
#            InlineKeyboardButton(TITLES[CALLBACK_BUTTON3_MORE], calback_data=CALLBACK_BUTTON3_MORE)
    #     ],
   
    # ]
         
    # keyboard = [
    #     [
    #         InlineKeyboardButton(TITLES[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT),
    #         InlineKeyboardButton("Option 1", callback_data='1'),
    #         InlineKeyboardButton("Option 2", callback_data='2'),
    #     ],
    #     [InlineKeyboardButton("Option 3", callback_data='3')],
    # ] 
    
    return InlineKeyboardMarkup(keyboard)

def get_keyboard2():
    Titles = {CALLBACK_BUTTON1_LEFT:"111"}
    keyboard = [
        [InlineKeyboardButton(Titles[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT)]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_my_inline_keyboard2():
    Titles = {CALLBACK_BUTTON_MYTEST: "My test Button"}
    keyboard = [
        [InlineKeyboardButton(Titles[CALLBACK_BUTTON_MYTEST], callback_data=CALLBACK_BUTTON_MYTEST)]
    ]
#    return InlineKeyboardMarkup(keyboard=keyboard, callback_data=BUTTON1_TEST)
#    return InlineKeyboardMarkup(keyboard=keyboard, resize_keyboard=True,)
    return InlineKeyboardMarkup(keyboard)


@debug_requests
def keyboard_callback_handler(update: Update, context):
    """ Обработчик ВСЕХ кнопок со ВСЕХ клавиатур """
    query = update.callback_query
    data = query.data
    now = datetime.now()

    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == CALLBACK_BUTTON1_LEFT:
        # Удалим клавиатуру у прошлого сообщения
        # (на самом деле отредактируем его так, что тексе останется тот же, а клавиатура пропадет)
        query.edit_message_text(text=current_text, )#parse_mode=ParseMode.MARKDOWN,)
        # Отправим новое сообщение при нажатии на кнопку
        text = "Новое сообщение\n\n callback_query.data= {}".format(data)
        context.bot.send_message(chat_id=chat_id, text=text, reply_markup=get_base_inline_keyboard())
    elif data == CALLBACK_BUTTON2_RIGHT:
        # Отредактируем текст сообщения, но оставим клавиатуру
        query.edit_message_text(text="Текст отредактирован в {}".format(now))#,parse_mode=ParseMode.MARKDOWN)
        context.bot.send_message(chat_id=chat_id, text=f'You {current_text.lower()}?')
#        context.bot.send_photo(chat_id=update.message.chat_id, get("https://cdn.fishki.net/upload/post/201406/06/1275531/9c944406a89a61d775c41652fcc7b2a5.jpg").content)
        
    elif data == CALLBACK_BUTTON3_MORE:
        # Отредактируем текст сообщения, но оставим клавиатуру
        query.edit_message_text(text="Показать предыдущий экран клавиатуры", reply_markup=get_keyboard2())
    elif data == CALLBACK_BUTTON4_MY:
        # Отредактируем текст сообщения, но оставим клавиатуру
        query.edit_message_text(text="Показать мою новую экран клавиатуры", reply_markup=get_my_inline_keyboard2())
    elif data == CALLBACK_BUTTON_MYTEST:
        query.edit_message_text(text="Нажата MYTEST кнопка")
    elif data == CALLBACK_BUTTON_HIDE_KEYBOARD:
        # спрятать клавиатуру
        # работает только после отправке нового сообщене
        context.bot.send_message(chat_id=chat_id, text="Спрятать клавиатуру\n\nНажмите /start чтобы вернуть ее обратно", reply_markup=ReplyKeyboardRemove(),)


""" Обработчики событий от телеграма """
#    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Отправь мне что-нибудь", reply_markup=get_base_inline_keyboard())



@debug_requests
def do_start(update, context ):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Отправь мне что-нибудь", reply_markup=get_base_reply_keyboard())
#     context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Отправь мне что-нибудь", reply_markup=get_base_inline_keyboard())

    
@debug_requests
def do_help(update, context):
    update.message.reply_text(text = "Это учебный бот\nСписок доступных команд есть в меню\nТак же я отвечаю на любое сообщение", reply_markup=get_base_inline_keyboard())


# def do_help(update, context):
#     keyboard = [
#         [
#             InlineKeyboardButton("Option 1", callback_data='1'),
#             InlineKeyboardButton("Option 2", callback_data='2'),
#         ],
#         [InlineKeyboardButton("Option 3", callback_data='3')],
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text(text = "Это учебный бот\nСписок доступных команд есть в меню\nТак же я отвечаю на любое сообщение", reply_markup=reply_markup)
    

#@bot.message_handler(content_types=["text"])
def any_msg(update, context):
    keyboard = types.InlineKeyboardMarkup()
    switch_button = types.InlineKeyboardButton(text="Нажми меня", switch_inline_query="Telegram")
    keyboard.add(switch_button)
    context.bot.send_message(update.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)
    
    
@debug_requests
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

@debug_requests
def do_echo(update, context):
    chat_id = update.message.chat_id
#    text = "Ваш ID = {}\n\n{}".format(chat_id, update.message.text)
    text = update.message.text
    if text == BUTTON1_HELP:
        return do_help(update=update, context=context)
    elif text == BUTTON2_TIME:
        return do_time(update=update, context=context)
    else:
        reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
    
#    context.bot.send_message(chat_id=update.message.chat_id, text=text)
    context.bot.send_message(chat_id=update.message.chat_id, text=reply_text, reply_markup=get_base_inline_keyboard())

@debug_requests
def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Selected option: {}".format(query.data))

#    coroutine c++ учимся готовить С++ корутины на практике
# легаси код

@debug_requests
def help(update, context):
    update.message.reply_text("Use /start to test this bot.")
    
def main():
    logging.info('Запускаем бота...')
    logging.info('Start...')

#    print(TG_TOKEN)
    bot = Bot(token=TG_TOKEN)
    updater = Updater(bot=bot)

        # Проверить что бот корректно подключился к Telegram API
    info = bot.get_me()
    logging.info(f'Bot info: {info}')

    start_handler = CommandHandler("start", do_start)
    help_handler = CommandHandler("help", do_help)
#    help_handler = CommandHandler("help", any_msg)
    time_handler = CommandHandler("time", do_time)
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler, pass_chat_data=True)
    test_buttons_handler = CallbackQueryHandler(button)
    
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(time_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)
    updater.dispatcher.add_handler(test_buttons_handler)

    updater.start_polling()
    updater.idle()

    logger.info('Закончили...')


if __name__=='__main__':
    main()
    
    
# for i in list:
#     print(i
