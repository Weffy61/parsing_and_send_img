import telegram
from environs import Env


env = Env()
env.read_env()
bot = telegram.Bot(token=env('TELEGRAM_API_TOKEN'))


with open('images/nasa_epic/nasa_epic_0.png', 'rb') as image:
    bot.send_photo(chat_id='-1001471388120', photo=image)
