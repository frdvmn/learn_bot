import logging
from telegram.ext import Application, MessageHandler, filters

import settings
# Отслеживание ошибок
logging.basicConfig(filename="bot.log", level=logging.INFO)

def main():
    # Cоздание экземпляра класса Application
    application = Application.builder().token(settings.API_KEY).build()
    async def message(update, context):
        text = update.message.text
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Вы написали: {text}")
    
    # Добавляет обработчик событий, в данном случае обработчик сообщений, который принимает сообщения, 
    # не являющиеся коммандами и выполняет асинхронную функцию message, в которой возвращаем полученное сообщение
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message))

    # Запускает бота в режиме опроса, 
    # при котором бот периодически опрашивает Telegram-сервер на наличие новых обновлений.
    application.run_polling()

if __name__ == "__main__":
    main()