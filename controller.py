import requests
from model import Model
from view import View


class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()
        self.process()

    def process(self):
        self.model.get_data()

        a = self.view.choose_scenario()

        if a == '1':
            self.scenario1()
        elif a == '2':
            self.scenario2()
        else:
            return self.view.choose_scenario()

    def scenario1(self):
        query = ("SELECT category, last_name, hire_date FROM employees "
                 "WHERE hire_date BETWEEN %s AND %s")

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
