from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base_class import Base


class Note(Base):
    __tablename__ = 'notes'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[Optional[datetime]] = mapped_column()
    title: Mapped[str] = mapped_column(String(256))
    note: Mapped[Optional[str]] = mapped_column(Text())

    # refresh server default values
    __mapper_args__ = {"eager_defaults": True}
