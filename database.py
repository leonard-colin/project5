from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from constants import PARAMETERS as par, DB_NAME, TABLES
from controller import Controller


class Database:
    """Class that defines all the parameters and all the datas contained in the database"""

    def __init__(self):
        """Class constructor that sets cursors' parameters"""

        self.cnx = mysql.connector.connect(user=par['user'], password=par['password'])  # charset='utf8')
        self.cursor = self.cnx.cursor(buffered=True)
        self.create_database()
        self.create_tables()
        self.controller = Controller()
        self.insert_categories()
        self.insert_aliments()

    def create_database(self):
        """Method that create a database"""

        try:
            self.cursor.execute("DROP DATABASE IF EXISTS Openfoodfacts")
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
            print("Database {} created successfully.".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))

        try:
            self.cursor.execute("USE {}".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database()
                self.cnx.database = DB_NAME
            else:
                print(err)

    def create_tables(self):
        """Method that creates database's tables"""

        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        print("\n Inserting datas...\n")

        # self.cursor.close()
        # self.cnx.close()

    def insert_categories(self):
        """Method that inserts categories into Categories database's table"""

        try:
            add_categories = ("INSERT INTO `Categories`"
                              "(name) "
                              "VALUES (%s)")
            data_categories = self.controller.add_aliments()
            self.cursor.executemany(add_categories, data_categories)
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully into Categories table")
            # self.cursor.close()
        except mysql.connector.Error as err:
            print("Failed to insert datas into Categories table. {}".format(err))

    def insert_aliments(self):
        """Method that inserts aliments into Aliments database's table"""

        try:
            add_aliments = ("INSERT IGNORE INTO Aliments "
                            "(barcode, name, nutriscore, url, stores) "
                            "VALUES (%s, %s, %s, %s, %s) ")
            data_aliments = self.controller.add_aliments()

            self.cursor.executemany(add_aliments, data_aliments)  # id)  # [data, id])
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully into Aliments table \n")
            # self.cursor.close()
        except mysql.connector.Error as err:
            print("Failed to insert datas into Aliments table. {}".format(err))

    def insert_associated(self, cat, barcode):
        """Method that inserts the associated aliments of each category
        into assoc_cat_ali database's table"""

        try:
            add_datas = ("""INSERT IGNORE INTO assoc_cat_ali
                        (barcode_ali, cat_id)
                        VALUES (%s, %s)
                        """)
            data = (cat, barcode)

            self.cursor.execute(add_datas, data)
            self.cnx.commit()
        except mysql.connector.Error as err:
            print("Failed to insert datas into assoc_cat_ali table. {}".format(err))

        # finally:
        #     if self.cnx.is_connected():
        #         self.cnx.close()
        #         print("MySQL connection is closed")

    def get_categories(self):
        """Method that return the id's and names of all categories"""

        query = """SELECT id, name FROM Categories """
        result = self.cursor.execute(query)
        return result
        # for (id, name) in self.cursor:
        #     cat_list = "{}. {}".format(id, name)
        #     return cat_list

    # def display_categories(self):
    #     """Method that"""
    #
    #     cat = self.get_categories()
    #     for (id, name) in cat:
    #         cat_list = "{}. {}".format(id, name)
    #         return cat_list

    def select_category(self):
        """Method that selects all the aliments according to one category"""

        query = """SELECT barcode, name FROM Aliments
                    INNER JOIN Category
                    ON Aliments.barcode = Category.id
                    WHERE Category.id = %s  """
        self.cursor.execute(query)
        pass

        # for (id, name) in self.cursor:
        #     print("{}. {}".format(id, name))
        # print dans la View

    def select_aliment(self, cat_id):
        """Method that..."""
        query = ("SELECT id_aliment, name FROM Aliments"
                 "WHERE id_categories = %s")
        result = self.cursor.execute(query, cat_id)
        return result

    def close_cursor(self):
        """Method that closes database's connexion"""
        self.cursor.close()
        self.cnx.close()

# if __name__ == '__main__':
#     Database()
