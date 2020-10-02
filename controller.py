from model import Model
from view import View


class Controller:
    """Class that defines the interactions between the View, Model and Database"""

    def __init__(self):
        """Class constructor"""

        self.view = View()
        self.model = Model()

    # def pre_data(self):
    #     self.database.insert_categories()
    #     self.database.insert_aliments()

    def process(self):
        """Method that sets all the program's process"""

        # self.model.get_data()
        self.choose_scenario()


    #Logique à mettre direct dans le process sans faire la méthode ?
    def choose_scenario(self):
        """Method that asks"""

        scenario = self.view.choose_scenario()
        if scenario not in ('1', '2'):
            self.view.choose_scenario()
        elif scenario == '1':
            self.get_substitute()
        elif scenario == '2':
            self.get_saved_aliments()

    def categories_list(self):
        """Method that return a list of categories from the API"""

        data = self.model.get_categories()
        category = []
        for element, cat in enumerate(data):
            if 'name' in cat:
                category.append([cat['name']])
        return category[:50]

    def aliments_list(self):
        """Method that adds all aliments from all categories in a list"""

        aliments = self.model.get_aliments()
        for element in aliments['products']:
            if not all(tag in element for tag in ("generic_name_fr", "nutriscore_grade", "url", "stores")):
                pass
            else:
                if element['generic_name_fr'] != '':
                    data = [element['code'], element['generic_name_fr'], element['nutriscore_grade'], element['url'],
                            element['stores']]
                    aliments.append(data)
                    # self.database.insert_associated(cat, element['code'])

    def display_categories(self):
        """Method that returns..."""

        cat_list = self.model.display_categories()
        return cat_list

    def choose_category(self):
        """Method that set conditions for a category selection by the user"""
        categories = self.model.display_categories()
        cat_number = range(1, 51)
        if categories != cat_number or categories != int:
            self.choose_category()

    def choose_aliment(self, cat):
        """Method that..."""
        ali = self.database.display_categories(cat_id)

    def get_saved_aliments(self):
        """Method that..."""

        choice = self.view.display_saved_aliments()
        if choice == '1':
            # Show all saved aliments
            pass
        elif choice == '2':
            # Show saved aliments by cat
            pass

    def get_substitute(self):
        """Method that gets a substitue aliment with a better nutriscore"""
        self.view.choose_category()

        # category = self.view.choose_category()

        # aliment = self.view.choose_aliment(category)

        # c = self.view.print_aliment(aliment)

        # d = self.model.best_element_by_cat(a, c)

        # e = self.view.save_aliment(d)

        # if e = True

# if __name__ == '__main__':
#     Controller()
