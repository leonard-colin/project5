import requests
from view import View
from model import Model


class Controller:

    def __init__(self):
        self.view = View()
        self.model = Model()

    def process(self):
        # self.get_data()
        choice = self.view.choose_scenario()

        # if choice == '1':
        #     self.view.scenario1()
        # elif choice == '2':
        #     self.view.scenario2()

        # a = self.view.get_categorie()

        # b = self.model.get_categorie(a)

        # c = self.view.print_aliment(b)

        # d = self.model.best_element(a, c)

        # e = self.view.save_aliment(d)

        # if e = True

        pass

    


if __name__ == '__main__':
    Controller
