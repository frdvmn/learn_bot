from random import randint, choice
import emoji
import settings
import requests

from telegram import ReplyKeyboardMarkup, KeyboardButton

def main_keyboard():
    keyboard = [
        [
            "Вызвать кота",
            "/start",
        ],
        [
            KeyboardButton("Мои координаты", request_location=True),
            "Заполнить анкету",
        ]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)

def get_emoji(user_data, smile = settings.USER_EMOJI):
    if 'emoji' not in user_data:
        if type(smile) is list:
            smile = choice(smile)
        user_data['emoji'] = emoji.emojize(smile)
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, вы выиграли" 
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, ничья"
    else:
        message = f"Ваше число {user_number}, мое {bot_number}, вы проиграли"
    return message

def is_cat():
    pass

if __name__ == "__main__":
    pass