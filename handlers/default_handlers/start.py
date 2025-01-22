from telebot.types import Message
from core.loader import bot

from utils.debug import info


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    info(message.json)
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!")
