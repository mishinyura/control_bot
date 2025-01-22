import os
from dotenv import load_dotenv, find_dotenv
from utils.debug import get_list_from_file

if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()
TOKEN = os.getenv("TOKEN")
DEFAULT_COMMANDS = (
    ('start', 'Запускает бота'),
    ('help', 'Выводит справку'),
    ('arrest', 'Арестовывает участника'),
)

STOP_WORDS = get_list_from_file('stop_list.txt')