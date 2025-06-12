import requests
from flask import Flask, request
import random

from birdcollection import BirdCollection

app = Flask(__name__)

website = """
        <h1>Birdbook</h1>
        """
@app.route("/")
def get_location_page():

    get_location_form = """
        <form action="/getlocation" method="post">
             <input type='text' name='location'>
             <input type='submit' value='Get Location'>
        </form>
    """
    return website + get_location_form

@app.route("/getlocation", methods=["POST"])
def run_birdbook():
    region_code = request.form.get("location", "")

    payload = {}
    headers = {'X-eBirdApiToken': '7vj7h3qud0ln'}
    response = requests.request("GET", f"https://api.ebird.org/v2/product/spplist/{region_code}", headers=headers,
                                    data=payload)
    species_code_list = response.json()

    try:
        birds_to_rate = BirdCollection(species_code_list, str(region_code), region_code)
    except ValueError as e:
        print(e)

    bird1 = random.choice(birds_to_rate.get_birds())
    bird2 = random.choice(birds_to_rate.get_birds())
    return f"""
    {website}
    <img src= {bird1.get_image_url()}>
    <img src= {bird2.get_image_url()}>
    """

if __name__ == "__main__":
    app.run(host="localhost", debug=True)