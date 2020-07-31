from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from constants import PARAMETERS as par, DB_NAME, TABLES
from model import Model


class Database:

    def __init__(self):
        self.cnx = mysql.connector.connect(user=par['user'], password=par['password'])  # charset='utf8')
        self.cursor = self.cnx.cursor(buffered=True)
        self.create_database()
        self.create_tables()
        self.model = Model()
        self.insert_categories()
        self.insert_aliments()

    def create_database(self):
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

        # self.cursor.close()
        # self.cnx.close()

    def insert_categories(self):
        try:
            add_categories = ("INSERT INTO `Categories`"
                              "(name) "
                              "VALUES (%s)")
            data_categories = self.model.get_categories()
            self.cursor.executemany(add_categories, data_categories)
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully into Categories table")
            # self.cursor.close()
        except mysql.connector.Error as err:
            print("Failed to insert datas into Categories table. {}".format(err))

    def insert_aliments(self):
        try:
            add_aliments = ("INSERT IGNORE INTO Aliments "
                            "(barcode, name, nutriscore, url, stores) "
                            "VALUES (%s, %s, %s, %s, %s) ")
            data_aliments = self.model.get_aliment()

            # for data, cat in data_aliments:
            #     Q1 = 'SELECT id_categories FROM Categories WHERE name = %s'
            #     print(cat)
            #     id = self.cursor.execute(Q1)
            #     print(id)
            self.cursor.executemany(add_aliments, data_aliments)  # id)  # [data, id])
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully into Aliments table")
            self.cursor.close()
        except mysql.connector.Error as err:
            print("Failed to insert datas into Aliments table. {}".format(err))

        # finally:
        #     if self.cnx.is_connected():
        #         self.cnx.close()
        #         print("MySQL connection is closed")

    def display_categories(self):
        query = ("SELECT id_categories, name "
                 "FROM Categories ")
        result = self.cursor.execute(query)
        return result

        # for (id, name) in self.cursor:
        #     print("{}. {}".format(id, name))
        # print dans la View

    def display_aliment(self, cat_id):
        query = ("SELECT id_aliment, name FROM Aliments"
                 "WHERE id_categories = %s")
        result = self.cursor.execute(query, cat_id)
        return result


if __name__ == '__main__':
    Database()
