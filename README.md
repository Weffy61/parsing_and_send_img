# Парсинг картинок космоса и постинг их в телеграм
Несколько скриптов для получения фото с запуска SpaceX и различных фото NASA. Также возможна отправка полученных
изображений в телеграм-канал с заданным временным интервалом
## Установка
```commandline
git clone https://github.com/Weffy61/parsing_and_send_img
```
## Установка зависимостей
Переход в директорию с исполняемым файлом и установка
```commandline
cd parsing_and_send_img
```
```commandline
pip install -r requirements.txt
```
## Создание и настройка .env
Для полноценной работы вам необходимо получить:  
- NASA API Key - для получения перейдите по [адресу](https://api.nasa.gov/) и зарегистрируйтесь. Ключ придет на 
указанную почту  
- Telegram Bot Token - необходимо создать Telegram бота в `@BotFather` и получить необходимый токен
- Telegram Chat ID - создайте группу или используйте существующую. Перешлите сообщение опубликованное от имени группы 
в бота `@getmyid_bot`. В ответном сообщении `Forwarded from chat` является вашим ChatID. 
[Подробнее](https://lumpics.ru/how-find-out-chat-id-in-telegram/)  
    
Создайте в корне папки `parsing_and_send_img` файл `.env`. Откройте его для редактирования любым текстовым 
редактором.  
```djangourlpath
export NASA_API_KEY=вставить NASA API Key
export TELEGRAM_API_TOKEN=вставить Telegram Bot Token
export TELEGRAM_GROUP_ID=вставить Telegram Chat ID
```
Также можно добавить
```djangourlpath
export TIME=интервал отправки сообщений в часах
```
Значение `TIME` по умолчанию 4 часа
## Получение фото SpaceX
### Запуск
```commandline
python fetch_spacex_images.py -l launch_id
```
`launch_id` - id конкретного запуска  
Если у запуска нет фото получите сообщение "`Извините, по данному запуску нет фото`"  
Получение фото с последнего запуска:
```commandline
python fetch_spacex_images.py
```
#### Помощь
```commandline
python fetch_spacex_images.py --help
```
## Получение фотографий дня от NASA
Получите около 30 изображений астрономический картин дня
### Запуск
```commandline
python fetch_nasa_images.py
```
## Получение фото Земли от NASA
Получите 5 изображений земли с разного ракурса
### Запуск
```commandline
python fetch_nasa_epic_images.py
```
## Отправка фото в Telegram канал
Отправите полученные изображения в Telegram канал с заданным интервалом. После отправки всех фото из папки `images` 
фото продолжат отправляться в рандомном порядке
### Запуск
```commandline
python bot.py -i interval
```
`interval` - интервал отправки сообщений в часах.  
Отправка фото с дефолтным интервалом
```commandline
python bot.py
```
#### Помощь
```commandline
python bot.py --help
```
## Отправка конкретного фото в Telegram канал
Отправите указанное изображение в телеграм канал. Если аргумент не указан отправится случайное фото из папки `images`
### Запуск
```commandline
python send_image -i image_name
```
#### Помощь
```commandline
python send_image.py --help
```