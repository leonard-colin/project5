from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from constants import PARAMETERS as par, DB_NAME, TABLES


class Database:
    """Class that defines all the parameters
    and all the datas contained in the database"""

    def __init__(self):
        """Class constructor that sets cursors' parameters"""

        self.cnx = mysql.connector.connect(user=par['user'],
                                           password=par['password'])
        self.cursor = self.cnx.cursor(buffered=True)

    def is_database_created(self):
        """Method that verify if the database already exists
        and returns the name of the database if it does"""

        query = """SELECT SCHEMA_NAME
                FROM INFORMATION_SCHEMA.SCHEMATA
                WHERE SCHEMA_NAME = %s"""
        self.cursor.execute(query, (DB_NAME,))
        db = self.cursor.fetchone()
        if db is None:
            pass
        else:
            db = ''.join(db)
            self.cursor.execute("USE {}".format(DB_NAME))
            return db

    def create_database(self):
        """Method that creates a database"""

        try:
            self.cursor.execute(
                "CREATE DATABASE IF NOT EXISTS {} "
                "DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
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

    def insert_categories(self, data_categories):
        """Method that inserts categories into Categories database's table"""

        try:
            add_categories = ("INSERT IGNORE INTO `Categories`"
                              "(name) "
                              "VALUES (%s)")
            data_categories = [[category] for category in data_categories]
            self.cursor.executemany(add_categories, data_categories)
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully "
                                        "into Categories table")

        except mysql.connector.Error as err:
            print("Failed to insert datas into Categories table. "
                  "{}".format(err))

    def insert_aliments(self, data_aliments):
        """Method that inserts aliments into Aliments database's table"""

        try:
            add_aliments = ("INSERT IGNORE INTO Aliments "
                            "(barcode, name, nutriscore, url, stores) "
                            "VALUES (%s, %s, %s, %s, %s) ")

            self.cursor.executemany(add_aliments, data_aliments)
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully "
                                        "into Aliments table \n")

        except mysql.connector.Error as err:
            print("Failed to insert datas into Aliments table. {}".format(err))

    def insert_associated(self, cat, datas):
        """Method that inserts the associated aliments of each category
        into assoc_cat_ali database's table"""

        try:
            add_datas = """INSERT IGNORE INTO assoc_cat_ali
                        (barcode_ali, cat_id)
                        VALUES (%s, %s)"""

            query = "SELECT `id` FROM `Categories` WHERE Categories.name = %s"
            self.cursor.execute(query, (cat,))
            id_cat = self.cursor.fetchone()[0]

            for data in datas:
                d = (data[0], id_cat)
                self.cursor.execute(add_datas, d)
                self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully "
                                        "into Associated table \n")

        except mysql.connector.Error as err:
            print("Failed to insert datas into assoc_cat_ali table. "
                  "{}".format(err))

    def select_categories(self):
        """Method that returns the id's and names of all categories"""

        query = """SELECT id, name FROM Categories """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def select_aliments(self, cat_id):
        """Method that returns all the aliments
        according to one category's id"""

        query = """SELECT Aliments.id, Aliments.name from Aliments
                INNER JOIN assoc_cat_ali
                ON Aliments.barcode = assoc_cat_ali.barcode_ali
                WHERE assoc_cat_ali.cat_id = %s"""
        self.cursor.execute(query, (cat_id,))
        result = self.cursor.fetchall()
        return result

    def select_nutriscore(self, ali_id):
        """Method that returns the nutriscore
        of an aliment from a given id"""

        query = """SELECT nutriscore from Aliments
                WHERE id = %s"""
        self.cursor.execute(query, (ali_id,))
        nutriscore = self.cursor.fetchone()
        return nutriscore

    def select_substitute(self, cat_id, nutriscore):
        """Method that returns a substitute aliment
        with a better nutriscore"""

        query = """SELECT `name`, `nutriscore`, `url`, `stores` from `Aliments`
                    INNER JOIN `assoc_cat_ali`
                    ON Aliments.barcode = assoc_cat_ali.barcode_ali
                    WHERE assoc_cat_ali.cat_id = %s
                    AND nutriscore < %s"""

        nutriscore = ''.join(nutriscore)
        ali_id = int(cat_id)
        datas = ali_id, nutriscore

        self.cursor.executemany(query, [datas])
        substitute = self.cursor.fetchone()
        return substitute

    def insert_substitute(self, aliment, substitute):
        """Method that inserts an aliment and its substitute
        into Substitute table"""

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
            print(self.cursor.rowcount, "substitute saved successfully.")

        except mysql.connector.Error as err:
            print("Failed to insert datas into Substitute table. "
                  "{}".format(err))

    def select_saved_substitutes(self):
        """Method that returns all aliments and their substitutes """

        query = """SELECT * FROM Substitute
                ORDER BY id ASC"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def close_cursor(self):
        """Method that closes database's connexion"""

        self.cursor.close()
        self.cnx.close()
