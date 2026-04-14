import anyio
from contextlib import asynccontextmanager
from starlette.concurrency import run_in_threadpool

from fastapi import FastAPI
from user.router import router

# 쓰레드풀 크기 조정
@asynccontextmanager
async def lifespan(_):
    limiter = anyio.to_thread.current_default_thread_limiter()
    limiter.total_tokens = 200
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)

def aws_sync():
    # AWS S3에서 파일 다운로드
    return

# 동기함수를 비동기로 실행하는 핸들러
@app.get("/async")
async def async_handler():
    # AWS S3에서 파일 다운로드
    await run_in_threadpool(aws_sync)
    return {"message": "Async handler completed"}