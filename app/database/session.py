from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.settings import settings

database_uri = f"mysql+aiomysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?charset=utf8mb4"

engine = create_async_engine(database_uri, future=True, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine,
                                  autocommit=False,
                                  autoflush=False,
                                  expire_on_commit=False,
                                  class_=AsyncSession)
