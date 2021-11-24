from db_connect import db
from datetime import datetime

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.String(100), nullable=False, unique=True)
    user_pw = db.Column(db.String(100), nullable=False) 

    def __init__(self, name, user_id, user_pw):
        self.name = name
        self.user_id = user_id
        self.user_pw = user_pw

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True,nullable=False)
    book_name = db.Column(db.String(500))
    publisher = db.Column(db.Text)
    author = db.Column(db.Text)
    publication_date = db.Column(db.Text)
    pages = db.Column(db.Integer )
    isbn = db.Column(db.Text)
    description = db.Column(db.Text)
    link = db.Column(db.Text)
    inventory = db.Column(db.Integer)
    starAvg = db.Column(db.Numeric(precision=2, scale=1), default=0)

class Rental(db.Model):
    __tablename__ = 'rental'
    index = db.Column(db.Integer, primary_key=True,nullable=False, autoincrement=True)
    user_id = db.Column(db.String(100), primary_key = True, nullable=False)
    book_name = db.Column(db.Text)
    rental_count = db.Column(db.Integer)

    def __init__(self, user_id, book_name, rental_count):
        self.user_id = user_id
        self.book_name = book_name
        self.rental_count = rental_count

class Post(db.Model):
    __tablename__='post'
    index = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.String(100),primary_key=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    book_id = db.Column(db.Integer, nullable=False)
    starValue = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, content, book_id, starValue):
        self.user_id = user_id
        self.content = content
        self.book_id = book_id
        self.starValue = starValue
