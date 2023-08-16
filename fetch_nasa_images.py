import requests
from environs import Env
from load_and_save import fetch_company_images


def get_nasa_image_urls(api_key):
    payload = {
        'api_key': api_key,
        'count': 30
    }
    images_data = requests.get('https://api.nasa.gov/planetary/apod', params=payload).json()
    images_urls = []
    checker_for_image = 'apod.nasa.gov/apod/image/'
    for image_data in images_data:
        if checker_for_image in image_data['url']:
            images_urls.append(image_data['url'])
    return images_urls


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env('NASA_API_KEY')
    nasa_links = get_nasa_image_urls(nasa_api_key)
    fetch_company_images(nasa_links, 'nasa')


if __name__ == '__main__':
    main()
