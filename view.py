from model import Model
from database import Database


class View:

    def __init__(self):
        self.model = Model()
        self.database = Database()

    def choose_scenario(self):
        scenario = input('1. Find a better aliment \n'
                         '2. Show my substituted aliments \n'
                         'Please put the number for your demand : ')
        print(scenario)
        if scenario != '1' and scenario != '2':
            return self.choose_scenario()
        return scenario

    def display_saved_aliments(self):
        choice = input("Do you want to see all your aliments or your aliments by category ?\n"
                       "1. All \n"
                       "2. Aliments by category\n")
        if choice != '1' and choice != '2':
            return self.display_saved_aliments()
        return choice

    def choose_category(self):
        cat = self.database.display_categories()
        for (id_cat, name) in cat:
            print("{}. {}".format(id_cat, name))
        cat_choice = input("Select a category number from the list")
        return cat_choice

    def choose_aliment(self, cat_id):
        ali = self.database.display_aliment(cat_id)
        for (ali_cat, name) in ali:
            print("{}. {}".format(ali_cat, name))
        ali_choice = input("Select an aliment from the list")
        return ali_choice
