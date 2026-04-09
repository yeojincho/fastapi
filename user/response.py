# 응답 데이터의 형식 관리

# 형식을 관리하는 이유
# 1) 클라이언트에게 잘못된 데이터를 넘기지 않기 위해
# 2) 보내면 안되는 민감데이터 유출을 방지

from datetime import datetime
from pydantic import BaseModel, Field

class UserResponse(BaseModel):
    id: int
    name: str
    job: str
    created_at: datetime