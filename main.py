from fastapi import FastAPI
from user.router import router

app = FastAPI()
app.include_router(router)


# @ -> Python 데코레이터: 파이썬 함수에 추가적인 기능을 부여하는 문법
# @app.get("/", status_code=200)
# def root_handler():
#     # return {"message": "Hello World"}
#     return {"ping": "pong"}

# @app.get("/hello",  status_code=status.HTTP_200_OK)
# def hello_handler():
#     return {"message": "Hello from FastAPI!"}
