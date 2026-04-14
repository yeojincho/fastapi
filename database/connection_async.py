# SQLAlchemy를 이용해서 DB와 연결하는 코드
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


# 데이터베이스 접속
DATABASE_URL = "sqlite+aiosqlite:///./local.db" # sqlite+aiosqlite: 같이 써야 비동기로 연결됨

# 엔진(Engine) : DB와의 접속을 관리하는 객체
async_engine = create_async_engine(DATABASE_URL, echo=True) # echo: 실제 쿼리 출력(주로 개발할때 True)

# 세션(Session)
AsyncSessionFactory = async_sessionmaker(
    bind=async_engine, 
    # 데이터를 어떻게 다룰지 조정하는 옵션(다 꺼두고 쓰는게 안전할듯)
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)

# SQLAlchemy 세션을 주입하는 함수
async def get_async_session():
    session = AsyncSessionFactory()
    
    try:
        yield session
    finally:
        await session.close()




