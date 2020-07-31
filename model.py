from __future__ import print_function
import requests


class Model:

    def __init__(self):
        self.get_data = requests.get("https://fr.openfoodfacts.org/categories.json")
        self.get_categories()
        self.get_aliment()

    def get_categories(self):
        data = (self.get_data.json()['tags'])
        category = []
        for element, cat in enumerate(data):
            if 'name' in cat:
                category.append([cat['name']])
        return category[:30]

    def get_aliment(self):
        category = self.get_categories()
        aliments = []
        for cat in category:
            # get_aliments = requests.get(
            #     "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + str(
            #         cat) + "&json=true")
            get_aliments = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" + str(cat) + "&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1=A&json=true")
            # get_aliments = requests.get("https://fr.openfoodfacts.org/category/" + str(cat) + ".json")
            product = (get_aliments.json()['products'])
            for element in product:
                cat = ''.join(cat)
                if 'generic_name_fr' in element and element['generic_name_fr'] != '':
                    data = [element['code'], element['generic_name_fr'], element['nutriscore_grade'], element['url'], element['stores']]
                    aliments.append(data)
        return aliments


if __name__ == '__main__':
    Model()
