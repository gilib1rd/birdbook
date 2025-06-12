import requests
class Bird:

    def __init__(self, bird_info_json):
        self.species_code = bird_info_json[0]['speciesCode']
        self.common_name = bird_info_json[0]['comName']
        self.scientific_name = bird_info_json[0]['sciName']
        observations = 0
        for i in range(len(bird_info_json)):
            if 'howMany' not in bird_info_json[i]:
                observations += 1
            else:
                observations += bird_info_json[i]['howMany']
        self.observations = observations

        try:
            api_endpoint = 'https://en.wikipedia.org/w/api.php'
            # gets image file name
            response = requests.get(api_endpoint, {
                "action": "query",
                "format": "json",
                "prop": "images",
                "titles": self.common_name,
                "redirects": 1,
                "formatversion": "2",
                "imlimit": "5"
            }).json()

            image_to_use = ""
            for image in response['query']['pages'][0]['images']:
                if "Commons-logo" not in image['title'] and "flag" not in image['title']:
                    image_to_use = image['title']
                    break

            # gets image URL from wikipedia
            response = requests.get(api_endpoint, {
                "action": "query",
                "format": "json",
                "prop": "imageinfo",
                "titles": str(image_to_use),
                "redirects": 1,
                "formatversion": "2",
                "iiprop": "url"
            }).json()

            self.image_url = response['query']['pages'][0]['imageinfo'][0]['url']
        except KeyError as e:
            self.image_url = "No image available"

    def __str__(self):
        return f'{self.common_name} ({self.scientific_name}) has {self.observations} observations.\n{self.image_url}'

    def get_species_code(self):
        return self.species_code

    def get_image_url(self):
        return self.image_url