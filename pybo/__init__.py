# ----------------------------------
# pybo.py를 __init__.py 파일로 변경하기
# ----------------------------------

# 파일명을 바꾸어도 플라스크 서버가 잘 실행된다. 우리는 플라스크 기본 앱을 FLASK_APP=pybo로 설정했다.

# ----------------------------------------------------------
# [ 1-06 안녕하세요, 파이보! ] 에서 cmd 창에

#             ==> (myproject) c:\projects\myproject>set FLASK_APP=pybo <==

# 을 사용하여 [ 플라스크 기본 앱을 FLASK_APP=pybo로 설정 ]
# ----------------------------------------------------------

# 따라서 이전에 pybo는 프로젝트 루트에 있는 pybo.py 파일을 가리켰지만,
# 이번에는 pybo 모듈 즉 pybo/__init__.py 파일을 가리킨다.

# ======================================================================================

from flask import Flask

from flask_migrate import Migrate               # 2-04 모델로 데이터 처리하기
from flask_sqlalchemy import SQLAlchemy         # 2-04 모델로 데이터 처리하기

from sqlalchemy import MetaData

from flaskext.markdown import Markdown

import config                                   # 2-04 모델로 데이터 처리하기

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
# db = SQLAlchemy()                             # 2-04 모델로 데이터 처리하기
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

def create_app():   # create_app 함수가 애플리케이션 팩토리
    app = Flask(__name__)
    # app.config.from_object(config)              # 2-04 모델로 데이터 처리하기
    app.config.from_envvar('APP_CONFIG_FILE')   # 4-08 서버 개발 환경을 위한 config 분리하기

    # ORM -----------------------------------   # 2-04 모델로 데이터 처리하기
    db.init_app(app)
    # migrate.init_app(app, db)                 # 2-04 모델로 데이터 처리하기
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    # --------------------------------------------------------------------------------
    from . import models                        # 2-04 모델로 데이터 처리하기
    # 앞에서 작성한 모델을 플라스크의 migrate 기능이 인식하려면 다음과 같은 import 과정이 필요하다.
    # (myproject) c:\projects\myproject> flask db migrate ==> 리비전 파일 생성
    # (myproject) c:\projects\myproject> flask db upgrade ==> 리비전 파일 실행
    # --------------------------------------------------------------------------------

    # 블루프린트
    # 플라스크에서는 URL과 함수의 매핑을 관리하기 위해 사용하는 도구(클래스)이다.
    from .views import main_views, question_views, answer_views, auth_views, clock_views, whoiam_views, MovieDL_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)   # 2-05 질문 목록과 질문 상세 기능 만들기
    app.register_blueprint(answer_views.bp)     # 2-06 답변 등록 기능 만들기
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(clock_views.bp)
    app.register_blueprint(whoiam_views.bp)
    app.register_blueprint(MovieDL_views.bp)

    # 3-03 템플릿 필터 직접 만들어보기
    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])

    return app

# ------------------------------------------------
# 데이터베이스 초기화하기
# ------------------------------------------------

# 이제 ORM을 사용할 준비가 되었으므로 flask db init 명령으로 데이터베이스를 초기화하자.

# ==> (myproject) c:\projects\myproject>flask db init

# ============================================================================