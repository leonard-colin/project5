# Find better aliments with OpenFoodFacts

### Installation 

* If you're on MacOS, you can install Pipenv and Mysql easily with Homebrew:

    $ brew install mysql  
    $ brew install pipenv

Otherwise, refer to [MySQL](https://dev.mysql.com/doc/refman/8.0/en/installing.html) and [Pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv) documentation for instructions.

* Once you installed pipenv, clone project repository and install from Pipfile:

    $ pipenv install  

* Next, activate the Pipenv shell:

    $ pipenv shell
    
    This will spawn a new shell subprocess, which can be deactivated by using `exit`.

### Usage

* From project source directory, run `main.py` (i.g.: `python3 main.py`)

* Wait a few seconds for the database to create if you run the program for the first time. 

* Press 1 to find a substitute to an aliment you choose from the list according to a category.  
  You have the possibility to save the chosen aliment with its substitute.
   
* Press 2 to see your saved aliments.

* Press 3 to quit the program.
