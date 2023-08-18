import requests
from environs import Env
import datetime
from load_and_save import save_images


def get_nasa_epic_image_urls(api_key, images_limit=5):
    payload = api_key
    epic_response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/images', params=payload)
    epic_response.raise_for_status()
    epic_response_converted = epic_response.json()
    images_urls = []
    for image_link in epic_response_converted:
        formatted_date = datetime.datetime.fromisoformat(image_link['date'])
        date = f'{formatted_date.year}/{formatted_date.month:02d}/{formatted_date.day:02d}'
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_link["image"]}.png'
        images_urls.append(image_url)
        images_limit -= 1
        if images_limit == 0:
            break
    return images_urls


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env.str('NASA_API_KEY')
    api_key_payload = {'api_key': nasa_api_key}
    nasa_epic_links = get_nasa_epic_image_urls(api_key_payload)
    save_images(nasa_epic_links, 'nasa_epic', api_key_payload)


if __name__ == '__main__':
    main()
