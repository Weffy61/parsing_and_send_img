import argparse
from bot import send_image_to_tlg, get_all_images
import random
from environs import Env


def post_image(all_images):
    image_parser = argparse.ArgumentParser(
        description='Отправка указанного изображения'
    )
    image_parser.add_argument('-i', '--image', help='Имя изображения')
    image_args = image_parser.parse_args()
    if image_args.image:
        return image_args.image
    return random.choice(all_images)


def main():
    env = Env()
    env.read_env()
    tlg_api = env.str('TELEGRAM_API_TOKEN')
    group_id = env.str('TELEGRAM_GROUP_ID')
    image = post_image(get_all_images())
    send_image_to_tlg(image, tlg_api, group_id)


if __name__ == '__main__':
    main()
