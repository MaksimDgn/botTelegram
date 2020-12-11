from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup # вся клавиатура вместе

BTN_MAIN = "Меню"
BUTTON1_HELP = "Помощь"
BUTTON2_TIME = "Время"
BUTTON1_TEST = "My test Button"
BTN_BACK = "callback_btn_back"
BTN_FORWARD = "callback_btn_forward"
BTN_ABOUT = "О компании"
BTN_KATALOG = "Каталог"


# CALLBACK_BTN_MAIN = "callback_btn_main"
# CALLBACK_BTN_LIN = "callback_btn_lin"
# CALLBACK_BTN_LAM = "callback_btn_lam"
# CALLBACK_BTN_PLINT = "callback_btn_plint"
# CALLBACK_BTN_NEW_LIN_b = "callback_btn_new_lin"
# CALLBACK_BUTTON3_MORE = "callback_button3_more"

# katalog_lin_b =[ 'b«Таркетт» (Сербия / Россия)', '"Beau Flor" (Бельгия)' ,'«Синтерос» (Россия)', '«Juteks» (Россия)', ' «Комитекс Лин» (Россия)','"Polystyl" (Россия).']

# def get_linolium_backForward_inlyne_keyboard():

#     Titles = {CALLBACK_BTN_NEW_LIN_b: katalog_lin_b[0],
#               CALLBACK_BTN_LIN: katalog_lin_b[1],
#               CALLBACK_BTN_LAM: katalog_lin_b[2],
#               CALLBACK_BTN_PLINT: katalog_lin_b[3],
#               CALLBACK_BTN_PLINT: katalog_lin_b[4],
#               CALLBACK_BTN_PLINT: katalog_lin_b[5],
#               CALLBACK_BUTTON3_MORE:"Eще",}
#     keyboard = [
#         [InlineKeyboardButton(Titles[CALLBACK_BTN_NEW_LIN_b], callback_data=CALLBACK_BTN_NEW_LIN_b),        
#         InlineKeyboardButton(Titles[CALLBACK_BTN_LIN], callback_data=CALLBACK_BTN_LIN)],
#         [
#         InlineKeyboardButton(Titles[CALLBACK_BTN_LAM], callback_data=CALLBACK_BTN_LAM),        
#         InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT )],
#         [
#             InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT ),
#             InlineKeyboardButton(Titles[CALLBACK_BTN_PLINT], callback_data=CALLBACK_BTN_PLINT)],

#         [InlineKeyboardButton(Titles[CALLBACK_BUTTON3_MORE], callback_data=CALLBACK_BUTTON3_MORE),],
#         ]    

#     return InlineKeyboardMarkup(keyboard)


def get_base_reply_keyboard():
    BUTTON1_HELP = "Помощь"
    BUTTON2_TIME = "Время"
    BTN_ABOUT = "О компании"
    BTN_KATALOG = "Каталог"
    keyboard = [
        [
            KeyboardButton(BTN_KATALOG),
            KeyboardButton(BTN_ABOUT),
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        )


def get_backForward_reply_keyboard():#👈👉🏻➡️⬅️
    Titles = {BTN_BACK: "👈⬅️Назад", BTN_FORWARD: "Вперед 👉🏻➡️", BTN_MAIN: "- Меню -"}
    keyboard = [
        [KeyboardButton(Titles[BTN_BACK]),
         KeyboardButton(Titles[BTN_FORWARD])],
        [KeyboardButton(Titles[BTN_MAIN])]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True,)



""" Пример Inline клавиатуры
def get_backForward_reply_keyboard():
    Titles = {CALLBACK_BTN_BACK: "Назад", CALLBACK_BTN_FORWARD: "Вперед"}
    keyboard = [
        [KeyboardButton(Titles[CALLBACK_BTN_FORWARD], CALLBACK_BTN_FORWARD),
         KeyboardButton(Titles[CALLBACK_BTN_FORWARD], CALLBACK_BTN_FORWARD)]
    ]
    return InlineKeyboardMarkup(keyboard)
"""
