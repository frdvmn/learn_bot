from random import randint, choice
import emoji
import settings
import requests
import json
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

def request_test():
    oauth_token = "5jYTWecadG946dmkJd13APjvyKMuer6RNJpfTspsgwUn3uuzquDqHCYEFZvVQS" 

    # URL запроса
    url = f"https://smarty.mail.ru/api/v1/persons/set?oauth_token={oauth_token}&oauth_provider=mcs"

    # Заголовки запроса
    headers = {
        "accept": "application/json",
        "Content-Type": "multipart/form-data"
    }

    # Данные запроса
    data = {
        "meta": json.dumps({
            "space": "5",
            "images": [
                {
                    "name": "file",
                    "person_id": 1
                }
            ]
        })
    }

    # Файл для отправки
    file = open("images.jpg", "rb")

    # Отправка запроса
    response = requests.post(url, headers=headers, data=data, timeout=10, stream=True, files={"file": file})

    # Закрытие файла
    file.close()

    # Проверка ответа
    if response.status_code == 200:
        print("Запрос отправлен успешно!")
        print(response.json())
    else:
        print("Ошибка:", response.text)
        response = requests.post(url, data={
            'accept':'application/json',
            'Content-Type':'multipart/form-data',
            "meta":{
            "space": "5",
            "images": [
                    {
                        "name": "file",
                        "person_id": 1
                    }
                ]
            }
        })

if __name__ == "__main__":
    # request_test()
    pass