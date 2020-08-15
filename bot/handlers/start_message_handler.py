from pyrogram import Client, Message
from bot import COMMAND, LOCAL, CONFIG
from bot.handlers import help_message_handler

async def func(client : Client, message: Message):
    try:
        await message.delete()
    except:
        pass
    await message.reply_text(LOCAL.WELCOME_MESSAGE.format(cmd_pass = COMMAND.PASSWORD))
    if not int(CONFIG.BOT_PRIVATE):
        await help_message_handler.func(client, message)