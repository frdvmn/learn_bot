from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup
from utils import main_keyboard
from telegram.ext import ConversationHandler
from telegram.constants import ParseMode

async def feedback_start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f"Привет, как тебя зовут ?", 
        reply_markup=ReplyKeyboardRemove()
    )
    return "name"

async def feedback_name(update, context):
    user_name = update.message.text
    if(len(user_name.split()) < 2):
       await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Введите имя и фамилию")
       return "name"
    else:
       context.user_data["feedback"] = {"name": user_name}
       reply_keyboard = [
           ["1", "2", "3"],
           ["4", "5"]
        ]
       await context.bot.send_message(
           chat_id=update.effective_chat.id, 
           text=f"Оцените сервис от 1 до 5", 
           reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)
        )
       return "rating"

async def feedback_rating(update, context):
    context.user_data["feedback"]["rating"] = int(update.message.text)
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=f"Напишите комментарий или нажмите /skip, чтобы пропустить", 
        reply_markup=ReplyKeyboardRemove())
    return "comment"

async def feedback_skip(update, context):
    user_text = f"""<b>Имя Фамилия</b>: {context.user_data["feedback"]["name"]}
<b>Оценка</b>: {context.user_data["feedback"]["rating"]}
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=user_text, 
        parse_mode=ParseMode.HTML,
        reply_markup=main_keyboard()
    )
    return ConversationHandler.END

async def feedback_comment(update, context):
    context.user_data["feedback"]["comment"] = update.message.text
    user_text = f"""<b>Имя Фамилия</b>: {context.user_data["feedback"]["name"]}
<b>Оценка</b>: {context.user_data["feedback"]["rating"]}
<b>Комментарий</b>: {context.user_data["feedback"]["comment"]}
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=user_text, 
        parse_mode=ParseMode.HTML,
        reply_markup=main_keyboard()
    )
    return ConversationHandler.END

async def feedback_dontknow(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Я вас не понимаю") 