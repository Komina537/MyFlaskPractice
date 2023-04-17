# ------------------------------------
# 서버로 전송된 폼을 처리하는 forms.py 파일
# ------------------------------------

# 파이보 프로젝트는 웹 브라우저에서 서버로 전송된 폼을 처리할 때 WTForms라는 라이브러리를 사용한다.
# WTForms 역시 모델 기반으로 폼을 처리한다. 그래서 폼 클래스를 정의할 forms.py 파일이 필요하다.

# ==================================================================================

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    # 이전 코드
    # subject = StringField('제목', validators=[DataRequired()])
    # content = TextAreaField('내용', validators=[DataRequired()])

    # 2-10 오류 메시지 한글로 바꾸기 코드
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class AnswerForm(FlaskForm):
    # 이전 코드
    # content = TextAreaField('내용', validators=[DataRequired()])

    # 2-10 오류 메시지 한글로 바꾸기 코드
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])

# 3-06 회원 가입 폼 작성
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])

# 3-07 로그인과 로그아웃
class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


# 2-10 폼 모듈로 데이터 검증 더 쉽게 하기 부분에서 사용하는 코드 ( 이후에 사용하지 않는 코드 )
# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField
# from wtforms.validators import DataRequired
#
# class QuestionForm(FlaskForm):
#     subject = StringField('제목', validators=[DataRequired()])
#     content = TextAreaField('내용', validators=[DataRequired()])

# 3-06 회원가입 폼 부분에서 사용하는 코드 ( 이후에 사용하지 않는 코드 )
# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, PasswordField, EmailField
# from wtforms.validators import DataRequired, Length, EqualTo, Email

# 3-06 명령 프롬프트에서 email_validator 설치
# (myproject) c:\projects\myproject>pip install email_validator