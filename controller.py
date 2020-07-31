from model import Model
from view import View
from database import Database


class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()
        self.database = Database()

    def pre_data(self):
        self.database.insert_categories()
        self.database.insert_aliments()

    def process(self):
        # self.model.get_data()

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

    def scenario2(self):

        category = self.view.choose_category()

        aliment = self.view.choose_aliment(category)

        c = self.view.print_aliment(aliment)

        # d = self.model.best_element_by_cat(a, c)

        # e = self.view.save_aliment(d)

        # if e = True
        pass


if __name__ == '__main__':
    Controller()
