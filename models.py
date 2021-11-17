from db_connect import db

class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True,nullable=False,autoincrement=True)
    user_id = db.Column(db.String(100), nullable=False, unique=True)
    user_pw = db.Column(db.String(100), nullable=False) 

    def __init__(self, user_id, user_pw):
        self.user_id = user_id
        self.user_pw = user_pw

