import requests
from environs import Env
import datetime
from load_and_save import fetch_company_images


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
    nasa_epic_links, nasa_epic_payload = get_nasa_epic_image_urls(nasa_api_key)
    fetch_company_images(nasa_epic_links, 'nasa_epic', nasa_epic_payload)


if __name__ == '__main__':
    main()
