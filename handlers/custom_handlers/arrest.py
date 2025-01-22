from telebot.types import Message

from core.loader import bot


@bot.message_handler(commands=["arrest"])
def bot_arrest(message: Message):
    bot.reply_to(message, 'Юля арестована циганской властью')
