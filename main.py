import requests
from pathlib import Path
from os.path import splitext
from urllib.parse import unquote, urlsplit
import datetime
from environs import Env


def save_image(image_url, path, params=None):
    image_path = Path(path).parent
    image_path.mkdir(parents=True, exist_ok=True)
    payload = params
    response = requests.get(image_url, params=payload)
    response.raise_for_status()
    with open(f'{path}', 'wb') as image:
        image.write(response.content)


def get_file_extension(url):
    last_part_of_link = unquote(urlsplit(url).path)
    _, extension = splitext(last_part_of_link)
    return extension


def get_spacex_image_urls():
    request = requests.get('https://api.spacexdata.com/v5/launches/')
    images_urls = request.json()[100]['links']['flickr']['original']
    return images_urls


def fetch_company(urls: list, company, params=None):
    for link_num, link in enumerate(urls):
        image_extension = get_file_extension(link)
        save_image(link, f'images/{company}/{company}_{link_num}{image_extension}', params)


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


def get_nasa_epic_image_urls(api_key, images_limit=5):
    payload = {
        'api_key': api_key
    }
    images_data = requests.get(f'https://api.nasa.gov/EPIC/api/natural/images', params=payload)
    images_data.raise_for_status()
    images_data_json = images_data.json()
    images_urls = []
    for image_data in images_data_json:
        formatted_date = datetime.datetime.fromisoformat(image_data['date'])
        date = f'{formatted_date.year}/{formatted_date.month:02d}/{formatted_date.day:02d}'
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_data["image"]}.png'
        images_urls.append(image_url)
        images_limit -= 1

        if images_limit == 0:
            break
    return images_urls, payload


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env.str('NASA_API_KEY')
    get_spacex_links = get_spacex_image_urls()
    fetch_company(get_spacex_links, 'space_x')
    get_nasa_links = get_nasa_image_urls(nasa_api_key)
    fetch_company(get_nasa_links, 'nasa')
    get_nasa_epic_links, nasa_epic_payload = get_nasa_epic_image_urls(nasa_api_key)
    fetch_company(get_nasa_epic_links, 'nasa_epic', nasa_epic_payload)


if __name__ == '__main__':
    main()
