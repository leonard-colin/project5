class View:
    """Class that defines all interactions between the program and the user"""

    def choose_scenario(self):
        """Method that asks the user to choose a scenario
        and returns his choice"""

        try:
            scenario = input('\n1. Find a better aliment \n'
                             '2. Show my substituted aliments \n'
                             '3. Quit program \n'
                             'Please enter the number for your demand : ')
            print("\n")
            if scenario not in ('1', '2', '3'):
                print("Please enter a valid choice")
                scenario = self.choose_scenario()
            return scenario

        except ValueError:
            print("\nPlease enter a valid choice\n")
            scenario = self.choose_scenario()
            return scenario

    def choose_category(self, categories):
        """Method that asks the user to choose
        one category from the list and returns his choice"""

        try:
            id_list = []
            for id_cat, name_cat in categories:
                id_list.append(id_cat)
                print("{}. {}".format(id_cat, name_cat))

            choice = int(input("\nPlease choose a category number : "))
            print("\n")
            if choice not in id_list:
                print("\nPlease enter a valid choice\n")
                choice = self.choose_category(categories)
            return choice

        except ValueError:
            print("\nPlease enter a valid choice\n")
            choice = self.choose_category(categories)
            return choice

    def choose_aliment(self, category):
        """Method that asks the user to choose an aliment to substitute
        and returns his choice"""

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

    def display_substitute(self, aliment, substitute):
        """Methode that displays a substitute to the user and asks him
        if he'd like to save it or not into database and returns his choice"""

        try:
            s = substitute
            print("\nYou selected {}".format(aliment))
            print("""{} has a better nutriscore with {}.
                    You can see it here : {}
                    You will find it in these stores : {}""".format(
                s[0], s[1], s[2], s[3]))

            choice = input("\nWould you like to save this result ?\n"
                           "Press 1 to save or 2 to ignore : ")
            print("\n")
            if choice not in ('1', '2'):
                print("\nPlease enter a valid choice\n")
                choice = self.display_substitute(aliment, substitute)
            return choice

        except TypeError:
            print("This aliment already have a nutriscore 'A'\n")

    def display_saved_substitute(self, substitute):
        """Method that displays all saved substituted aliments to the user"""

        print("Here are all your substitutes :\n")
        for s in substitute:
            print("{}/  {}\n"
                  "substitute : {}\n".format(s[0], s[1], s[2]))
        print("\n")
