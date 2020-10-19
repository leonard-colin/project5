from __future__ import print_function
import json
import requests
from database import Database


class Model:
    """Class that defines all the interactions with the database"""

    # def __init__(self):
    #     """Class constructor"""
    #     #self.get_data = requests.get("https://fr.openfoodfacts.org/categories.json")
    #     # self.database = Database()

    def refresh_data(self, category):

        categories_data = requests.get("https://fr.openfoodfacts.org/categories.json")
        f = open("api_data_files/of_api_cat.json", "w")
        f.write(str(categories_data.text))
        f.close()

        for cat in category:
            ret_aliments = requests.get(
                "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0="
                + str(cat) + "&json=true")
            f = open("api_data_files/of_api_ali" + str(cat) + ".json", "w")
            f.write(str(ret_aliments.text))
            f.close()

    def get_categories(self):
        """Method that gets categories from Open Food Facts' API"""
        categories = []
        with open("api_data_files/of_api_cat.json", "r") as file:
            file = file.read()

        data = json.loads(file)
        data = data['tags']
        for category in data:
            categories.append(category['name'])
        return categories[:50]

    def get_aliments(self, category):
        """Method that gets aliments from Open Food Facts' API"""
        aliments = dict()
        for cat in category:
            aliments[cat] = []

            with open("api_data_files/of_api_ali" + str(cat) + ".json") as file:
                file = file.read()
            ret_aliments = json.loads(file)
            aliments[cat].append(ret_aliments)
        return aliments

# from __future__ import print_function
# import requests
# from database import Database
#
#
# class Model:
#     """Class that defines all the interactions with the database"""
#
#     def __init__(self):
#         """Class constructor"""
#         self.get_data = requests.get("https://fr.openfoodfacts.org/categories.json")
#         self.get_aliments()
#         self.database = Database()
#
#     def get_categories(self):
#         """Method that gets categories from Open Food Facts' API"""
#         categories = (self.get_data.json()['tags'])
#         return categories
#
#     def get_aliments(self):
#         """Method that gets aliments from Open Food Facts' API"""
#         category = self.get_categories()
#         aliments = []
#         for cat in category:
#             ret_aliments = requests.get(
#                 "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0="
#                 + str(cat) + "&json=true")
#             aliments.append(ret_aliments.json())
#         return aliments
#
#
#
#     # def add_aliments(self):
#     #     aliments = self.data_aliment()
#     #     for element in aliments['products']:
#     #         if not all(tag in element for tag in ("generic_name_fr", "nutriscore_grade", "url", "stores")):
#     #             pass
#     #         else:
#     #             if element['generic_name_fr'] != '':
#     #                 data = [element['code'], element['generic_name_fr'], element['nutriscore_grade'], element['url'],
#     #                         element['stores']]
#     #                 aliments.append(data)
#     #
#     # def display_categories(self):
#     #     cat = self.database.get_categories()
#     #     for (id, name) in cat:
#     #         return "{}. {}".format(id, name)
#
# # if __name__ == '__main__':
# #     Model()
