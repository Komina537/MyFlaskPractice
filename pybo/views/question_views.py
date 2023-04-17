from datetime import datetime

# from flask import Blueprint, render_template      # 2-05 질문 목록과 질문 상세 기능 만들기
# from pybo.models import Question                  # 2-05 질문 목록과 질문 상세 기능 만들기

from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect

from .. import db                                   # 2-10 폼 데이터를 저장하는 코드 작성하기

from pybo.models import Question, Answer, User

# from pybo.forms import QuestionForm               # 2-10 폼 모듈로 데이터 검증 더 쉽게 하기
from pybo.forms import QuestionForm, AnswerForm     # 2-10 CSRF 코드와 오류 표시 기능 추가하기

from pybo.views.auth_views import login_required

bp = Blueprint('question', __name__, url_prefix='/question')    # main_view.py 파일의 블루프린트와 구별하기 위해 /question 으로 작성

# --------------------------------------------------------------- # 2-10 폼 모듈로 데이터 검증 더 쉽게 하기
@bp.route('/create/', methods=('GET', 'POST'))  # 2-10 질문 전송 방식 수정하기
@login_required
def create():
    form = QuestionForm()
    # question_form.html 템플릿에 전달하는 QuestionForm의 객체(form)는 템플릿에서 라벨이나 입력폼 등을 만들때 필요하다.
# -------------------------------------------------------------------- 2-10 폼 데이터를 저장하는 코드 작성하기
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
# ----------------------------------------------------------------------------------------------------
    return render_template('question/question_form.html', form=form)    # 2-10 폼 모듈로 데이터 검증 더 쉽게 하기

@bp.route('/list/')     # 2-05 index 함수명을 _list로 바꾸고 URL 매핑 규칙도 / 에서 /list/로 바꿈
def _list():            # _list로 지정한 이유는 list가 파이썬의 예약어이기 때문
    page = request.args.get('page', type=int, default=1)    # 3-01 페이징 구현하기
    kw = request.args.get('kw', type=str, default='')
    question_list = Question.query.order_by(Question.create_date.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        sub_query = db.session.query(Answer.question_id, Answer.content, User.username) \
            .join(User, Answer.user_id == User.id).subquery()
        question_list = question_list \
            .join(User) \
            .outerjoin(sub_query, sub_query.c.question_id == Question.id) \
            .filter(Question.subject.ilike(search) |  # 질문제목
                    Question.content.ilike(search) |  # 질문내용
                    User.username.ilike(search) |  # 질문작성자
                    sub_query.c.content.ilike(search) |  # 답변내용
                    sub_query.c.username.ilike(search)  # 답변작성자
                    ) \
            .distinct()
    question_list = question_list.paginate(page=page, per_page=10)  # 3-01 페이징 구현하기
    return render_template('question/question_list.html', question_list=question_list, page=page, kw=kw)


# 3-14 검색 부터 안쓰는 코드
# @bp.route('/list/')
# def _list():
#     page = request.args.get('page', type=int, default=1)  # 페이지
#     question_list = Question.query.order_by(Question.create_date.desc())
#     question_list = question_list.paginate(page=page, per_page=10)
#     return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()         # 2-10 CSRF 코드와 오류 표시 기능 추가하기
    # 이 과정이 없으면 템플릿에서 form 객체를 읽어오지 못해 오류가 난다.
    question = Question.query.get_or_404(question_id)
    # 이전 코드
    # return render_template('question/question_detail.html', question=question)

    # 2-10 CSRF 코드와 오류 표시 기능 추가하기
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/delete/<int:question_id>')
@login_required
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('question._list'))

@bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
@login_required
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    if g.user != question.user:
        flash('수정권한이 없습니다')
        return redirect(url_for('question.detail', question_id=question_id))
    if request.method == 'POST':  # POST 요청
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(question)
            question.modify_date = datetime.now()  # 수정일시 저장
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    else:  # GET 요청
        form = QuestionForm(obj=question)
    return render_template('question/question_form.html', form=form)

@bp.route('/vote/<int:question_id>/')
@login_required
def vote(question_id):
    _question = Question.query.get_or_404(question_id)
    if g.user == _question.user:
        flash('본인이 작성한 글은 추천할수 없습니다')
    else:
        _question.voter.append(g.user)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))
