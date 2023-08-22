import argparse
import requests
from load_and_save import save_image


def parse_launch_id():
    parser_launch_id = argparse.ArgumentParser(
        description='Загрузка фото от SpaceX по ID запуска'
    )
    parser_launch_id.add_argument('-l', '--launch_id', help='ID запуска')
    launch_args = parser_launch_id.parse_args()
    return launch_args.launch_id


def get_images_by_launch_id(launch_id):
    request = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    request.raise_for_status()
    images_urls = request.json()['links']['flickr']['original']
    if len(images_urls) == 0:
        print('Извините, по данному запуску нет фото')
    return images_urls


def get_default_images():
    request = requests.get(f'https://api.spacexdata.com/v5/launches/')
    request.raise_for_status()
    images_urls = request.json()[100]['links']['flickr']['original']
    return images_urls


def main():
    launch_id = parse_launch_id()
    if launch_id:
        spacex_links = get_images_by_launch_id(launch_id)
    else:
        spacex_links = get_default_images()
    for link_num, link in enumerate(spacex_links):
        save_image(link, link_num, 'space_x')


if __name__ == '__main__':
    main()
