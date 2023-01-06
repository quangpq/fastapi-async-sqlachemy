from datetime import datetime
from typing import Optional
from .base import CamelModel


# Shared properties
class NoteBase(CamelModel):
    title: str
    note: str
    updated_at: Optional[datetime]


# Properties to receive on item creation
class NoteCreate(NoteBase):
    pass


# Properties to receive on item update
class NoteUpdate(NoteBase):
    id: int


class NoteInDBBase(NoteBase):
    pass


# Properties to return to client
class Note(NoteInDBBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
