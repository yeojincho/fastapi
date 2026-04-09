# 요청 본문의 데이터 형식 관리

from pydantic import BaseModel, Field

# 사용자 추가시 데이터 형식
class UserCreateRequest(BaseModel):
    name: str = Field(..., max_length=10, min_length=2)
    job: str

# 사용자 정보 수정시 데이터 형식
class UserUpdateRequest(BaseModel):
    job: str