import logging
from random import randint
from telegram.ext import Application, MessageHandler, CommandHandler, filters

import settings
# Отслеживание ошибок
logging.basicConfig(filename="bot.log", level=logging.INFO)

def main():
    # Cоздание экземпляра класса Application
    application = Application.builder().token(settings.API_KEY).build()
    async def message(update, context):
        text = update.message.text
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Вы написали: {text}")
    
    async def greet_user(update, context):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Добро пожаловать.")
    
    def play_random_numbers(user_number):
        bot_number = randint(user_number - 10, user_number + 10)
        if user_number > bot_number:
            message = f"Ваше число {user_number}, мое {bot_number}, вы выиграли" 
        elif user_number == bot_number:
            message = f"Ваше число {user_number}, мое {bot_number}, ничья"
        else:
            message = f"Ваше число {user_number}, мое {bot_number}, вы проиграли"
        return message

    async def guess_number(update, context):
        print(context.args)
        if context.args:
            try:
                user_number = int(context.args[0])
                message = play_random_numbers(user_number)
            except (ValueError, TypeError):
                message = "Введите целое число"
        else:
            message = "Введите число"
        await context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    
    application.add_handler(CommandHandler("start", greet_user))
    application.add_handler(CommandHandler("guess", guess_number))

    # Добавляет обработчик событий, в данном случае обработчик сообщений, который принимает сообщения, 
    # не являющиеся коммандами и выполняет асинхронную функцию message, в которой возвращаем полученное сообщение
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    # Запускает бота в режиме опроса, 
    # при котором бот периодически опрашивает Telegram-сервер на наличие новых обновлений.
    application.run_polling()

if __name__ == "__main__":
    main()