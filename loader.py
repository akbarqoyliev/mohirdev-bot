from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from utils.db_api.postgresql import Database
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
<<<<<<< HEAD
# db = Database()
=======
# db = Database()
>>>>>>> afe66c2e9cef9eaeb7cf9b45f331f4d340848570
