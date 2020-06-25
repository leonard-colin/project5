import mysql.connector
from mysql.connector import errorcode
import requests


class Model:

    def __init__(self, category):
        self.get_data = requests.get("https://world.openfoodfacts.org/category/" + category + ".json")

        # get_data = requests.get("https://world.openfoodfacts.org/category/" + category + ".json")
        # product = (get_data.json()['products'])

        # result = []
        # for element in product:
        #     if 'product_name' in element:
        #         result.append(element['product_name'])
        #
        # try:
        #     cnx = mysql.connector.connect(user='root',
        #                                   host='localhost',
        #                                   database='openfoodfact')
        # except mysql.connector.Error as err:
        #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        #         print("Something is wrong with your user name or password")
        #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
        #         print("Database does not exist")
        #     else:
        #         print(err)
        # else:
        #     cnx.close()

    def get_products(self, category):
        pass
        # a = requests.get("https://world.openfoodfacts.org/category/" + category + ".json")
        # product = (a.json()['products'])
        # result = []
        # for element in product:
        #     if 'product_name' in element:
        #         result.append(element['product_name'])
        # print(result)
