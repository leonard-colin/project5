from model import Model
from view import View
from database import Database


class Controller:
    """Class that defines the interactions between the View, Model and Database"""

    def __init__(self):
        """Class constructor"""

        self.view = View()
        self.model = Model()
        self.database = Database()

    def pre_process(self):
        categories = self.model.get_categories()
        # categories = [[category] for category in categories]
        self.database.insert_categories(categories)
        aliments = self.model.get_aliments(categories)
        for cat, elements in aliments.items():
            aliments[cat] = self.clean_data(elements)
        for cat, elements in aliments.items():
            self.database.insert_aliments(elements)
        for cat, elements in aliments.items():
            self.database.insert_associated(cat, elements)

        # for category in categories:
        #     for aliment in aliments:
        #         #for aliment in categories:
        #         code_tag = 1
        #         aliment = aliment[code_tag]
        #         self.database.insert_associated(category, aliment[code_tag])

    def clean_data(self, aliments):
        """
            disgusting CODE
        :param aliments:
        :return:
        """
        lst_data = []
        for aliment in aliments:
            for products in aliment['products']:
                valid_tag = ["product_name_fr", "nutriscore_grade", "url", "stores"]
                if not all(tag in products for tag in valid_tag):
                    pass
                else:
                    if products['product_name_fr'] != '':
                        data = [products['code'], products['product_name_fr'], products['nutriscore_grade'],
                                products['url'],
                                products['stores']]
                        lst_data.append(data)
        return lst_data
        # self.database.insert_aliments(lst_data)
        # parsed_data = []
        # valid_tag = ["code", "product_name_fr", "nutrition_grade_fr", "url", "stores"]
        # for aliment in aliments:
        #     for products in aliment["products"]:
        #         # d = dict()
        #         for tag in products:
        #             if tag in valid_tag:
        #                 parsed_data.append(products[valid_tag])
        #                 #d[tag] = products[tag]
        #         # for key in d.values():
        #         #     parsed_data.append(key)
        # print(parsed_data)
        # return parsed_data

    def process(self):
        """Method that defines all the program's process"""
        # self.view.first_screen()
        self.pre_process()
        scenario = self.view.choose_scenario()
        if scenario == '1':
            self.get_substitute()
        elif scenario == '2':
            self.get_saved_aliments()

    def get_substitute(self):
        """Method that gets a substitute aliment with a better nutriscore"""

        categories = self.database.select_categories()
        category = self.view.choose_category(categories)

        aliments = self.database.select_aliments(category)
        aliment = self.view.choose_aliment(aliments)

        nutriscore = self.database.select_nutriscore(aliment)
        if nutriscore == 'a':
            #self.view.is_nutrscore_a(aliment)
            self.get_substitute()
        else:
            substitute = self.database.select_substitute(category, nutriscore)  # nutriscore)
            choice = self.view.print_substitute(aliment, substitute)
            if choice == '1':
                self.database.insert_substitute(aliment, substitute)
            elif choice == '2':
                self.process()
