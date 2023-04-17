# ---------------------------------
# 데이터베이스를 처리하는 models.py 파일
# ---------------------------------

# 파이보 프로젝트는 ORM(object relational mapping)을 지원하는 파이썬 데이터베이스 도구인
# SQLAlchemy를 사용한다. SQLAlchemy는 모델 기반으로 데이터베이스를 처리한다.
# 지금은 모델 기반으로 데이터베이스를 처리한다는 말이 이해되지 않겠지만,
# 이후 프로젝트를 진행하면 잘 알 수 있을 것이다. 아무튼 지금 여러분이 알아야 할 내용은
# 파이보 프로젝트에는 "모델 클래스들을 정의할 models.py 파일이 필요하다"는 것이다.

# ================================================================================

from pybo import db

question_voter = db.Table(
    'question_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'), primary_key=True)
)

answer_voter = db.Table(
    'answer_voter',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id', ondelete='CASCADE'), primary_key=True)
)

# 질문 모델 생성 ------------------------------------------------- # 2-04 모델로 데이터 처리하기
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
# ----------------------------------------------------------------------------------------

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=question_voter, backref=db.backref('question_voter_set'))


# Question과 같은 모델 클래스는 db.Model 클래스를 상속하여 만들어야 한다.
# 이때 사용한 db 객체는 __init__.py 파일에서 생성한 SQLAlchemy 클래스의 객체이다.
# Question 모델은 고유 번호(id), 제목(subject), 내용(content), 작성일시(create_date)
# 속성으로 구성했으며, 각 속성은 db.Column으로 생성했다.
# db.Column에 어떤 값들을 전달했는지 살펴보면서 각 속성의 특징을 확인해 보자.

# db.Column() 괄호 안의 첫번째 인수는 데이터 타입을 의미한다.
# 데이터 타입은 속성에 저장할 데이터의 종류를 결정한다.
# db.Integer는 고유 번호와 같은 숫자값에 사용하고, db.String은 제목처럼 글자 수가
# 제한된 텍스트에 사용한다.글 내용처럼 글자 수를 제한할 수 없는 텍스트는 db.Text를 사용한다.
# 작성일시는 날짜와 시각에 해당하는 db.DateTime을 사용했다.

# db.Column에는 데이터 타입 외에 다음과 같은 속성을 추가로 설정할수 있다.
# primary_key ==> 기본 키 설정
# nullable ==> null 값 허용 여부

# 답변 모델 생성 ------------------------------------------------- # 2-04 모델로 데이터 처리하기
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    # question_id 속성은 답변을 질문과 연결하기 위해 추가한 속성이다.
    # 답변은 어떤 질문에 대한 답변인지 알아야 하므로 질문의 id 속성이 필요하다.
    # 그리고 모델을 서로 연결할 때에는 위와 같이 db.ForeignKey를 사용해야 한다.

    # db.ForeignKey의 첫 번째 파라미터 'question.id'는 question 테이블의 id 컬럼을 의미한다.
    # (question 객체의 속성 id로 착각하지 말자.)
    # 즉, Answer 모델의 question_id 속성은 question 테이블의 id 컬럼과 연결된다는 뜻이다.

    # db.ForeignKey의 두 번째 파라미터 ondelete는 삭제 연동 설정이다.
    # 즉, ondelete='CASCADE'는 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제된다는 의미이다.

    question = db.relationship('Question', backref=db.backref('answer_set'))
    # question 속성은 답변 모델에서 질문 모델을 참조하기 위해 추가했다.
    # 위와 같이 db.relationship으로 question 속성을 생성하면 답변 모델에서 연결된 질문 모델의 제목을
    # answer.question.subject처럼 참조할 수 있다.

    # db.relationship의 첫 번째 파라미터는 참조할 모델명이고 두 번째 backref 파라미터는 역참조 설정이다.
    # 역참조란 쉽게 말해 질문에서 답변을 거꾸로 참조하는 것을 의미한다. 한 질문에는 여러 개의 답변이 달릴 수 있는데
    # 역참조는 이 질문에 달린 답변들을 참조할 수 있게 한다.
    # 예를 들어 어떤 질문에 해당하는 객체가 a_question이라면 a_question.answer_set와 같은 코드로
    # 해당 질문에 달린 답변들을 참조할 수 있다.

    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
# ----------------------------------------------------------------------------------------

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    voter = db.relationship('User', secondary=answer_voter, backref=db.backref('answer_voter_set'))

# ------------------------------------------------------------------------ 3-06 회원가입
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# id는 자동으로 증가하는 User 모델의 기본 키이다.
# username, password, email에는 null값을 허용하지 않도록 nullable=False로 설정했다.
# 또 username, email에는 unique=True를 지정했다. unique=True는 "같은 값을 저장할 수 없다"를 뜻한다.
# 이렇게 해야 username과 email이 중복되어 저장되지 않는다.