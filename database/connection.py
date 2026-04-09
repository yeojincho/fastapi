# SQLAlchemy를 이용해서 DB와 연결하는 코드
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 데이터베이스 접속
DATABASE_URL = "sqlite:///./local.db" # 현재 경로에 파일 형태로 DB 생성

# 엔진(Engine) : DB와의 접속을 관리하는 객체
engine = create_engine(DATABASE_URL, echo=True) # echo: 실제 쿼리 출력(주로 개발할때 True)

# 세션(Session)
SessionFactory = sessionmaker(
    bind=engine, 
    # 데이터를 어떻게 다룰지 조정하는 옵션(다 꺼두고 쓰는게 안전할듯)
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

# SQLAlchemy 세션을 주입하는 함수
def get_session():
    session = SessionFactory()
    
    try:
        yield session
    finally:
        session.close()




