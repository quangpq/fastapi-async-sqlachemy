from typing import Optional

from .base import DateTime, CamelModel, ORMModel


# Shared properties
class NoteBase(CamelModel):
    title: str
    note: str
    updated_at: Optional[DateTime] = None


# Properties to receive on item creation
class NoteCreate(NoteBase):
    pass


# Properties to receive on item update
class NoteUpdate(NoteBase):
    id: int


class NoteInDBBase(NoteBase):
    pass


# Properties to return to client
class Note(NoteInDBBase, ORMModel):
    id: int
    created_at: DateTime
