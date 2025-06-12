import unittest
import requests

from bird import Bird

class TestBird(unittest.TestCase):

    def test_print(self):
        payload = {}
        headers = {'X-eBirdApiToken': '7vj7h3qud0ln'}
        response = requests.request("GET", "https://api.ebird.org/v2/data/obs/US-PA/recent/cangoo", headers=headers, data=payload)
        bird_observation_json = response.json()
        #print(bird_observation_json)

        cangoo = Bird(bird_observation_json)
        print(cangoo)