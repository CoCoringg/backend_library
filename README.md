# 도서관대출서비스

- Flask를 사용하여 도서관대출서비스 웹 페이지 구현 


## 프로젝트 구성 안내

## 1. 프로젝트 소개

### 1-1. 구현한 기능

- **로그인**
    
    - 유저로부터 아이디(이메일)와 비밀번호 정보를 입력받아 로그인
    - 아이디와 비밀번호는 필수 입력 사항
    - 로그인한 유저에 대해 session으로 관리
    - 비밀번호는 아래의 개인정보 보호조치 기준에 맞추어 최소 8자리 이상의 길이로 입력 받기
        - [개인정보의 기술적·관리적 보호조치 기준](https://www.law.go.kr/%ED%96%89%EC%A0%95%EA%B7%9C%EC%B9%99/(%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%9C%84%EC%9B%90%ED%9A%8C)%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4%EC%9D%98%EA%B8%B0%EC%88%A0%EC%A0%81%C2%B7%EA%B4%80%EB%A6%AC%EC%A0%81%EB%B3%B4%ED%98%B8%EC%A1%B0%EC%B9%98%EA%B8%B0%EC%A4%80/(2020-5,20200811))
        - [한국인터넷진흥원 개인정보의 기술적·관리적 보호조치 기준 해설서](https://www.kisa.or.kr/public/laws/laws3_View.jsp?cPage=7&mode=view&p_No=259&b_No=259&d_No=102&ST=T&SV=)
    - 아이디는 이메일 형식으로만 입력 받기

- **회원가입**
    
    - 유저로부터 아이디(이메일), 비밀번호, 이름 정보를 입력받아 회원가입
    - 비밀번호와 비밀번호 확인의 값이 일치
    - 아이디는 이메일 형식으로만 정보를 입력
    - 이름은 한글, 영문으로만 입력
    - 비밀번호는 아래의 개인정보 보호조치 기준에 맞추어 영문, 숫자, 특수문자 중 2종류 이상을 조합하여 최소 10자리 이상 또는 3종류 이상을 조합하여 최소 8자리 이상의 길이로 구성
        - [개인정보의 기술적·관리적 보호조치 기준](https://www.law.go.kr/%ED%96%89%EC%A0%95%EA%B7%9C%EC%B9%99/(%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8%EC%9C%84%EC%9B%90%ED%9A%8C)%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4%EC%9D%98%EA%B8%B0%EC%88%A0%EC%A0%81%C2%B7%EA%B4%80%EB%A6%AC%EC%A0%81%EB%B3%B4%ED%98%B8%EC%A1%B0%EC%B9%98%EA%B8%B0%EC%A4%80/(2020-5,20200811))
        - [한국인터넷진흥원 개인정보의 기술적·관리적 보호조치 기준 해설서](https://www.kisa.or.kr/public/laws/laws3_View.jsp?cPage=7&mode=view&p_No=259&b_No=259&d_No=102&ST=T&SV=)

- **로그아웃**
    
    - 현재 로그인한 유저에 대해 로그아웃
    - 로그아웃한 유저를 현재 session에서 제거

- **메인 페이지**
    
    - 현재 DB 상에 존재하는 모든 책 정보를 가져옴
    - 현재 DB 상에 존재하는 남은 책의 수를 표기
    - 책 이름을 클릭 시 책 소개 페이지로 이동
    - 책의 평점은 현재 DB 상에 담겨있는 모든 평점의 평균으로 표기, 숫자 한자리수로 반올림하여 표기
    
- **대여하기**
    
    - 메인 페이지의 대여하기 버튼을 클릭하여 실행
    - 현재 DB 상에 책이 존재 하지 않는 경우, 대여되지 않음
    - 현재 DB 상에 책에 존재하는 경우, 책을 대여하고 책의 권수를 -1 
    - 현재 DB 상에 책이 존재하지 않는 경우, 유저에게 대여가 불가능하다는 메세지를 반환
    - 유저가 이미 이 책을 대여했을 경우, 이에 대한 안내 메세지를 반환

- **반납하기**
    
    - 반납하기 버튼을 통해 책을 반납, 책을 반납한 후 DB 상에 책의 권수를 +1 

- **책소개**
    
    - 메인 페이지의 책 이름을 클릭하여 접근
    - 책에 대한 소개를 출력
    - 가장 최신의 댓글이 보이도록 정렬
    - 댓글을 작성, 책에 대한 평점
    - 댓글 내용과 평가 점수는 모두 필수 입력 사항
    - 
- **마이페이지**
   
    - 로그인한 유저가 대여 한 책에 대한 정보를 출력



### 1-2. 사용 테이블


  | 테이블 이름      | 데이터 설명                  |
  | ----------------- | ---------------------------- |
  | book              | 책 정보 담긴 테이블    |
  | post              | 댓글 정보 테이블            |
  | rental            | 책 대여 테이블                  |
  | user              | 유저 테이블          |

  

  

### 1-3. 기술 스택

- Flask, Flask-jinja2 , MariaDB, PyMySQL, SQLAlchemy, JavaScript, CSS, jQuery




### 1-4. 웹서비스에 대한 자세한 개요

- 도서 정보 데이터를 활용한 도서관 대출 웹 서비스 
- 책 목록에서 책 클릭 시 상세정보 페이지 전환 -> 상세정보 페이지에서 댓글 남길 수 있음
- 책 목록에서 대여/반납 기능 


## 2. 프로젝트 목표

  - 파이썬을 활용한 웹 서비스 구현



