"""
[Overview]
create a database:
    books.db
create a model:
    title, author, date_published, price
Imports:py, pyi
    - models file
    - functions file(pyi)
    - options file
    - driver file
Program needs:
    menu:options
        - display, get, build, construct, list
    database:books, data
        - add, edit, delete, search, clean
    driver:options
        - add, search, analysis, exit, view
    app:control flow
        - looping
"""
from sqlalchemy import create_engine, Column, Date, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///books.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Book(Base):
    __tablename__ = "books"
    id    = Column(Integer, primary_key=True)
    title = Column('Title', String)
    author = Column('Author', String)
    date_published = Column('Published', Date)
    price = Column('Price', Integer)
    
    def __init__(self, title, author, published, price):
        self.title = title
        self.author = author
        self.date_published = published
        self.price = price

    def __repr__(self):
        return f'Title: {self.title} Author: {self.author} Published: {self.date_published} Price: {self.price/100}'

    @staticmethod
    def commit_changes():
        session.commit()
    
    @staticmethod
    def add_book(book):
        session.add(book)

    @staticmethod
    def edit_book():
        pass

    @staticmethod
    def delete_book(book):
        session.delete(book)

    @staticmethod
    def search_book(title:str):
        return session.query(Book).filter_by(title=title)

    @staticmethod
    def clean_date(date:str):
        def month_str_to_int(month):
            months = ['January', 'February', 'March', 'April', 'May', 'June', 
            'July', 'August', 'September', 'October', 'November', 'December']
            return months.index(month) + 1
        date_group = date.replace(',', '').split(" ")
        year = int(date_group[2])
        month = month_str_to_int(date_group[0])
        day = int(date_group[1])
        return datetime.date(year, month, day)

    @staticmethod
    def clean_price(price:str):
        return int(float(price)*100)
    
