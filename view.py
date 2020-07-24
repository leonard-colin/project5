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
        if scenario != '1' or scenario != '2':
            self.choose_scenario()
        return scenario

    def display_saved_aliments(self):
        choice = input("Do you want to see all your aliments or your aliments by category ?\n"
                       "1. All \n"
                       "2. Aliments by category\n")
        if choice != '1' or choice != '2':
            self.display_saved_aliments()
        return choice
        
    def choose_category(self):
        # self.model.list_categories()
        category = input("Select a category from list")

        return category

