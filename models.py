from db_connect import db

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.String(100), nullable=False, unique=True)
    user_pw = db.Column(db.String(100), nullable=False) 

    def __init__(self, user_id, user_pw):
        self.user_id = user_id
        self.user_pw = user_pw

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True,nullable=False)
    book_name = db.Column(db.Text)
    publisher = db.Column(db.Text)
    author = db.Column(db.Text)
    publication_date = db.Column(db.Text)
    pages = db.Column(db.Integer )
    isbn = db.Column(db.Text)
    description = db.Column(db.Text)
    link = db.Column(db.Text)

