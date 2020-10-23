PARAMETERS = {
    'user': 'leo',  # input('user: '),
    'password': 'password',  # input('password: '),
    'database': 'openfoodfacts'
}

DB_NAME = PARAMETERS['database']

TABLES = {}
TABLES['Categories'] = (
    """CREATE TABLE `Categories` (
    `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
    `name` VARCHAR(250) NOT NULL
    ) 
    Engine = InnoDB"""
)

TABLES['Aliments'] = (
    """ CREATE TABLE `Aliments` (
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `barcode` VARCHAR(100) PRIMARY KEY NOT NULL,
    `name` VARCHAR(250) NOT NULL, 
    `nutriscore` CHAR(1) NOT NULL, 
    `url` TEXT NOT NULL, 
    `stores` VARCHAR(150) NOT NULL 
    ) 
    Engine=InnoDB """

)

TABLES['assoc_cat_ali'] = (
    """ CREATE TABLE `assoc_cat_ali` (
    `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `barcode_ali` VARCHAR(100) NOT NULL,
    `cat_id` INT UNSIGNED NOT NULL,
    CONSTRAINT fk_code_ali FOREIGN KEY (`barcode_ali`) REFERENCES Aliments(`barcode`),
    CONSTRAINT fk_id_cat FOREIGN KEY (`cat_id`) REFERENCES Categories(`id`)
    )
    ENGINE=InnoDB """
)

TABLES['Substitute'] = (
    """ CREATE TABLE `Substitute` (
    `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
    `ali_source` VARCHAR(250) NOT NULL, 
    `ali_sub` VARCHAR(250) NOT NULL
    )
ENGINE=InnoDB """
)
# CONSTRAINT fk_ali_source FOREIGN KEY (`ali_source`) REFERENCES Aliments(`barcode`),
#     CONSTRAINT fk_ali_sub FOREIGN KEY (`ali_sub`) REFERENCES Aliments(`barcode`)
# "   CONSTRAINT `fk_categories_id`"
# "       FOREIGN KEY (`id_categories`)"
# "       REFERENCES `Categories`(`id_categories`)"

# TABLES['FK'] = (
#     "ALTER TABLE Aliments"
#     "ADD CONSTRAINT fk_categories_id,"
#     "   FOREIGN KEY (id_categories),"
#     "   REFERENCES Categories (id_categories)"
# )
