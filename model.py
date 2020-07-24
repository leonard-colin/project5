from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
import requests
from constants import PARAMETERS as par, DB_NAME


class Model:

    # cnx = mysql.connector.connect(user=par['user'], password=par['password'], database=par['database'])
    # cursor = cnx.cursor()
    # db_name = "OpenFoodFacts"

    def __init__(self):
        self.get_data = requests.get("https://fr.openfoodfacts.org/categories.json")
        self.category = []
        self.aliment = []
        self.get_categories()

    def get_categories(self):
        data = (self.get_data.json()['tags'])
        category = self.category
        for element, cat in enumerate(data):
            if 'name' in cat:
                category.append([cat['name']])
        return category
        #return [[el] for el in category]




    def get_aliment(self):
        pass
        # category = self.get_categories()
        # get_aliments = requests.get(
        #     "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" +
        #     category['name'] + "&sort_by=unique_scans_n&page_size=1000&axis_x=energy&axis_y=products_n&action=display&json=1")
        # for element, ali in enumerate(category):
        #     if 'name' in ali:
        #         self.aliment.append(ali['name'])
        # return self.aliment


if __name__ == '__main__':
    Model()
