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
#from buttons import get_base_inline_keyboard
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
BTN_BACK = "callback_btn_back"
BTN_FORWARD = "callback_btn_forward"
BTN_MAIN = "Меню"
CALLBACK_BTN_BACK = "callback_btn_back"
CALLBACK_BTN_FORWARD = "callback_btn_forward"
BTN_ABOUT = "О компании"
BTN_KATALOG = "Каталог"

""" Main btn"""
CALLBACK_BTN_NEW = "callback_btn_new"
CALLBACK_BTN_MAIN = "callback_btn_main"
CALLBACK_BTN_LIN = "callback_btn_lin"
CALLBACK_BTN_LAM = "callback_btn_lam"
CALLBACK_BTN_PLINT = "callback_btn_plint"

CALLBACK_BTN_NEW_LIN = "callback_btn_new_lin"

CALLBACK_BTN_LAM_0  = "callback_btn_lam_0"
CALLBACK_BTN_LAM_1  = "callback_btn_lam_1"
CALLBACK_BTN_LAM_2  = "callback_btn_lam_2"
CALLBACK_BTN_LAM_3  = "callback_btn_lam_3"
CALLBACK_BTN_LAM_4  = "callback_btn_lam_4"
CALLBACK_BTN_LAM_5  = "callback_btn_lam_5"
CALLBACK_BTN_LAM_6  = "callback_btn_lam_6"
CALLBACK_BTN_LAM_7  = "callback_btn_lam_7"
CALLBACK_BTN_LAM_8  = "callback_btn_lam_8"
CALLBACK_BTN_LAM_9  = "callback_btn_lam_9"


TITLES = {CALLBACK_BUTTON1_LEFT:"Новое сообщение", CALLBACK_BUTTON2_RIGHT: 'Отредактировать', CALLBACK_BUTTON_HIDE_KEYBOARD: "спрятать/показать клавиатуру!",CALLBACK_BUTTON3_MORE: "Eще", CALLBACK_BUTTON4_MY: "callback_button4_my"}

tel_1 = '+375 (44) 493-72-91'
tel_2 = '+375 (17) 504-81-81'
about = """\nБолее 5 лет продаём полы. \n\tМы предлагаем линолеум, ламинат, ковролин, МДФ, ПВХ и САЙДИНГ только от проверенных поставщиков, несущих ответственность за свою продукцию. Вне зависимости от коллекции и цены все строительно-отделочные материалы выбранный вами, будут отвечать главным европейским стандартам качества. Если же вам попался бракованный, то мы обязуемся заменить его – быстро и совершенно бесплатно!
\n\tМы всегда выезжаем к клиенту с образцами продукции, тем самым даём возможность приложить выбранный к вашему интерьеру.
\n\* Замер, консультация, доставка.
\nПри необходимости укладка линолеума ламината, ковролина, монтаж панелей МДФ и ПВХ.
\n* В каких городах мы работаем?
Продаем полы в Лиде, Новогрудоке, Кореличах. Выезжаем в сельскую местность по этим районам.."""

site = 'http://уютдом.бел/'
menu_bot = """
 menu bot 
/start@mrMarinBot \n
/start - запуск
/help - помощь
/time - узнать серверное время
/button - показать кнопки
/katalog - Каталог продукции
"""

"""Главная страница"""
main_page_text = f"Телефон :\n\t{tel_1} \n\t{tel_2}\n\nСайт: {site}\nО компании: {about}\n {menu_bot}"
"""кнопки: главной страници"""

"""кнопки: Каталог продукции"""
katalog_txt = """Каталог продукции
 Линолеум
 ламинат
 ковролин
 сайдинг
 МДФ
 панели
 ПВХ"""
#katalog_txt = f"Каталог продукции Линолеум ламинат ковролин сайдинг МДФ панели ПВХ"

