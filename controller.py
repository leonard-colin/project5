import requests
from model import Model
from view import View


class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()
        self.process()

    def process(self):
        #self.model.get_data()

        a = self.view.choose_scenario()

        if a == '1':
            self.scenario1()
        elif a == '2':
            self.scenario2()

    def scenario1(self):
        choice = self.view.display_saved_aliments()
        if choice == '1':
            # Show all saved aliments
            pass
        elif choice == '2':
            # Show saved aliments by cat
            pass

        # query = ("SELECT category, last_name, hire_date FROM employees "
        #          "WHERE hire_date BETWEEN %s AND %s")

    def scenario2(self):
        category = self.view.choose_category()

        b = self.model.get_categories(category)

        # c = self.view.print_aliment(b)

        # d = self.model.best_element_by_cat(a, c)

        # e = self.view.save_aliment(d)

        # if e = True
        pass


if __name__ == '__main__':
    Controller()
