from __future__ import print_function
import requests


class Model:
    """Class that defines all the interactions with the database"""

    def get_categories(self):
        """Method that gets categories from Open Food Facts' API"""
        get_data = requests.get("https://fr.openfoodfacts.org/categories.json")
        categories = []
        data = (get_data.json()['tags'])
        for category in data:
            categories.append(category['name'])
        return categories[:30]

    def get_aliments(self, category):
        """Method that gets aliments from Open Food Facts' API"""
        aliments = dict()
        for cat in category:
            aliments[cat] = []
            ret_aliments = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl?"
                "action=process&tagtype_0=categories"
                "&tag_contains_0=contains&tag_0="
                + str(cat) + "&json=true")
            ret_aliments = ret_aliments.json()
            aliments[cat].append(ret_aliments)
        return aliments

    # --- Code to save data locally into json
    # files to make it faster for development phase ---

    # def refresh_data(self, category):
    #
    #     categories_data = requests.get(
    #     "https://fr.openfoodfacts.org/categories.json"
    #     )
    #     f = open("api_data_files/of_api_cat.json", "w")
    #     f.write(str(categories_data.text))
    #     f.close()
    #
    #     for cat in category:
    #         ret_aliments = requests.get(
    #             "https://fr.openfoodfacts.org/cgi/search.pl?
    #             action=process&tagtype_0=categories&tag_contains_0=contains&tag_0="
    #             + str(cat) + "&json=true")
    #         f = open("api_data_files/of_api_ali" + str(cat) + ".json", "w")
    #         f.write(str(ret_aliments.text))
    #         f.close()
    #
    # def get_categories(self):
    #     """Method that gets categories from Open Food Facts' API"""
    #     categories = []
    #     with open("api_data_files/of_api_cat.json", "r") as file:
    #         file = file.read()
    #
    #     data = json.loads(file)
    #     data = data['tags']
    #     for category in data:
    #         categories.append(category['name'])
    #     return categories[:50]
    #
    # def get_aliments(self, category):
    #     """Method that gets aliments from Open Food Facts' API"""
    #     aliments = dict()
    #     for cat in category:
    #         aliments[cat] = []
    #
    #         with open("api_data_files/of_api_ali"
    #         + str(cat) + ".json") as file:
    #             file = file.read()
    #         ret_aliments = json.loads(file)
    #         aliments[cat].append(ret_aliments)
    #     return aliments
