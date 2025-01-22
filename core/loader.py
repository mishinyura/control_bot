from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from core import config

storage = StateMemoryStorage()
bot = TeleBot(token=config.TOKEN, state_storage=storage)
