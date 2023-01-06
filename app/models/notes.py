from sqlalchemy import (Column, Integer, String, Text, TIMESTAMP)
from sqlalchemy.sql import text

from app.database.base_class import Base


class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, nullable=True)
    title = Column(String(256), nullable=False)
    note = Column(Text(), nullable=True)

    # refresh server default values
    __mapper_args__ = {"eager_defaults": True}
