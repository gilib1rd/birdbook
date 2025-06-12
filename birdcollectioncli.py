from birdcollection import BirdCollection
import requests

def birdcollection_cli(birdcollection):
    print("Success! Enter a number to use this bird collection.")
    while True:
        print("\nCurrent Collection:", birdcollection.name)
        choice = input("1: See all birds in collection\n2: Search for bird by name/keyword\n"
                           "3: Find most observed bird in collection\n4: Find amount of species in collection\n"
                            "5: See pie chart of birds (not recommended for large collections)\n6: Filter (creates a new collection of birds with observations above a given threshold)"
                            "\n0: Exit / Go Back\n")
        if choice == "1":
            for bird in birdcollection.get_birds():
                print(bird)
        elif choice == "2":
            get_birds_by_name(birdcollection)
        elif choice == "3":
            print(f"Most observed bird in {birdcollection.region_code}: {birdcollection.get_most_observed_bird()}")
        elif choice == "4":
            print(f"{birdcollection.find_amount_of_species()} birds are in this collection.")
        elif choice == "5":
            birdcollection.plot_birds()
        elif choice == "6":
            filter_birds(birdcollection, birdcollection.region_code)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def get_birds_by_name(birdcollection):
    # in its own function because it returns a list, allows for future expansion on messing with Bird object
    name = input("Enter a name/keyword to search: ")
    birds_found = birdcollection.find_birds_by_name(name)
    if len(birds_found) == 0:
        print(f"No birds were found containing '{name}'.")
    else:
        for i in range(len(birds_found)):
            print(f"{i}: {str(birds_found[i])}")

def filter_birds(birdcollection, region_code):
    """
    :return: a new BirdCollection based on given BirdCollection but only containing Birds with observations above a given threshold
    """
    upper_limit = birdcollection.get_most_observed_bird().observations
    while True:
        threshold = input(f"What threshold to use for filtering? (between 1-{upper_limit}, or c for cancel): ")
        if threshold == "c" or threshold == "C":
            break
        try:
            threshold = int(threshold)
            if 0 < threshold < upper_limit:
                filtered_birds_list = list(filter(lambda b: b.observations > threshold, birdcollection.get_birds()))
                filtered_species_code_list = []
                print("Filtering...")
                for bird in filtered_birds_list:
                    filtered_species_code_list.append(bird.species_code)
                filtered_birds = BirdCollection(filtered_species_code_list, f"Birds with more than {threshold} observations in {region_code}", region_code)
                birdcollection_cli(filtered_birds)
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid threshold. Please try again.")



def main():
    region_code = input("Welcome! Enter a region code to look at birds observed in that region: ")
    print("Searching for birds... (takes a while)")

    payload = {}
    headers = {'X-eBirdApiToken': '7vj7h3qud0ln'}
    response = requests.request("GET", f"https://api.ebird.org/v2/product/spplist/{region_code}", headers=headers,
                                data=payload)
    species_code_list = response.json()

    try:
        birdcollection = BirdCollection(species_code_list, str(region_code), region_code)
        birdcollection_cli(birdcollection)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()