def get_katalog_keyboard():
    Titles = {CALLBACK_BTN_NEW:"Новинки",
               CALLBACK_BTN_LIN: 'Линолиум',
               CALLBACK_BTN_LAM: 'Ламинад',
               CALLBACK_BTN_PLINT: 'Плинтус',
               CALLBACK_BUTTON3_MORE:"Eще",}
    keyboard = [
        [InlineKeyboardButton(Titles[CALLBACK_BTN_NEW], callback_data=CALLBACK_BTN_NEW)],
        [
            InlineKeyboardButton(Titles[CALLBACK_BTN_LIN], callback_data=CALLBACK_BTN_LIN),
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM], callback_data=CALLBACK_BTN_LAM),
            InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT),
        ],
        [InlineKeyboardButton(Titles[CALLBACK_BUTTON3_MORE], callback_data=CALLBACK_BUTTON3_MORE),],
        ]
    return InlineKeyboardMarkup(keyboard)



katalog_lam =[ 
'Kronostar (РФ)'
,'Tarkett (РФ)'
,'Classen (Германия)'
,'Kronopol (Польша)'
,'Helvetic Floors (Швейцария)'
,'SWISS KRONO AG (Швейцария)'    
,'VIVAFLOOR (РБ)'
,'Мостовдрев'
,'Подложка'
,'Timber']

katalog_lin =[ '«Таркетт» (Сербия / Россия)', '"Beau Flor" (Бельгия)' ,'«Синтерос» (Россия)', '«Juteks» (Россия)', ' «Комитекс Лин» (Россия)','"Polystyl" (Россия).']

def get_linolium_backForward_inlyne_keyboard():

    Titles = {CALLBACK_BTN_NEW_LIN: katalog_lin[0],
              CALLBACK_BTN_LIN: katalog_lin[1],
              CALLBACK_BTN_LAM: katalog_lin[2],
              CALLBACK_BTN_PLINT: katalog_lin[3],
              CALLBACK_BTN_PLINT: katalog_lin[4],
              CALLBACK_BTN_PLINT: katalog_lin[5],
              CALLBACK_BUTTON3_MORE:"Eще",}
    keyboard = [
        [InlineKeyboardButton(Titles[CALLBACK_BTN_NEW_LIN], callback_data=CALLBACK_BTN_NEW_LIN),        
        InlineKeyboardButton(Titles[CALLBACK_BTN_LIN], callback_data=CALLBACK_BTN_LIN)],
        [
        InlineKeyboardButton(Titles[CALLBACK_BTN_LAM], callback_data=CALLBACK_BTN_LAM),        
        InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT )],
        [
            InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT ),
            InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT)],

        [InlineKeyboardButton(Titles[CALLBACK_BUTTON3_MORE], callback_data=CALLBACK_BUTTON3_MORE),],
        ]    
    return InlineKeyboardMarkup(keyboard) 


def get_laminad_backForward_inlyne_keyboard():

    Titles = {CALLBACK_BTN_LAM_0: katalog_lam[0],
              CALLBACK_BTN_LAM_1: katalog_lam[1],
              CALLBACK_BTN_LAM_2: katalog_lam[2],
              CALLBACK_BTN_LAM_3: katalog_lam[3],
              CALLBACK_BTN_LAM_4: katalog_lam[4],
              CALLBACK_BTN_LAM_5: katalog_lam[5],
              CALLBACK_BTN_LAM_6: katalog_lam[6],
              CALLBACK_BTN_LAM_7: katalog_lam[7],
              CALLBACK_BTN_LAM_8: katalog_lam[8],
              CALLBACK_BTN_LAM_9: katalog_lam[9],
              CALLBACK_BUTTON3_MORE:"Eще",}
    keyboard = [
        [InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_0], callback_data=CALLBACK_BTN_LAM_0),        
         InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_1], callback_data=CALLBACK_BTN_LAM_1)],
        [                                                                            
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_2], callback_data=CALLBACK_BTN_LAM_2),
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_3], callback_data=CALLBACK_BTN_LAM_3)],
        [                                                                               
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_4], callback_data=CALLBACK_BTN_LAM_4),
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_5], callback_data=CALLBACK_BTN_LAM_5)],
        [                                                                               
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_6], callback_data=CALLBACK_BTN_LAM_6),        
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_7], callback_data=CALLBACK_BTN_LAM_7)],
        [                                                                               
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_8], callback_data=CALLBACK_BTN_LAM_8),
            InlineKeyboardButton(Titles[CALLBACK_BTN_LAM_9], callback_data=CALLBACK_BTN_LAM_9)
        ],
        # [                                                    
        #  InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT ),
        #  InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT)],

        [InlineKeyboardButton(Titles[CALLBACK_BUTTON3_MORE], callback_data=CALLBACK_BUTTON3_MORE),],
        ]    
    return InlineKeyboardMarkup(keyboard)



