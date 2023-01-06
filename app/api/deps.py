from typing import Generator

from app.database.session import SessionLocal


async def get_db() -> Generator:
    async with SessionLocal.begin() as db:
        yield db
