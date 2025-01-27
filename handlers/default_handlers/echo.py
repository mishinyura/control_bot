import re


from telebot.types import Message

from core.config import STOP_WORDS
from core.loader import bot
from utils.api import get_weather

import re


def is_stop_word(text: str) -> bool:
    for word in STOP_WORDS:
        if word in re.findall(word, text):
            return True
    return False


@bot.message_handler(func=lambda message: True)
def handle_message(message: Message):
    mess = message.text.lower()
    print(f"Получено сообщение от {message.from_user.username}: {message.text}")

    if is_stop_word(mess):
        bot.send_message(message.chat.id, 'Нельзя материться')
    elif re.search(r'коп', mess) and re.search(r'погода', mess):
        temperature = get_weather()
        text = f'В Москве сейчас {temperature} ℃'
        bot.send_message(message.chat.id, text)
    elif re.search(r'^пук$', mess):
        bot.send_message(message.chat.id, 'Пик')
    elif re.search(r'^пик$', mess):
        bot.send_message(message.chat.id, 'Пук')

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
# @bot.message_handler(state=None)
# def bot_echo(message: Message):
#     bot.reply_to(
#         message, "Эхо без состояния или фильтра.\n" f"Сообщение: {message.text}"
#     )
