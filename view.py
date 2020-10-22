from constants import PARAMETERS as p


class View:
    """Class that defines all interactions between the program and the user"""

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

    # def display_categories(self, categories):
    #     """Method that displays all categories to the user"""
    #
    #     for id_cat, name_cat in categories:
    #         print("{}. {}".format(id_cat, name_cat))

    def choose_category(self, categories):
        """Method that asks the user to choose
        one category from the list and returns its choice"""
        for id_cat, name_cat in categories:
            print("{}. {}".format(id_cat, name_cat))
        # self.display_categories(category)
        cat_id = int(input("Please choose a category number : "))
        return cat_id

    # def print_aliment(self, cat):
    #     ali = self.database.select_aliment(cat)
    #     for (ali_id, name) in ali:
    #         ali_list = "{}. {}".format(ali_id, name)
    #         print(ali_list)

    def choose_aliment(self, category):
        """Method that asks the user to choose an aliment to substitute and return its choice"""
        for (ali_id, name) in category:
            ali_list = "{}. {}".format(ali_id, name)
            print(ali_list)


        choice = input("Select an aliment from the list : \n")
        return choice

    # def display_saved_aliments(self):
    #     """Method that asks the"""
    #
    #     choice = input("Do you want to see all your aliments or your aliments by category ?\n"
    #                    "1. All \n"
    #                    "2. Aliments by category\n")
    #     return choice

# if __name__ == '__main__':
#     View()
