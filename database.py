from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from constants import PARAMETERS as par, DB_NAME, TABLES


class Database:
    """Class that defines all the parameters and all the datas contained in the database"""

    def __init__(self):
        """Class constructor that sets cursors' parameters"""

        self.cnx = mysql.connector.connect(user=par['user'], password=par['password'])  # charset='utf8')
        self.cursor = self.cnx.cursor(buffered=True)
        self.create_database()
        self.create_tables()

    def create_database(self):
        """Method that creates a database"""

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

    def insert_categories(self, data_categories):
        """Method that inserts categories into Categories database's table"""

        data_categories = [[category] for category in data_categories]
        try:
            add_categories = ("INSERT INTO `Categories`"
                              "(name) "
                              "VALUES (%s)")
            self.cursor.executemany(add_categories, data_categories)
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully into Categories table")
            # self.cursor.close()
        except mysql.connector.Error as err:
            print("Failed to insert datas into Categories table. {}".format(err))

    def insert_aliments(self, data_aliments):
        """Method that inserts aliments into Aliments database's table"""

        try:
            add_aliments = ("INSERT IGNORE INTO Aliments "
                            "(barcode, name, nutriscore, url, stores) "
                            "VALUES (%s, %s, %s, %s, %s) ")

            self.cursor.executemany(add_aliments, data_aliments)  # id)  # [data, id])
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully into Aliments table \n")
            # self.cursor.close()
        except mysql.connector.Error as err:
            print("Failed to insert datas into Aliments table. {}".format(err))

    def insert_associated(self, cat, datas):
        """Method that inserts the associated aliments of each category
        into assoc_cat_ali database's table"""

        try:
            add_datas = """INSERT IGNORE INTO assoc_cat_ali
                        (barcode_ali, cat_id)
                        VALUES (%s, %s)"""

            query = "SELECT `id` FROM `Categories` WHERE Categories.name = %s"  # "''' + cat + '''"'''
            self.cursor.execute(query, (cat,))
            id_cat = self.cursor.fetchone()[0]

            for data in datas:
                d = (data[0], id_cat)
                self.cursor.execute(add_datas, d)
                self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully into Associated table \n")
        except mysql.connector.Error as err:
            print("Failed to insert datas into assoc_cat_ali table. {}".format(err))

    def select_categories(self):
        """Method that return the id's and names of all categories"""

        query = """SELECT id, name FROM Categories """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def select_aliments(self, cat_id):
        """Method that..."""

        query = """SELECT Aliments.id, Aliments.name from Aliments
                INNER JOIN assoc_cat_ali
                ON Aliments.barcode = assoc_cat_ali.barcode_ali
                WHERE assoc_cat_ali.cat_id = %s"""
        self.cursor.execute(query, (cat_id,))
        result = self.cursor.fetchall()
        return result

    def select_nutriscore(self, ali_id):

        query = """SELECT nutriscore from Aliments
                WHERE id = %s"""
        self.cursor.execute(query, (ali_id,))
        nutriscore = self.cursor.fetchone()
        return nutriscore

    def select_substitute(self, cat_id, nutriscore):
        """Method that select a substitution aliment with a better nutriscore"""

        query = '''SELECT `name`, `nutriscore`, `url`, `stores` from `Aliments`
                    INNER JOIN `assoc_cat_ali`
                    ON Aliments.barcode = assoc_cat_ali.barcode_ali
                    WHERE assoc_cat_ali.cat_id = %s
                    AND nutriscore < %s'''

        nutriscore = ''.join(nutriscore)
        ali_id = int(cat_id)
        datas = ali_id, nutriscore

        self.cursor.executemany(query, [datas])
        substitute = self.cursor.fetchone()
        return substitute

    def insert_substitute(self, aliment, substitute):

        try:
            add_datas = """INSERT INTO Substitute
                    (ali_source, ali_sub)
                    Values (%s, %s)"""

            query = """SELECT Aliments.name FROM Aliments
                    WHERE id = %s"""

            self.cursor.execute(query, (aliment,))
            aliment = self.cursor.fetchone()
            
            aliment = ''.join(aliment)
            substitute = '\n'.join(substitute)

            values = [aliment, substitute]
            self.cursor.execute(add_datas, values)
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully into Substitute table \n")
        except mysql.connector.Error as err:
            print("Failed to insert datas into Substitute table. {}".format(err))

    def close_cursor(self):
        """Method that closes database's connexion"""
        self.cursor.close()
        self.cnx.close()
        # finally:
        #     if self.cnx.is_connected():
        #         self.cnx.close()
        #         print("MySQL connection is closed")
