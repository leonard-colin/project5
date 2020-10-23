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
        # try:
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
        try:
            for id_cat, name_cat in categories:
                print("{}. {}".format(id_cat, name_cat))
            cat_id = int(input("\nPlease choose a category number : "))
            print("\n")
            return cat_id
        except ValueError:
            print("\nPlease enter a valid choice\n")
            cat_id = self.choose_category(categories)
            return cat_id

    def choose_aliment(self, category):
        """Method that asks the user to choose an aliment to substitute and return its choice"""
        try:
            id_list = []
            for ali_id, name in category:
                id_list.append(ali_id)
                ali_list = "{}. {}".format(ali_id, name)
                print(ali_list)
            choice = int(input("\nSelect an aliment number from the list : "))
            if choice not in id_list:
                print("\nPlease enter a valid choice\n")
                choice = self.choose_aliment(category)
            return choice
        except ValueError:
            print("\nPlease enter a valid choice\n")
            choice = self.choose_aliment(category)
            return choice

    def print_substitute(self, aliment, substitute):
        """Methode that..."""

        try:
            s = substitute
            print("\nYou selected {}".format(aliment))
            print("""{} has a better nutriscore with {}.
                    You can see it here : {}
                    You will find it in these stores : {}""".format(
                s[0], s[1], s[2], s[3]))
            choice = input("Would you like to save this result ?\n"
                           "Press 1 to save or 2 to ignore : ")
            return choice
        except TypeError:
            print("This aliment already have a nutriscore 'A'\n"
                  "You can choose another aliment")
            choice = self.print_substitute(aliment, substitute)
            return choice

    # def save_substitute(self):
    #     choice = input("Would you like to save this result ?\n"
    #                    "Press 1 to save or 2 to ignore")
