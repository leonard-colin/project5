PARAMETERS = {
    'user': input('user: '),
    'password': input('password: '),
    'database': 'openfoodfacts'
}

DB_NAME = "openfoodfacts"

TABLES = {}
TABLES['categories'] = (
    "CREATE TABLE categories ("
    "   id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "   name VARCHAR(14) NOT NULL,"
    "   PRIMARY KEY (id)"
    ")"
)

TABLES['aliments'] = (
    "CREATE TABLE aliments ("
    "   id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "   name VARCHAR(14) NOT NULL,"
    "   nutri_score VARCHAR(1) NOT NULL,"
    "   PRIMARY KEY (id)"
    ")"
)
