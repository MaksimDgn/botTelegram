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
