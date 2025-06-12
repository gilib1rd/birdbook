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

    def __str__(self):
        return f'{self.common_name} ({self.scientific_name}) has {self.observations} observations.'

    def get_species_code(self):
        return self.species_code