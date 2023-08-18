import time
import telegram
from environs import Env
import os
import random
import argparse


def get_time(interval):
    time_parser = argparse.ArgumentParser(
        description='Отправка изображений космоса с указаным интервалом в часах'
    )
    time_parser.add_argument('-i', '--interval', help='Интервал', default=interval, type=float)
    time_args = time_parser.parse_args()
    return time_args.interval


def send_image_to_tlg(img_name, api_token, group_id):
    bot = telegram.Bot(token=api_token)
    with open(f'images/{img_name}', 'rb') as image:
        bot.send_photo(chat_id=group_id, photo=image)


def get_all_images():
    directory = os.walk('images/')
    all_images = []

    for folder in directory:
        path, _, images = folder
        for image in images:
            all_images.append(image)
    return all_images


def send_images_to_tlg(images: list, timer, api_token, group_id):
    time_interval = timer * 3600
    counter = 0
    while True:
        if counter > len(images) - 1:
            random.shuffle(images)
            counter = 0
        image = images[counter]
        send_image_to_tlg(image, api_token, group_id)
        counter += 1
        time.sleep(time_interval)


def main():
    env = Env()
    env.read_env()
    tlg_api = env.str('TELEGRAM_API_TOKEN')
    interval = env.float('TELEGRAM_MESSAGE_INTERVAL', 4)
    group_id = env.str('TELEGRAM_GROUP_ID')
    time_interval = get_time(interval)
    images = get_all_images()
    send_images_to_tlg(images, time_interval, tlg_api, group_id)


if __name__ == '__main__':
    main()


