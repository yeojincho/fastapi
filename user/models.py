from datetime import datetime
from sqlalchemy import Integer, String, DATETIME, func
from sqlalchemy.orm import Mapped, mapped_column
from database.orm import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32))
    job: Mapped[str] = mapped_column(String(32))
    created_at: Mapped[datetime] = mapped_column(DATETIME, server_default=func.now())

    


