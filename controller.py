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
                        data = [products['code'], products['product_name_fr'], products['nutriscore_grade'], products['url'],
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
        self.pre_process()
        scenario = self.view.choose_scenario()
        # try catch needed si l'utilisateur rentre des lettres
        if scenario not in ('1', '2'):
            self.view.choose_scenario()
        elif scenario == '1':
            self.get_substitute()
        elif scenario == '2':
            self.get_saved_aliments()

    def get_substitute(self):
        """Method that gets a substitue aliment with a better nutriscore"""

        self.view.display_categories(self.model.get_categories())

        category = self.view.choose_category()

        self.view.print_aliment(category)

        aliment = self.view.choose_aliment()

        # d = self.model.best_element_by_cat(a, c)

        # e = self.view.save_aliment(d)

        # if e = True

    # def add_categories(self):
    #     """Method that return a list of categories from the API"""
    #
    #     data = self.model.get_categories()
    #     category = []
    #     for element, cat in enumerate(data):
    #         if 'name' in cat:
    #             category.append([cat['name']])
    #     self.database.insert_categories(category[:50])

    def choose_category(self):
        """Method that set conditions for a category selection by the user"""
        categories = self.database.get_categories()
        cat = range(1, 51)
        if categories != cat or categories != int:
            self.choose_category()
        return cat

    def choose_aliment(self, cat):
        """Method that..."""
        ali = self.view.display_categories(cat)

    def get_saved_aliments(self):
        """Method that..."""
        """
            cette methode n'existe pas
        """
        choice = self.view.display_saved_aliments()
        if choice == '1':
            # Show all saved aliments
            pass
        elif choice == '2':
            # Show saved aliments by cat
            pass

# if __name__ == '__main__':
#     Controller()


# from model import Model
# from view import View
# from database import Database
#
#
# class Controller:
#     """Class that defines the interactions between the View, Model and Database"""
#
#     def __init__(self):
#         """Class constructor"""
#
#         self.view = View()
#         self.model = Model()
#         self.database = Database()
#
#     # def pre_data(self):
#     #     self.database.insert_categories()
#     #     self.database.insert_aliments()
#
#     def process(self):
#         """Method that defines all the program's process"""
#
#         self.add_categories()
#         self.add_aliments()
#
#
#         scenario = self.view.choose_scenario()
#         if scenario not in ('1', '2'):
#             self.view.choose_scenario()
#         elif scenario == '1':
#             self.get_substitute()
#         elif scenario == '2':
#             self.get_saved_aliments()
#
#     def get_substitute(self):
#         """Method that gets a substitue aliment with a better nutriscore"""
#
#         self.view.display_categories(self.model.get_categories())
#
#         category = self.view.choose_category()
#
#         self.view.print_aliment(category)
#
#         aliment = self.view.choose_aliment()
#
#         # d = self.model.best_element_by_cat(a, c)
#
#         # e = self.view.save_aliment(d)
#
#         # if e = True
#
#     def add_categories(self):
#         """Method that return a list of categories from the API"""
#
#         data = self.model.get_categories()
#         category = []
#         for element, cat in enumerate(data):
#             if 'name' in cat:
#                 category.append([cat['name']])
#         self.database.insert_categories(category[:50])
#
#
#     def add_aliments(self):
#         """Method that adds all aliments from all categories in a list"""
#
#         lst_data = []
#         aliments = self.model.get_aliments()
#         print(aliments)
#         for element in aliments['products']:
#             if not all(tag in element for tag in ("generic_name_fr", "nutriscore_grade", "url", "stores")):
#                 pass
#             else:
#                 if element['generic_name_fr'] != '':
#                     data = [element['code'], element['generic_name_fr'], element['nutriscore_grade'], element['url'],
#                             element['stores']]
#                     lst_data.append(data)
#                     print(lst_data)
#                     # self.database.insert_associated(cat, element['code'])
#         self.database.insert_aliments(lst_data)
#
#     def choose_category(self):
#         """Method that set conditions for a category selection by the user"""
#         categories = self.model.display_categories()
#         cat = range(1, 51)
#         if categories != cat or categories != int:
#             self.choose_category()
#         return cat
#
#     def choose_aliment(self, cat):
#         """Method that..."""
#         ali = self.display_categories(cat)
#
#     def get_saved_aliments(self):
#         """Method that..."""
#
#         choice = self.view.display_saved_aliments()
#         if choice == '1':
#             # Show all saved aliments
#             pass
#         elif choice == '2':
#             # Show saved aliments by cat
#             pass
#
# # if __name__ == '__main__':
# #     Controller()
