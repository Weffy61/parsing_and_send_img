import requests
from pathlib import Path
from os.path import splitext
from urllib.parse import unquote, urlsplit


def get_file_extension(url):
    last_part_of_link = unquote(urlsplit(url).path)
    _, extension = splitext(last_part_of_link)
    return extension


def save_images(urls: list, company, params=None):
    for link_num, link in enumerate(urls):
        image_extension = get_file_extension(link)
        path = f'images/{company}_{link_num}{image_extension}'
        image_path = Path(path).parent
        image_path.mkdir(parents=True, exist_ok=True)
        payload = params
        response = requests.get(link, params=payload)
        response.raise_for_status()
        with open(f'{path}', 'wb') as image:
            image.write(response.content)
