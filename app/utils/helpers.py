import asyncio
import json
from functools import partial, wraps
from typing import List, Optional, Callable, Any

from fastapi import BackgroundTasks, Request
from fastapi.logger import logger
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession


class MockBackgroundTasks(BackgroundTasks):
    def add_task(self, func: Callable, *args: Any, **kwargs: Any) -> None:
        func(*args, **kwargs)


async def execute_stmt(db: AsyncSession, stmt, first_only=False):
    result = await db.execute(stmt)
    if first_only:
        return result.scalar_one_or_none()
    return result.scalars().all()


def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)

    return run


async def flush_database(db: AsyncSession):
    try:
        await db.flush()
    except Exception as e:
        await db.rollback()
        raise RuntimeError(e)


async def commit_database_raise(db: AsyncSession):
    try:
        await db.commit()
    except Exception as e:
        await db.rollback()
        raise RuntimeError(e)


async def commit_database(db: AsyncSession):
    try:
        await commit_database_raise(db)
    except Exception as e:
        logger.error(e)


def get_base_url(request: Request):
    return f"https://{request.url.netloc}".rstrip('/')


def get_full_url(host: str, path: Optional[str]) -> Optional[str]:
    if path is None:
        return None
    return f"{host}{path}"


def models2dict(items: Optional[List[BaseModel]]) -> List[dict]:
    if items is None:
        return []
    return [item.dict(by_alias=True) for item in items]


def model2dict(item: Optional[BaseModel]) -> Optional[dict]:
    if item is None:
        return None
    return item.dict(by_alias=True)


def model2json(item: Optional[BaseModel]) -> Optional[str]:
    if item is None:
        return None
    return item.json(by_alias=True)


def parse_json_array(v):
    if isinstance(v, list):
        return v
    if not isinstance(v, str):
        return []

    text = v.strip()
    if len(text) < 1:
        return []

    try:
        arr = json.loads(v)
    except Exception as e:
        print(e)
        return []

    if not isinstance(arr, list):
        return []

    return arr
