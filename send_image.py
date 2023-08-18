import argparse
from bot import send_image_to_tlg, get_all_images
import random
from environs import Env


def parse_image(all_images):
    image_parser = argparse.ArgumentParser(
        description='Отправка указанного изображения'
    )
    random_image = random.choice(all_images)
    image_parser.add_argument('-i', '--image', help='Имя изображения', default=random_image)
    image_args = image_parser.parse_args()
    return image_args.image


def main():
    env = Env()
    env.read_env()
    tlg_api = env.str('TELEGRAM_API_TOKEN')
    group_id = env.str('TELEGRAM_GROUP_ID')
    image = parse_image(get_all_images())
    send_image_to_tlg(image, tlg_api, group_id)


if __name__ == '__main__':
    main()
