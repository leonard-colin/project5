# from database import Database
from model import Model
from constants import PARAMETERS as p


class View:
    """Class that defines all interactions between the program and the user"""

    def __init__(self):
        """Class constructor"""
        
        self.first_screen()
        self.model = Model()
        # self.database = Database()
        self.choose_scenario()
        self.choose_category()


    def first_screen(self):
        """Method that displays a message while to the user while database is being created"""

        user = p['user']
        print("Hello {}, please wait while creating database...\n".format(user))

    def choose_scenario(self):
        """Method that asks the user to choose a scenario and returns its answer"""

        scenario = input('1. Find a better aliment \n'
                         '2. Show my substituted aliments \n'
                         'Please put the number for your demand : ')
        return scenario

    def display_categories(self):
        """Method that displays all categories to the user"""

        cat_list = self.model.display_categories()
        print(cat_list)

    def choose_category(self):
        """Method that asks the user to choose one category from the list and returns its choice"""

        choice = int(input("Please choose the number of the category : "))
        return choice

    def choose_aliment(self, cat_id):
        """Method that asks the user to choose an aliment to substitute and return its choice"""

        ali = self.model.display_aliments(cat_id)
        for (ali_cat, name) in ali:
            print("{}. {}".format(ali_cat, name))
        ali_choice = input("Select an aliment from the list")
        return ali_choice

    # def display_saved_aliments(self):
    #     """Method that asks the"""
    #
    #     choice = input("Do you want to see all your aliments or your aliments by category ?\n"
    #                    "1. All \n"
    #                    "2. Aliments by category\n")
    #     return choice


# if __name__ == '__main__':
#     View()
