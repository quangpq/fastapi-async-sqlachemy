from app.core.settings import settings
from . import crud


def register_routers(parent):
    parent.include_router(crud.router, prefix=f"{settings.API_STR}", tags=["notes"])
