# FastAPI 회원 관리 API

FastAPI + SQLAlchemy를 사용한 간단한 회원 관리 REST API 프로젝트입니다.

## 기술 스택

- **Python 3.14**
- **FastAPI** 0.135.3
- **SQLAlchemy** 2.0
- **Pydantic** v2
- **SQLite** (로컬 개발용)
- **Uvicorn** (ASGI 서버)

## 프로젝트 구조

```
fastapi/
├── main.py               # FastAPI 앱 진입점
├── database/
│   ├── connection.py     # DB 연결 및 세션 관리
│   └── orm.py            # SQLAlchemy Base 클래스
└── user/
    ├── models.py         # User ORM 모델
    ├── request.py        # 요청 스키마 (Pydantic)
    ├── response.py       # 응답 스키마 (Pydantic)
    └── router.py         # 회원 관련 API 라우터
```

## 설치 및 실행

### 1. 가상환경 생성 및 활성화

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 2. 패키지 설치

```bash
pip install fastapi sqlalchemy uvicorn pydantic
```

### 3. 서버 실행

```bash
uvicorn main:app --reload
```

서버가 실행되면 `http://localhost:8000`에서 접근 가능합니다.

## API 문서

서버 실행 후 아래 주소에서 Swagger UI를 통해 API를 테스트할 수 있습니다.

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API 엔드포인트

| Method | URL | 설명 |
|--------|-----|------|
| GET | `/users` | 전체 회원 목록 조회 |
| GET | `/users/search?name=&job=` | 회원 검색 (name, job 조건) |
| GET | `/users/{user_id}` | 단일 회원 조회 |
| POST | `/users/user` | 회원 추가 |
| PATCH | `/users/{user_id}` | 회원 정보 수정 (job) |
| DELETE | `/users/{user_id}` | 회원 삭제 |

### 요청/응답 예시

**회원 추가 (POST /users/user)**

```json
// Request Body
{
  "name": "alex",
  "job": "developer"
}

// Response (201 Created)
{
  "id": 1,
  "name": "alex",
  "job": "developer",
  "created_at": "2026-04-09T10:00:00"
}
```

**회원 정보 수정 (PATCH /users/{user_id})**

```json
// Request Body
{
  "job": "designer"
}
```
