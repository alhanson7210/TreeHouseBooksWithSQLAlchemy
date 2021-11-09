""" App.py
[Overview]
Imports:py, pyi
    - models file
    - functions file(pyi)
    - options file
    - driver file
Program needs:
    main_menu:options
        - add, search, analysis, exit, view
    functions:books, data
        - add, edit, delete, search, clean
    database:books
        - add
    driver:control flow
        - looping
[Local Setup Steps]
Create a folder for your project:
    mkdir folder; cd folder
Open your folder in your IDE(Optional)
Open the terminal in your IDE(Optional)
Create a virtual environment
    Mac:
        python3 -m venv env
    Windows:
        python -m venv env
Activate your environment
    Mac:
        source ./env/bin/activate
    Windows:
        .\env\Scripts\activate
Install SQLAlchemy:
    pip install sqlalchemy
Create requirements file:
     pip freeze > requirements.txt
"""
from driver import (add_option, search_option, analysis_option, view_option)
from menu import (get_option, get_menus)
from models import (Book, Base, engine, session)
import csv

def app_add_csv():
    with open("suggested_books.csv") as books_csv_file:
        book_groupings = csv.reader(books_csv_file)
        for book_info_group in book_groupings:
            title, author, date, price = book_info_group
            book_does_not_exist = session.query(Book).filter_by(title=title).count() == 0
            if book_does_not_exist:
                Book.add_book(Book(title=title, author=author, published=Book.clean_date(date), price=Book.clean_price(price)))
        Book.commit_changes()

def app_driver():
    menus = get_menus()
    main_menu = menus['main_menu']
    running_system = True
    while running_system:
        option = get_option(main_menu['options'], main_menu['start'], main_menu['end'])
        if option == 1:
            add_option()
        elif option == 2:
            view_option()
        elif option == 3:
            search_option()
        elif option == 4:
            analysis_option()
        elif option == 5:
            running_system = False
        else:
            running_system = False
    #end
#end
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    #app_driver()
    app_add_csv()
    for book in session.query(Book):
        print(book)
#end
