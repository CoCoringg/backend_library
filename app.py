from flask import Flask, json, request, jsonify, session
from flask.templating import render_template
import pymysql
from flask_cors import CORS
from api import library
from db_connect import db
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.register_blueprint(library)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:93990@127.0.0.1:3306/library"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'asodfajsdofijac'

db.init_app(app)
bcrypt = Bcrypt(app)

if __name__ == '__main__':
    app.run(debug=True)

