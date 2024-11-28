from glob import glob
from random import choice
from utils import play_random_numbers, get_emoji, main_keyboard

async def greet_user(update, context):
    context.user_data['emoji'] = get_emoji(context.user_data)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Добро пожаловать. {context.user_data['emoji']}", reply_markup=main_keyboard())

async def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (ValueError, TypeError):
            message = "Введите целое число"
    else:
        message = "Введите число"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(cat_pic_filename, 'rb'))

async def user_coordinates(update, context):
    context.user_data['emoji'] = get_emoji(context.user_data)
    coords = update.message.location
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{context.user_data['emoji']}Ваши координаты: \nШирина - {coords.latitude} \nДолгота - {coords.longitude}", reply_markup=main_keyboard())

async def message(update, context):
    text = update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Вы написали: {text}", reply_markup=main_keyboard())
