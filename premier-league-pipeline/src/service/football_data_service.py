
import requests
import os

from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('FOOTBALL_DATA_KEY')
BASE_URL = 'https://api.football-data.org/v4'


class FootballDataService:
    def __init__(self):
        pass

    def get_matches(self, season):

        headers = {'X-Auth-Token': API_KEY}
        url = f'{BASE_URL}/competitions/PL/matches?season={season}&status=FINISHED'
        response = requests.get(url, headers=headers)
        data = response.json()
        return data['matches']
