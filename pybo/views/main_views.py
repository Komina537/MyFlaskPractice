# from flask import Blueprint, render_template                  # 2-05 질문 목록과 질문 상세 기능 만들기
from flask import Blueprint, url_for                            # 2-05 url_for로 리다이렉트 기능 추가하기
from werkzeug.utils import redirect                             # 2-05 url_for로 리다이렉트 기능 추가하기

from pybo.models import Question                                # 2-05 질문 목록과 질문 상세 기능 만들기

# 이 코드는 pybo/__init__.py 파일의 create_app 함수 안에 있던 hello_pybo 함수를
# main_views.py 파일에 그대로 옮긴 것이다.
# 단, 애너테이션이 @app.route에서 @bp.route로 변경되었다.
# 이 변화에 주목하자. @bp.route에서 bp 객체는 다음처럼 생성되었다.

bp = Blueprint('main', __name__, url_prefix='/')

# bp 객체 생성시 사용된 __name__은 모듈명인 "main_views"가 인수로 전달된다.
# 첫번째 인수로 전달한 "main"은 블루프린트의 "별칭"이다.
# 이 별칭은 나중에 자주 사용할 url_for 함수에서 사용된다.
# 그리고 url_prefix는 라우팅 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL을 의미한다.
# 예를 들어 main_views.py 파일의 URL 프리픽스에 url_prefix='/' 대신
# url_prefix='/main'이라고 입력했다면 hello_pybo 함수를 호출하는 URL은
# localhost:5000/이 아니라 localhost:5000/main/이 된다.

@bp.route('/hello')
def hello_pybo():
    return redirect(url_for('clock._clock'))



@bp.route('/')
def index():
    # ---------------------- # 2-05 질문 목록과 질문 상세 기능 만들기 -----------------------
    # question_list = Question.query.order_by(Question.create_date.desc())
    # return render_template('question/question_list.html', question_list=question_list)
    # ----------------------------------------------------------------------------------

    # 질문 목록 데이터는 question_list = Question.query.order_by(Question.create_date.desc())
    # 로 얻을 수 있다. order_by는 조회 결과를 정렬하는 함수이다.
    # order_by(Question.create_date.desc()) 의 의미는 조회된 데이터를 작성일시 기준으로
    # 역순으로 정렬하라는 의미이다. 역순이 아닌 작성일시 순으로 조회하기 위해서는
    # order_by(Question.create_date.asc()) 또는 asc() 를 생략하여
    # order_by(Question.create_date)와 같이 사용하면 된다.

    # render_template 함수는 템플릿 파일을 화면으로 렌더링 하는 함수이다.
    # 조회한 질문 목록 데이터를 render_template 함수의 파라미터로 전달하면
    # 템플릿에서 해당 데이터로 화면을 구성할수 있다. 여기서 사용한 question/question_list.html 파일을
    # 템플릿 파일이라고 부른다.

    return redirect(url_for('clock._clock'))
    # return redirect(url_for('question._list'))  # 2-05 url_for로 리다이렉트 기능 추가하기
    # detail 함수는 제거하고 index 함수는 question._list에 해당하는 URL로 리다이렉트(redirect)하도록 코드를 수정했다.
    # redirect 함수는 입력받은 URL로 리다이렉트하고, url_for 함수는 라우팅 함수명으로 URL을 역으로 찾는 함수이다.
    # redirect(URL) - URL로 페이지를 이동
    # url_for(라우팅 함수명) - 라우팅 함수에 매핑되어 있는 URL을 리턴

    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 이부분 다시 읽어보자 -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # url_for 함수에 전달된 question._list는 question, _list 순서로 해석되어 라우팅 함수를 찾는다.
    # question은 등록된 블루프린트 별칭, _list는 블루프린트에 등록된 함수명이다.
    # 따라서 question._list는 question이라는 별칭으로 등록한 question_views.py 파일의 _list 함수를 의미한다.
    # 그리고 _list 함수에 등록된 URL 매핑 규칙은 @bp.route('/list/')이므로
    # url_for('question._list')는 bp의 프리픽스 URL인 /question/과 /list/가 더해진 /question/list/ URL을 반환한다.


# ---------------------- # 2-05 질문 목록과 질문 상세 기능 만들기 -----------------------
# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/question_detail.html', question=question)

# detail 함수의 매개변수 question_id에는 URL 매핑 규칙에 사용한 <int:question_id>가 전달된다.
# 즉, http://localhost:5000/detail/[[MARK]]2[[/MARK]]/ 페이지를 요청하면
# main_views.py 파일의 detail 함수가 실행되고, 매개변수 question_id에는 2라는 값이 전달된다.

