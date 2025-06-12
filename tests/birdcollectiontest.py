import unittest
import requests

from birdcollection import BirdCollection

class TestBirdCollection(unittest.TestCase):

    def test_get_from_api(self):
        payload = {}
        headers = {'X-eBirdApiToken': '7vj7h3qud0ln'}
        region_code = "US-PA"
        response = requests.request("GET", f"https://api.ebird.org/v2/product/spplist/{region_code}", headers=headers,
                                    data=payload)
        species_code_list = response.json()
        print(species_code_list)

        penn_birds = BirdCollection(species_code_list, "Pennsylvania", region_code)
        print(penn_birds)
        for bird in penn_birds.get_birds():
            print(bird)

    def test_get_from_list(self):
        region_code = "US-PA"
        species_code_list = ['bbwduc', 'bahgoo', 'snogoo', 'rosgoo', 'sxrgoo1', 'gragoo', 'swagoo1', 'x00776', 'gwfgoo',
                             'lwfgoo', 'tunbeg1', 'pifgoo', 'brant', 'bargoo', 'cacgoo1']

        penn_birds = BirdCollection(species_code_list, "Pennsylvania", region_code)
        print(penn_birds)
        for bird in penn_birds.get_birds():
            print(bird)

    def test_find_birds_by_name(self):
        region_code = "US-PA"
        species_code_list = ['bbwduc', 'bahgoo', 'snogoo', 'rosgoo', 'sxrgoo1', 'gragoo', 'swagoo1', 'x00776', 'gwfgoo',
                             'lwfgoo', 'tunbeg1', 'pifgoo', 'brant', 'bargoo', 'cacgoo1']

        penn_birds = BirdCollection(species_code_list, "Pennsylvania", region_code)

        self.assertEqual(penn_birds.find_birds_by_name("Anser"), penn_birds.get_birds()[0:4])
        self.assertEqual(penn_birds.find_birds_by_name("Barnacle Goose")[0], penn_birds.get_birds()[5])
        self.assertEqual(penn_birds.find_birds_by_name("Gili"), [])

    def test_get_most_observed_bird(self):
        region_code = "US-PA"
        species_code_list = ['bbwduc', 'bahgoo', 'snogoo', 'rosgoo', 'sxrgoo1', 'gragoo', 'swagoo1', 'x00776', 'gwfgoo',
                             'lwfgoo', 'tunbeg1', 'pifgoo', 'brant', 'bargoo', 'cacgoo1']

        penn_birds = BirdCollection(species_code_list, "Pennsylvania", region_code)

        self.assertEqual(penn_birds.get_most_observed_bird(), penn_birds.get_birds()[0])

    def test_graphing(self):
        region_code = "VA"
        species_code_list = ['mallar3', 'rocpig', 'cowpig1', 'eucdov', 'alpswi1', 'comswi', 'palswi3', 'commoo3', 'bkhgul',
                             'yelgul1', 'lbbgul', 'whisto1', 'graher1', 'hoopoe', 'grswoo', 'leskes1', 'eurkes', 'perfal',
                             'rorpar', 'peflov', 'monpar', 'eurmag1', 'eurjac', 'hoocro1', 'coatit2', 'blutit', 'gretit1',
                             'banswa', 'barswa', 'comhom1', 'comchi1', 'blackc1', 'sarwar1', 'firecr1', 'shttre1', 'winwre4',
                             'eursta', 'eurbla', 'eurrob1', 'blared1', 'burthr', 'itaspa1', 'eutspa', 'grywag', 'whiwag',
                             'comcha', 'eurgre1', 'eurgol', 'eurser1']

        penn_birds = BirdCollection(species_code_list, "Vatican", region_code)

        penn_birds.plot_birds()
