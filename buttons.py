from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup # вся клавиатура вместе


BUTTON1_HELP = "Помощь"
BUTTON2_TIME = "Время"
BUTTON1_TEST = "My test Button"
CALLBACK_BUTTON4_MY =  "callback_button4_my"

def get_base_reply_keyboard():
    BUTTON1_HELP = "Помощь"
    BUTTON2_TIME = "Время"
    keyboard = [
        [
            KeyboardButton(BUTTON1_HELP),
            KeyboardButton(BUTTON2_TIME),
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        )


def get_my_inline_keyboard():
    Titles = {CALLBACK_BUTTON4_MY: "My test Button"}
    keyboard = [
        [KeyboardButton(Titles[CALLBACK_BUTTON4_MY], CALLBACK_BUTTON4_MY)]
    ]
#    return InlineKeyboardMarkup(keyboard=keyboard, callback_data=BUTTON1_TEST)
#    return InlineKeyboardMarkup(keyboard=keyboard, resize_keyboard=True,)
    return InlineKeyboardMarkup(keyboard)
