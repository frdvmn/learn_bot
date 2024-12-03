import logging

from telegram.ext import Application, MessageHandler, CommandHandler, ConversationHandler, filters, JobQueue
from handlers import (greet_user, guess_number, send_cat_picture, user_coordinates, message, 
                      check_user_photo)

from feedback import feedback_start, feedback_name, feedback_rating, feedback_comment, feedback_skip, feedback_dontknow
from jobs import send_hello
import settings
# Отслеживание ошибок
logging.basicConfig(filename="bot.log", level=logging.INFO)

def main():
    
    # Cоздание экземпляра класса Application
    application = Application.builder().token(settings.API_KEY).build()
    
    # Отправка сообщений с интервалом
    jq = application.job_queue
    jq.run_repeating(send_hello, interval=5, first=0)

    feedback = ConversationHandler(
        entry_points=[
            MessageHandler(filters.Regex('^(Заполнить анкету)$'), feedback_start)
        ], 
        states={
            "name": [
                MessageHandler(filters.TEXT, feedback_name)
            ],
            "rating": [
                MessageHandler(filters.Regex("^(1|2|3|4|5)"), feedback_rating)
            ],
            "comment": [
                CommandHandler('skip', feedback_skip),
                MessageHandler(filters.TEXT, feedback_comment)
            ] 
        }, 
        fallbacks=[
            MessageHandler(filters.TEXT | filters.VIDEO | filters.ATTACHMENT | filters.LOCATION | filters.PHOTO, feedback_dontknow)
        ]
    )
    application.add_handler(feedback)

    application.add_handler(CommandHandler("start", greet_user))
    application.add_handler(CommandHandler("guess", guess_number))
    application.add_handler(CommandHandler("cat", send_cat_picture))

    application.add_handler(MessageHandler(filters.Regex('^(Вызвать кота)$'), send_cat_picture))
    application.add_handler(MessageHandler(filters.LOCATION, user_coordinates))
    application.add_handler(MessageHandler(filters.PHOTO, check_user_photo))

    # Добавляет обработчик событий, в данном случае обработчик сообщений, который принимает сообщения, 
    # не являющиеся коммандами и выполняет асинхронную функцию message, в которой возвращаем полученное сообщение
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    # Запускает бота в режиме опроса, 
    # при котором бот периодически опрашивает Telegram-сервер на наличие новых обновлений.
    application.run_polling()

if __name__ == "__main__":
    main()