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

    def get_categories(self, category):
        data = (self.get_data.json()['tag'])
        category = self.category
        for element, cat in data:
            if 'name' in cat:
                category.append(element['name'])
        return category

    def get_aliment(self):
        pass


if __name__ == '__main__':
    Model()
