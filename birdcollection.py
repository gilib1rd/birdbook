from bird import Bird
import requests
import matplotlib.pyplot as plt

class BirdCollection:

    def __init__(self, species_codes_list, name, region_code):
        self.name = name
        self.birds_list = []
        self.region_code = region_code
        payload = {}
        headers = {'X-eBirdApiToken': '7vj7h3qud0ln'}
        if len(species_codes_list) == 0:
            raise ValueError("No birds have been observed in this region.")
        for species_code in species_codes_list:
            response = requests.request("GET", f"https://api.ebird.org/v2/data/obs/{region_code}/recent/{species_code}", headers=headers,
                                        data=payload)
            bird_observation_json = response.json()
            if len(bird_observation_json) != 0:
                new_bird = Bird(bird_observation_json)
                self.birds_list.append(new_bird)
        self.birds_list.sort(key=lambda b: b.observations, reverse=True)

    def __str__(self):
        return f"There are {len(self.birds_list)} {self.name} Birds"

    def get_birds(self):
        """
        :return: a list of Bird objects
        """
        return self.birds_list

    def find_birds_by_name(self, name):
        """
        :return: list of Bird objects that contain the given name
        """
        birds_found = []
        for bird in self.birds_list:
            if name.lower() in str(bird).lower():
                birds_found.append(bird)
        return birds_found

    def get_most_observed_bird(self):
        """
        :return: Bird object that has the most observations
        """
        return self.birds_list[0]

    def find_amount_of_species(self):
        """
        :return: integer amount of species in bird collection
        """
        return len(self.birds_list)

    def plot_birds(self):
        """
        shows a pie chart displaying percentages of birds in a given region
        """
        extra_observations = 0
        if len(self.birds_list) >= 10:
            edited_birds = list(map(lambda b: b.common_name, self.birds_list[0:10]))
            edited_observations = list(map(lambda b: b.observations, self.birds_list[0:10]))
            for bird in self.birds_list[11:]:
                extra_observations += bird.observations
            edited_birds.append("other")
            edited_observations.append(extra_observations)
        else:
            edited_birds = list(map(lambda b: b.common_name, self.birds_list))
            edited_observations = list(map(lambda b: b.observations, self.birds_list))

        _, ax = plt.subplots()
        ax.pie(edited_observations, labels=edited_birds, autopct='%1.1f%%')
        ax.set_title(self.name)
        plt.show()
