from datetime import timedelta

# Chat id временно единственный, пока нет DB
async def send_hello(context):
    interval = timedelta(seconds=5)
    await context.bot.send_message(chat_id=670283527, text=f"ПРИВЕТ, Я ДРУГ!{context.job.trigger.interval}") 
    context.job.trigger.interval += interval
    if(context.job.trigger.interval > timedelta(seconds=10)):
        await context.bot.send_message(chat_id=670283527, text=f"пока(") 
        context.job.enabled = False  # Временно отключить отправку
        context.job.schedule_removal()  # Полностью отключить отправку