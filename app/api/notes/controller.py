from datetime import datetime
from typing import List

from fastapi.logger import logger
from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.controllers import note_controller
from app.models import Note
from app.utils import helpers


async def get_by_id(db: AsyncSession, note_id: int) -> schemas.Note:
    data = await note_controller.get_by_id(db, note_id)
    return data


async def get_all(db: AsyncSession) -> List[schemas.Note]:
    data = await note_controller.get_all(db)
    return parse_obj_as(List[schemas.Note], data)


async def create_note(db: AsyncSession, data: schemas.NoteCreate) -> Note:
    return await note_controller.create(db, data)


async def update_note(db: AsyncSession, data: schemas.NoteUpdate) -> Note:
    note = await note_controller.get_by_id(db, data.id)

    try:
        note.title = data.title
        note.note = data.note
        note.updated_at = datetime.now()

        await helpers.flush_database(db)
    except Exception as e:
        logger.error(e)
        raise RuntimeError("Can not update note")

    return note


async def delete_note(db: AsyncSession, note_id: int):
    note = await note_controller.get_by_id(db, note_id)

    try:
        await db.delete(note)
        await helpers.flush_database(db)
    except Exception as e:
        logger.error(e)
        raise RuntimeError("Can not delete the note")


def _validate_data(data: schemas.NoteBase):
    data.title = data.title.strip()
    if len(data.title) < 2:
        raise RuntimeError("The name is too short")

    if len(data.title) > 254:
        raise RuntimeError("The name is too long")
