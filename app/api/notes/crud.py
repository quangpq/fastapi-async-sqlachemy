from typing import List

from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.logger import logger
from sqlalchemy.ext.asyncio import AsyncSession

from app import schemas
from app.api import deps, errors
from . import controller

router = APIRouter()


@router.get("/notes", response_model=List[schemas.Note], responses=errors.error_responses)
async def get_all(
        db: AsyncSession = Depends(deps.get_db),
):
    try:
        data = await controller.get_all(db)
    except Exception as e:
        logger.error(e)
        raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
    return data


@router.get("/notes/{note_id}", response_model=schemas.Note, responses=errors.error_responses)
async def get_by_id(
        note_id: int,
        db: AsyncSession = Depends(deps.get_db),
):
    try:
        data = await controller.get_by_id(db, note_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
    return data


@router.post("/notes", response_model=schemas.Note, responses=errors.error_responses)
async def create(
        body: schemas.NoteCreate,
        db: AsyncSession = Depends(deps.get_db),
):
    try:
        data = await controller.create_note(db, body)
    except Exception as e:
        logger.error(e)
        raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
    return data


@router.put("/notes", response_model=schemas.Note, responses=errors.error_responses)
async def update(
        body: schemas.NoteUpdate,
        db: AsyncSession = Depends(deps.get_db),
):
    try:
        data = await controller.update_note(db, body)
    except Exception as e:
        logger.error(e)
        raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
    return data


@router.delete("/notes/{note_id}")
async def delete(
        note_id: int,
        db: AsyncSession = Depends(deps.get_db),
):
    try:
        await controller.delete_note(db, note_id)
    except Exception as e:
        logger.error(e)
        raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
