from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode
from app.constants import PARAMETERS as par, DB_NAME, TABLES


class Database:
    """Class that defines all the parameters
    and all the datas contained in the database"""

    def __init__(self):
        """Class constructor that sets cursors' parameters"""

        self.cnx = mysql.connector.connect(user=par['user'],
                                           password=par['password'])
        self.cursor = self.cnx.cursor(buffered=True)

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
        """Method that inserts categories into category database's table"""

        try:
            add_categories = ("INSERT IGNORE INTO `category`"
                              "(name) "
                              "VALUES (%s)")
            data_categories = [[category] for category in data_categories]
            self.cursor.executemany(add_categories, data_categories)
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully "
                                        "into category table")

        except mysql.connector.Error as err:
            print("Failed to insert datas into category table. "
                  "{}".format(err))

    def insert_aliments(self, data_aliments):
        """Method that inserts aliments into aliment database's table"""

        try:
            add_aliments = ("INSERT IGNORE INTO aliment "
                            "(barcode, name, nutriscore, url, stores) "
                            "VALUES (%s, %s, %s, %s, %s) ")

            self.cursor.executemany(add_aliments, data_aliments)
            self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully "
                                        "into aliment table \n")

        except mysql.connector.Error as err:
            print("Failed to insert datas into aliment table. {}".format(err))

    def insert_associated(self, cat, datas):
        """Method that inserts the associated aliments of each category
        into asso_cat_ali database's table"""

        try:
            add_datas = """INSERT IGNORE INTO asso_cat_ali
                        (barcode_ali, cat_id)
                        VALUES (%s, %s)"""

            query = "SELECT `id` FROM `category` WHERE category.name = %s"
            self.cursor.execute(query, (cat,))
            id_cat = self.cursor.fetchone()[0]

            for data in datas:
                d = (data[0], id_cat)
                self.cursor.execute(add_datas, d)
                self.cnx.commit()
            print(self.cursor.rowcount, "Datas inserted successfully "
                                        "into associated table \n")

        except mysql.connector.Error as err:
            print("Failed to insert datas into asso_cat_ali table. "
                  "{}".format(err))

    def select_categories(self):
        """Method that returns the id's and names of all categories"""

        query = """SELECT id, name FROM category """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def select_aliments(self, cat_id):
        """Method that returns all the aliments
        according to one category's id"""

        query = """SELECT aliment.id, aliment.name from aliment
                INNER JOIN asso_cat_ali
                ON aliment.barcode = asso_cat_ali.barcode_ali
                WHERE asso_cat_ali.cat_id = %s"""
        self.cursor.execute(query, (cat_id,))
        result = self.cursor.fetchall()
        return result

    def select_nutriscore(self, ali_id):
        """Method that returns the nutriscore
        of an aliment from a given id"""

        query = """SELECT nutriscore from aliment
                WHERE id = %s"""
        self.cursor.execute(query, (ali_id,))
        nutriscore = self.cursor.fetchone()
        return nutriscore

    def select_substitute(self, cat_id, nutriscore):
        """Method that returns a substitute aliment
        with a better nutriscore"""

        query = """SELECT barcode, name, nutriscore, url, stores from aliment
                    INNER JOIN asso_cat_ali
                    ON aliment.barcode = asso_cat_ali.barcode_ali
                    WHERE asso_cat_ali.cat_id = %s
                    AND nutriscore < %s"""

        nutriscore = ''.join(nutriscore)
        ali_id = int(cat_id)
        datas = ali_id, nutriscore

        self.cursor.executemany(query, [datas])
        substitute = self.cursor.fetchone()
        return substitute

    def insert_substitute(self, aliment, substitute):
        """Method that inserts an aliment and its substitute
        into substitute table"""

        try:
            add_datas = """INSERT INTO substitute
                    (ali_source_barcode, ali_sub_barcode)
                    Values (%s, %s)"""

            query_ali_barcode = """SELECT aliment.barcode FROM aliment
                            WHERE id = %s"""

            self.cursor.execute(query_ali_barcode, (aliment,))
            aliment = self.cursor.fetchone()

            values = aliment[0], substitute[0]
            self.cursor.execute(add_datas, values)
            self.cnx.commit()
            print(self.cursor.rowcount, "substitute saved successfully.")

        except mysql.connector.Error as err:
            print("Failed to insert datas into substitute table. "
                  "{}".format(err))

    def select_saved_substitutes(self):
        """Method that returns all aliments and their substitutes """

        query_ali_source = """SELECT name FROM aliment
                        INNER JOIN substitute
                        ON aliment.barcode = substitute.ali_source_barcode"""

        self.cursor.execute(query_ali_source)
        ali_source = self.cursor.fetchone()
        source_data = []
        while ali_source is not None:
            ali_source = ''.join(ali_source)
            source_data.append(ali_source)
            ali_source = self.cursor.fetchone()

        query_ali_sub = """SELECT name, nutriscore, url, stores from aliment
                        INNER JOIN substitute
                        ON aliment.barcode = substitute.ali_sub_barcode"""
        self.cursor.execute(query_ali_sub)
        ali_sub = self.cursor.fetchone()
        sub_data = []
        while ali_sub is not None:
            ali_sub = ', '.join(ali_sub)
            sub_data.append(ali_sub)
            ali_sub = self.cursor.fetchone()

        result = [source_data, sub_data]
        return result

    def close_cursor(self):
        """Method that closes database's connexion"""

        self.cursor.close()
        self.cnx.close()
