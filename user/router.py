from fastapi import APIRouter, Path, Query, status, HTTPException, Depends
from sqlalchemy import select, delete
from database.connection import get_session
from user.request import UserCreateRequest, UserUpdateRequest
from user.response import UserResponse
from user.models import User


router = APIRouter(prefix="/users", tags=["회원 관리"])


# 임시 전체 유저 데이터
users = [
        {"id": 1, "name": "alex", "job": "student"},
        {"id": 2, "name": "bob", "job": "sw engineer"},
        {"id": 3, "name": "chris", "job": "barista"},
    ]

@router.get("",
            status_code=status.HTTP_200_OK, 
            summary="전체 회원 목록 조회 API",
            response_model=list[UserResponse]
            )
def get_users_handler(
    session = Depends(get_session) # Depends: FastAPI에서 의존성(get_session)을 자동 실행/주입/정리
):
    statement = select(User) # SELECT * FROM USER;
    result = session.execute(statement)
    users = result.scalars().all()  # scalars(): 첫번째 열의 데이터만, all(): 리스트변환
    return users


@router.get(
        "/search", 
        summary="회원 정보 검색 API",
        response_model=list[UserResponse],
        )
def search_user_handler(
    name: str | None = Query(None), 
    job:str | None = Query(None),
    session = Depends(get_session),
    ):
    if not name and not job:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="검색 조건이 없습니다."
        )
    stmt = select(User)
    if name:
        stmt = stmt.where(User.name == name)
    if job:
        stmt = stmt.where(User.job == job) # name 거쳐온거면 where 2번
    
    result = session.execute(stmt)
    users = result.scalars().all()
    return users



@router.get(
        "/{user_id}", 
        summary="단일 회원 조회 API",
        response_model=UserResponse
        )
# Path:경로에서 가져옴, ...: 필수값, ge: 이상(Greater than or Equal)
def get_user_handler(user_id: int = Path(..., ge=1, le=9999), 
                     session=Depends(get_session)
                     ):
    stmt = select(User).where(User.id == user_id)
    result = session.execute(stmt)
    user = result.scalar() # scalar(): 1개 | 0개

    if not user: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="회원를 찾을 수 없습니다."
        )
    return user


@router.post(
        "/user", 
        summary="회원 추가 API",
        response_model=UserResponse, 
        status_code=status.HTTP_201_CREATED
        )
def create_user_handler(body: UserCreateRequest, 
                        session = Depends(get_session)):
    new_user = User(name=body.name, job=body.job)
    session.add(new_user)
    session.commit() # DB에 반영(INSERT)
    session.refresh(new_user) # 반영된 행 읽어오기(SELECT)
    return new_user

    # new_user = {"id":len(users)+1, "name":body.name, "jop":body.job}
    # users.append(new_user)
    # return new_user

@router.patch(
        "/{user_id}", 
        summary="회원 정보 수정 API",
        response_model=UserResponse
        )
def update_user_handler(
    user_id: int, 
    body: UserUpdateRequest,
    session = Depends(get_session)
    ):
    stmt = select(User).where(User.id == user_id)
    result = session.execute(stmt)
    user = result.scalar() # scalar(): 객체 하나만

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="회원을 찾을 수 없습니다."
        )
    user.job = body.job # user는 세션에서 가져온 것이므로 session.add(user) 하지 않아도 됨
    session.commit() # UPDATE 쿼리로 DB 반영(UPDATE user SET job=? WHERE user.id = ?)
    session.refresh(user)
    return user


@router.delete(
    "/{user_id}", 
    summary="회원 삭제 API",
    status_code=status.HTTP_204_NO_CONTENT # 204_NO_CONTENT: 응답 메시지 반환 안되도록
    )
def delete_user_handler(user_id: int,
                        session = Depends(get_session)
                        ):
# 1) 곧바로 삭제
    stmt = delete(User).where(User.id == user_id)
    session.execute(stmt)
    session.commit()

# 2) 조회 후 삭제(조회해보고 없으면 없다고 알려줄수있음)
# with SessionFactory() as session:
#     stmt = select(User).where(User.id == user_id)
#     result = session.execute(stmt)
#     user = result.scalar()

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, 
#             detail="회원을 찾을 수 없습니다."
#         )
#     session.delete(user) # DELETE 쿼리로 DB 반영(DELETE FROM user WHERE user.id = ?)
#     # session.expunge(user) -> 세션에서 관리/추척 대상에서 제거해라
#     session.commit()

        