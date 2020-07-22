from model import Model
import mysql.connector
from constants import PARAMETERS as par


class View:

    def __init__(self):
        self.model = Model()

    def choose_scenario(self):
        scenario = input('1. Which aliment would you like to substitute ? \n'
                         '2. Show my substituted aliments \n'
                         'Please put the number for your demand : ')
        return scenario

    def choose_category(self):
        # self.model.list_categories()
        category = input("Select a category from list")

        return category

