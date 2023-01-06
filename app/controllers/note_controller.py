from typing import List

from fastapi.logger import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.models import Note
from app.utils import helpers


class DuplicateNameError(RuntimeError):
    def __str__(self, *args, **kwargs):
        return "The name has been registered"


async def get_by_id(db: AsyncSession, note_id: int) -> Note:
    note = await helpers.execute_stmt(db, select(Note).filter_by(id=note_id), first_only=True)
    if note is None:
        raise RuntimeError("Note not found")
    return note


async def get_all(db: AsyncSession) -> List[Note]:
    notes = await helpers.execute_stmt(db, select(Note))
    if notes is None:
        return []
    return notes


async def create(db: AsyncSession, data: schemas.NoteCreate) -> Note:
    note = Note(
        title=data.title,
        note=data.note,
    )
    try:
        db.add(note)
        await helpers.flush_database(db)
    except Exception as e:
        logger.error(e)
        raise RuntimeError("Can not create note")

    return note
