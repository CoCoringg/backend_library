from flask import Blueprint, json, render_template, redirect, jsonify, request, session, g
from db_connect import db
from models import User, Book
from flask_bcrypt import Bcrypt

library = Blueprint('library',__name__)
bcrypt = Bcrypt()


#모든 요청 전에 실행하는 함수인 before_app_request를 활용해서 요청마다 로그인된 사용자가 있는지 파악
@library.before_app_request 
def load_logged_in_user():
        user_id = session.get('login')
        if user_id is None:
                g.user = None
        else:
                g.user = db.session.query(User).filter(User.id == user_id).first()

@library.route("/")
def hello():
    data = Book.query.order_by(Book.id).all()
    return render_template('base.html', data = data)

@library.route('/join', methods=['GET','POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else : #POST일 경우 
        name = request.form['name']
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        pw_hash = bcrypt.generate_password_hash(user_pw)

        user = User(name, user_id, pw_hash)
        db.session.add(user)
        db.session.commit()

        return jsonify({"result":"success"})

@library.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else : #POST 
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']

        user = User.query.filter(User.user_id == user_id).first()

        if user is not None: #해당 ID DB에 존재할 때
            if bcrypt.check_password_hash(user.user_pw, user_pw): #비밀번호 확인
                session['login'] = user.id #세션 주기
                return jsonify({'result':'success'})
            else :
                return jsonify({'result':'fail'})
        else:
            return jsonify({'result':'fail'})

@library.route('/logout')
def logout():
    session['login'] = None
    return redirect('/')


    
        
