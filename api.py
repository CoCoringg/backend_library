from flask import Blueprint, json, render_template, redirect, jsonify, request, session, g
from flask.templating import render_template_string
from db_connect import db
from models import User, Book, Rental, Post
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
    if session.get('login') is not None:
        
        data = Book.query.order_by(Book.id).all()
         
        return render_template('book_list.html', data = data)
    
    else:
        data = Book.query.order_by(Book.id).all()
        return render_template('book_list.html', data = data, rental_data = None)

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


@library.route('/detail/<id>')
def detail_go(id):
    id = int(id)
    book_data = Book.query.filter(Book.id == id).all()
    if id == 1 or id == 2 or id == 3 or id == 7 or id == 8 or id == 9 :
        img_url = f'book_img/{id}.png'
    else :
        img_url = f'book_img/{id}.jpg'
    return render_template('detail.html', data = book_data, img_url = img_url)



@library.route('/rentalpopup/<id>')
def rental_popup(id):
    id = int(id) #책 ID
    
    # if session.get("login") is not None:
    book_data = Book.query.filter(Book.id == id).all()
    return render_template('rentalpopup.html', data = book_data) 
        

@library.route('/rental', methods=['POST'])
def rental():
    
    book_name = request.form['book_name']
    user = User.query.filter(User.id== session.get('login')).first() #대여하는 user 정보
    
    if Rental.query.filter(Rental.user_id == user.user_id and Rental.book_name == book_name).first() is None:
        rental = Rental(user.user_id, book_name, 1 )
        Book.query.filter(Book.book_name == book_name).update({'inventory': Book.inventory - 1})
        db.session.add(rental)
        db.session.commit()
        return jsonify({"result":"success"})
    else:
        return jsonify({"result":"fail"})

    # 대여 오류 - rental 테이블에 해당 이름의 책 존재 시 대여 못하게 하는 기능
    # 반납기능
    # 반납 과 대여 버튼 구분하고싶다.


#반납하기
@library.route('/returnpopup/<id>')
def renturn_popup(id):
    id = int(id) #책 ID
    book_data = Book.query.filter(Book.id == id).all()
    return render_template('returnpopup.html', data = book_data) 

@library.route('/return', methods=['POST'])
def return_go():
    
    book_name = request.form['book_name']
    user = User.query.filter(User.id== session.get('login')).first() #대여하는 user 정보
    
    if Rental.query.filter(Rental.user_id == user.user_id and Rental.book_name == book_name).first() is None: #대여한적 없을 때
        return jsonify({"result":"fail"})
    else:
        Rental.query.filter(Rental.user_id == user.user_id and Rental.book_name == book_name).delete()
        book_return = Book.query.filter(Book.book_name == book_name).first()
        book_return.inventory +=1
        db.session.commit() 
        return jsonify({"result":"success"})

#댓글 저장 - post 테이블에
@library.route('/post', methods=["POST"])
def post():
    user_id = request.form['user_id']
    content = request.form['content']

    post = Post(user_id, content)
    db.session.add(post)
    db.session.commit()

    return jsonify({"result":"success"})