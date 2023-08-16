import telegram
from environs import Env

env = Env()
env.read_env()

bot = telegram.Bot(token=env('TELEGRAM_API_TOKEN'))
bot.send_message(text='Hello!', chat_id='-1001471388120')