def get_base_inline_keyboard():
    Titles = {CALLBACK_BUTTON1_LEFT:"Новое сообщение", CALLBACK_BUTTON2_RIGHT: 'send Foto/Отреда', CALLBACK_BUTTON_HIDE_KEYBOARD: "спрятать/показать клавиатуру", CALLBACK_BUTTON3_MORE: "Eще", CALLBACK_BUTTON4_MY: "Каталог картинок"}
    Titles2 = {CALLBACK_BTN_NEW:"Новинки",
           CALLBACK_BTN_LIN: 'Линолиум',
           CALLBACK_BTN_LAM: 'Ламинад',
           CALLBACK_BTN_PLINT: 'Плинтус',
           CALLBACK_BUTTON3_MORE:"Eще",}
    keyboard = [
        [InlineKeyboardButton(Titles2[CALLBACK_BTN_NEW], callback_data=CALLBACK_BTN_NEW)],
        [
         InlineKeyboardButton(Titles2[CALLBACK_BTN_LIN], callback_data=CALLBACK_BTN_LIN),
         InlineKeyboardButton(Titles2[CALLBACK_BTN_LAM], callback_data=CALLBACK_BTN_LAM),
         InlineKeyboardButton(Titles2[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT),
        ],
        [
         InlineKeyboardButton(Titles2[CALLBACK_BUTTON3_MORE], callback_data=CALLBACK_BUTTON3_MORE),
        ],
        ]    
    # keyboard = [
    #     [InlineKeyboardButton(Titles[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT),
    #      InlineKeyboardButton(Titles[CALLBACK_BUTTON2_RIGHT], callback_data=CALLBACK_BUTTON2_RIGHT),
    #      InlineKeyboardButton("Option 3 more", callback_data=CALLBACK_BUTTON3_MORE),
    #     ],
    #     [
    #      InlineKeyboardButton(Titles[CALLBACK_BUTTON4_MY], callback_data=CALLBACK_BUTTON4_MY),
    #      InlineKeyboardButton("Option 5", callback_data='5'),
    #      InlineKeyboardButton(Titles[CALLBACK_BUTTON_HIDE_KEYBOARD] , callback_data=CALLBACK_BUTTON_HIDE_KEYBOARD ),
    #     ],
    #     ]
    return InlineKeyboardMarkup(keyboard)



def get_keyboard2():
    Titles = {CALLBACK_BUTTON1_LEFT:"111 BUTTON1_LEFT"}
    keyboard = [
        [InlineKeyboardButton(Titles[CALLBACK_BUTTON1_LEFT], callback_data=CALLBACK_BUTTON1_LEFT)]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_my_inline_keyboard2():
    Titles = {CALLBACK_BUTTON_MYTEST: "My test Button(Каталог картинок)"}
    keyboard = [
        [InlineKeyboardButton(Titles[CALLBACK_BUTTON_MYTEST], callback_data=CALLBACK_BUTTON_MYTEST)]
    ]
#    return InlineKeyboardMarkup(keyboard=keyboard, callback_data=BUTTON1_TEST)
#    return InlineKeyboardMarkup(keyboard=keyboard, resize_keyboard=True,)
    return InlineKeyboardMarkup(keyboard)



def get_backForward_inlyne_keyboard():#👈👉🏻➡️⬅️
    Titles = {BTN_BACK: "👈⬅️Назад", BTN_FORWARD: "Вперед 👉🏻➡️", BTN_MAIN: "- Меню -"}
    keyboard = [
        [InlineKeyboardButton(Titles[BTN_BACK], callback_data=CALLBACK_BTN_BACK),
         InlineKeyboardButton(Titles[BTN_FORWARD], callback_data=CALLBACK_BTN_FORWARD)],
        [InlineKeyboardButton(Titles[BTN_MAIN], callback_data=CALLBACK_BTN_MAIN)]
    ]
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

        
    elif data == CALLBACK_BUTTON3_MORE:
        # Отредактируем текст сообщения, но оставим клавиатуру
        query.edit_message_text(text="Показать предыдущий экран клавиатуры", reply_markup=get_keyboard2())
    elif data == CALLBACK_BUTTON4_MY:
        # Отредактируем текст сообщения, но оставим клавиатуру
        query.edit_message_text(text="Это новая экран-клавиатура 👍❤️", reply_markup=get_my_inline_keyboard2())
    elif data == CALLBACK_BUTTON_MYTEST:
        # Выводит сообщение, картинку, клавиатуру
        query.edit_message_text(text="'edit_message_text'\ntext = Нажата MYTEST кнопка")
        context.bot.send_photo(chat_id=chat_id, photo='https://cdn.fishki.net/upload/post/201406/06/1275531/9c944406a89a61d775c41652fcc7b2a5.jpg')
        context.bot.send_message(chat_id=chat_id, text='Каталог картинок', reply_markup=get_backForward_inlyne_keyboard())
        
    elif data == CALLBACK_BTN_BACK :
        context.bot.send_photo(chat_id=chat_id, photo='https://img2.pngindir.com/20191029/rjp/transparent-green-text-font-circle-5db7c9c7e47a80.2378616215723258319359.jpg')
        context.bot.send_message(chat_id=chat_id, text="нажата кнопка 'назад'", reply_markup=get_backForward_inlyne_keyboard())
        #context.bot.send_message(chat_id=chat_id, text='', reply_markup=get_base_inline_keyboard())
    elif data == CALLBACK_BTN_FORWARD :
        context.bot.send_photo(chat_id=chat_id, photo='https://st.depositphotos.com/1168775/1325/i/950/depositphotos_13251648-stock-photo-ok-green-button.jpg')
        context.bot.send_message(chat_id=chat_id, text="нажата кнопка вперед", reply_markup=get_backForward_inlyne_keyboard())
    elif data == CALLBACK_BUTTON_HIDE_KEYBOARD:
        # спрятать клавиатуру
        # работает только после отправке нового сообщене
        context.bot.send_message(chat_id=chat_id, text="Спрятать клавиатуру\n\nНажмите /start чтобы вернуть ее обратно", reply_markup=ReplyKeyboardRemove(),)

    elif data == CALLBACK_BTN_NEW:
        context.bot.send_photo(chat_id=chat_id, photo='https://st.depositphotos.com/1168775/1325/i/950/depositphotos_13251648-stock-photo-ok-green-button.jpg')
        context.bot.send_message(chat_id=chat_id, text="нажата кнопка NEW", reply_markup=ReplyKeyboardRemove())
    elif data == CALLBACK_BTN_MAIN:
        context.bot.send_message(chat_id=chat_id, text="нажата кнопка MAIN", reply_markup=get_base_inline_keyboard())
    elif data == CALLBACK_BTN_LIN:
        context.bot.send_photo(chat_id=chat_id, photo='http://www.santrade.by/IVC/Ravena%201%20931.png')
       # context.bot.send_message(chat_id=chat_id, text="нажата кнопка Линолиум", reply_markup=get_backForward_inlyne_keyboard())
        context.bot.send_message(chat_id=chat_id, text="нажата кнопка Линолиум", reply_markup=get_linolium_backForward_inlyne_keyboard())
    elif data == CALLBACK_BTN_LAM:
        context.bot.send_photo(chat_id=chat_id, photo='http://www.santrade.by/Kronostar/whitened-oak.png')
        context.bot.send_message(chat_id=chat_id, text="нажата кнопка Ламинад", reply_markup=get_laminad_backForward_inlyne_keyboard())
        
    elif data == CALLBACK_BTN_PLINT:
        context.bot.send_photo(chat_id=chat_id, photo='https://st.depositphotos.com/1168775/1325/i/950/depositphotos_13251648-stock-photo-ok-green-button.jpg')
        context.bot.send_message(chat_id=chat_id, text="нажата кнопка Плинтус", reply_markup=get_backForward_inlyne_keyboard())
        

""" Обработчики событий от телеграма """
#    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Отправь мне что-нибудь", reply_markup=get_base_inline_keyboard())





@debug_requests
def do_start(update, context ):
    context.bot.send_message(chat_id=update.message.chat_id, text=main_page_text, reply_markup=get_base_reply_keyboard())
#     context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Отправь мне что-нибудь", reply_markup=get_base_inline_keyboard())


@debug_requests
def do_adout(update, context):
    update.message.reply_text(text=about, reply_markup=get_base_inline_keyboard())

@debug_requests
def do_katalog(update, context):
    update.message.reply_text(text=katalog_txt, reply_markup=get_katalog_keyboard())
    
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
    if text == BTN_ABOUT:
       
        # context.bot.send_message(chat_id=chat_id, text="Спрятать клавиатуру\n\nНажмите /start чтобы вернуть ее обратно", reply_markup=ReplyKeyboardRemove(),)
       # context.bot.send_message(chat_id=update.message.chat_id, text=about, reply_markup=get_base_inline_keyboard())
        return do_adout(update=update, context=context)
    elif text == BTN_KATALOG:
        reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
       # context.bot.send_message(chat_id=update.message.chat_id, text=reply_text, reply_markup=get_base_inline_keyboard())
        return do_katalog(update=update, context=context)
    if text == BTN_BACK:
        print(text)
        return go_back(update=Update, context=context)
    else:
        reply_text = "Ваш ID = {}\n\n{}".format(chat_id, text)
        context.bot.send_message(chat_id=update.message.chat_id, text=reply_text, reply_markup=get_base_inline_keyboard())
#    context.bot.send_message(chat_id=update.message.chat_id, text=text)


@debug_requests
def go_back(update, context):
    chat_id = update.message.chat_id
#    text = "Ваш ID = {}\n\n{}".format(chat_id, update.message.text)
    text = update.message.text
    print(f'go_back{text}')
    if text == BTN_BACK:
        print(f'go_back{text} in BTN_BACK')
        context.bot.send_photo(chat_id=chat_id, photo='https://img2.pngindir.com/20191029/rjp/transparent-green-text-font-circle-5db7c9c7e47a80.2378616215723258319359.jpg')
        return to_back(update=Update, context=context)
    if text == BTN_FORWARD:
        context.bot.send_photo(chat_id=chat_id, photo='https://st.depositphotos.com/1168775/1325/i/950/depositphotos_13251648-stock-photo-ok-green-button.jpg')
        return to_forward(update=Update, context=context)
    else:
        reply_text = f"нажата {text} клавиша"
#    context.bot.send_message(chat_id=update.message.chat_id, text=reply_text, reply_markup=get_backForward_reply_keyboard())

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
    about_handler = CommandHandler("about", do_adout)
    katalog_handler = CommandHandler("katalog", do_katalog)
    
    message_handler = MessageHandler(Filters.text, do_echo)
    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler, pass_chat_data=True)
    test_buttons_handler = CallbackQueryHandler(button)
    
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(about_handler)
    updater.dispatcher.add_handler(help_handler)
    updater.dispatcher.add_handler(katalog_handler)
#    updater.dispatcher.add_handler(back_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(buttons_handler)
    updater.dispatcher.add_handler(test_buttons_handler)


    updater.start_polling()
    updater.idle()

    logger.info('Закончили...')


if __name__=='__main__':
    main()
