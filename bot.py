import logging

from telegram.ext import Application, MessageHandler, CommandHandler, filters
from handlers import greet_user, guess_number, send_cat_picture, user_coordinates, message

import settings
# Отслеживание ошибок
logging.basicConfig(filename="bot.log", level=logging.INFO)

def main():
    
    # Cоздание экземпляра класса Application
    application = Application.builder().token(settings.API_KEY).build()
    
    application.add_handler(CommandHandler("start", greet_user))
    application.add_handler(CommandHandler("guess", guess_number))
    application.add_handler(CommandHandler("cat", send_cat_picture))

    application.add_handler(MessageHandler(filters.Regex('^(Вызвать кота)$'), send_cat_picture))
    application.add_handler(MessageHandler(filters.LOCATION, user_coordinates))

    # Добавляет обработчик событий, в данном случае обработчик сообщений, который принимает сообщения, 
    # не являющиеся коммандами и выполняет асинхронную функцию message, в которой возвращаем полученное сообщение
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    # Запускает бота в режиме опроса, 
    # при котором бот периодически опрашивает Telegram-сервер на наличие новых обновлений.
    application.run_polling()

if __name__ == "__main__":
    main()