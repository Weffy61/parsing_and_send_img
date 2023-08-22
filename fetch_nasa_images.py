import requests
from environs import Env
from load_and_save import save_image


def get_nasa_image_urls(api_key, image_limit):
    payload = {
        'api_key': api_key,
        'count': image_limit
    }
    apod_response_converted = requests.get('https://api.nasa.gov/planetary/apod', params=payload).json()
    images_urls = []
    checker_for_image = 'apod.nasa.gov/apod/image/'
    for image_link in apod_response_converted:
        if checker_for_image in image_link['url']:
            images_urls.append(image_link['url'])
    return images_urls


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env.str('NASA_API_KEY')
    image_limit = 30
    nasa_links = get_nasa_image_urls(nasa_api_key, image_limit)
    for link_num, link in enumerate(nasa_links):
        save_image(link, link_num, 'nasa_apod')


if __name__ == '__main__':
    main()
