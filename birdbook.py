import requests
from birdcollection import BirdCollection

api_endpoint = 'https://en.wikipedia.org/w/api.php'

#gets image file name
response = requests.get(api_endpoint, {
	"action": "query",
	"format": "json",
	"prop": "images",
	"titles": "rock pigeon",
	"redirects": 1,
	"formatversion": "2",
	"imlimit": "1"
}).json()

image_file = response['query']['pages'][0]['images'][0]['title']
print(image_file)

#gets image URL from wikipedia
response = requests.get(api_endpoint, {
	"action": "query",
	"format": "json",
	"prop": "imageinfo",
	"titles": "File:Columba livia - 01.jpg",
	"redirects": 1,
	"formatversion": "2",
	"iiprop": "url"
}).json()

image_url = response['query']['pages'][0]['imageinfo'][0]['url']
print(image_url)