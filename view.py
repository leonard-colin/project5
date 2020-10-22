from constants import PARAMETERS as p


class View:
    """Class that defines all interactions between the program and the user"""

    def first_screen(self):
        """Method that displays a message while to the user while database is being created"""

        user = p['user']
        print("Hello {}, please wait while creating database...\n".format(user))

    def choose_scenario(self):
        """Method that asks the user to choose a scenario and returns its answer"""
        # try catch ICI
        #try:
        scenario = input('1. Find a better aliment \n'
                         '2. Show my substituted aliments \n'
                         'Please enter the number for your demand : ')
        print("\n")
        if scenario not in ('1', '2'):
            print("Please enter a valid choice")
            scenario = self.choose_scenario()
        return scenario

        # except (ValueError, TypeError):
        #     print("Please enter a valid choice")
        #     self.choose_scenario()

    def choose_category(self, categories):
        """Method that asks the user to choose
        one category from the list and returns its choice"""
        for id_cat, name_cat in categories:
            print("{}. {}".format(id_cat, name_cat))
        cat_id = int(input("\nPlease choose a category number : "))
        print("\n")
        return cat_id

    def choose_aliment(self, category):
        """Method that asks the user to choose an aliment to substitute and return its choice"""

        for (ali_id, name) in category:
            ali_list = "{}. {}".format(ali_id, name)
            print(ali_list)
        choice = input("\nSelect an aliment number from the list : ")
        return choice

    def print_substitute(self, aliment, substitute):
        """Methode that..."""

        print("You selected {}".format(aliment))
        print("""{} has a better nutriscore with {}.
                You can see it here : {}
                You will find it in these stores : {}""".format(
            substitute[0], substitute[1], substitute[2], substitute[3]))

    # def display_saved_aliments(self):
    #     """Method that asks the"""
    #
    #     choice = input("Do you want to see all your aliments or your aliments by category ?\n"
    #                    "1. All \n"
    #                    "2. Aliments by category\n")
    #     return choice

# if __name__ == '__main__':
#     View()
