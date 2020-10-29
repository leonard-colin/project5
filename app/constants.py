PARAMETERS = {
    'user': 'leo',  # input('user: '),
    'password': 'password',  # input('password: '),
    'database': 'openfoodfacts'
}

DB_NAME = PARAMETERS['database']

TABLES = {}
TABLES['category'] = (
    """CREATE TABLE `category` (
    `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(250) NOT NULL
    )
    Engine = InnoDB"""
)

TABLES['aliment'] = (
    """ CREATE TABLE `aliment` (
    `id` INT UNSIGNED NOT NULL UNIQUE AUTO_INCREMENT,
    `barcode` BIGINT PRIMARY KEY NOT NULL,
    `name` VARCHAR(250) NOT NULL,
    `nutriscore` CHAR(1) NOT NULL,
    `url` TEXT NOT NULL,
    `stores` VARCHAR(150) NOT NULL
    )
    Engine=InnoDB """
)

TABLES['asso_cat_ali'] = (
    """ CREATE TABLE `asso_cat_ali` (
    `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `barcode_ali` BIGINT NOT NULL,
    `cat_id` INT UNSIGNED NOT NULL,
    CONSTRAINT fk_code_ali FOREIGN KEY (`barcode_ali`)
    REFERENCES aliment(`barcode`),
    CONSTRAINT fk_id_cat FOREIGN KEY (`cat_id`)
    REFERENCES category(`id`)
    )
    ENGINE=InnoDB """
)

TABLES['substitute'] = (
    """ CREATE TABLE `Substitute` (
    `id` INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    `ali_source_barcode` BIGINT NOT NULL,
    `ali_sub_barcode` BIGINT NOT NULL,
    CONSTRAINT fk_ali_source FOREIGN KEY (`ali_source_barcode`)
    REFERENCES aliment(`barcode`),
    CONSTRAINT fk_ali_sub FOREIGN KEY (`ali_sub_barcode`)
    REFERENCES aliment(`barcode`)
    )
ENGINE=InnoDB """
)
