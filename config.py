# ------------------------------------
# 파이보 프로젝트를 설정하는 config.py 파일
# ------------------------------------

# config.py 파일은 파이보 프로젝트의 환경을 설정한다.
# 파이보 프로젝트의 환경변수, 데이터베이스 등의 설정을 이 파일에 저장한다.

# =============================================================

# ---------------------------
# 플라스크 ORM 라이브러리 사용하기
# ---------------------------

# 파이썬 ORM 라이브러리 중 가장 많이 사용하는 SQLAlchemy를 사용해 보자.
# 이와 더불어 파이썬 모델을 이용해 테이블을 생성하고 컬럼을 추가하는 등의 작업을 할 수 있게
# 해주는 Flask-Migrate 라이브러리도 사용해 보자.

# ----------------------------
# 설치
# ----------------------------

# (myproject) c:\projects\myproject>pip install flask-migrate

# Flask-Migrate 라이브러리를 설치하면 SQLAlchemy도 함께 설치되므로
# myproject 가상 환경에서 다음 명령을 수행하여 Flask-Migrate 라이브러리를 설치하자.

# =============================================================

import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
# SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소이고
# SQLALCHEMY_DATABASE_URI 설정에 의해 SQLite 데이터베이스가 사용되고
# 데이터베이스 파일은 프로젝트 홈 디렉터리 바로 밑에 pybo.db 파일로 저장된다.

SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트를 처리하는 옵션이다.
# 이 옵션은 파이보에 필요하지 않으므로 False로 비활성화하자.

SECRET_KEY = "dev"          # 2-10 푬 모듈로 데이터 검증 더 쉽게 하기 부분에서 추가되는 코드







# 데이터베이스 관리 명령어 정리하기

# flask db migrate => 모델을 새로 생성하거나 변경할 때 사용 (실행하면 작업파일이 생성된다.)

# flask db upgrade => 모델의 변경 내용을 실제 데이터베이스에 적용할 때 사용
# (위에서 생성된 작업파일을 실행하여 데이터베이스를 변경한다.)

# 2-10 폼 모듈로 데이터 검증 더 쉽게 하기 --------------------------------------------
# 명령 프롬프트에서 Flask-WTF 라이브러리 설치

# (myproject) c:\projects\myproject> pip install flask-wtf

# -------------------------------------------------------------------------------