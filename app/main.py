from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.logger import logger
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api import notes, errors
from app.core.log import set_logger
from app.core.settings import settings
from app.database.session import SessionLocal, engine

set_logger(logger, settings.DEBUGGING)

app = FastAPI(
    title="FastAPI",
    version="1.0.0",
    openapi_url=f"{settings.API_STR}/openapi.json",
    docs_url=f"{settings.API_STR}/docs",
    redoc_url=None
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

notes.register_routers(app)


@app.exception_handler(errors.CustomCodeException)
async def custom_code_exception_handler(request, exc: errors.CustomCodeException):
    code = status.HTTP_400_BAD_REQUEST
    msg = str(exc.detail)
    if exc.status_code == 404:
        code = status.HTTP_404_NOT_FOUND
        msg = "Not found"

    return JSONResponse(
        status_code=code,
        content={"error": msg, "code": exc.code},
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    code = status.HTTP_400_BAD_REQUEST
    msg = str(exc.detail)
    if exc.status_code == status.HTTP_401_UNAUTHORIZED:
        code = status.HTTP_401_UNAUTHORIZED
    elif exc.status_code == status.HTTP_404_NOT_FOUND:
        code = status.HTTP_404_NOT_FOUND
        msg = "Not found"

    return JSONResponse(
        status_code=code,
        content={"error": msg},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    msg = ", ".join([f'{err["loc"]}: {err["msg"]}' for err in exc.errors()])
    return JSONResponse(content={"error": msg},
                        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


@app.on_event("shutdown")
async def shutdown_event():
    SessionLocal.close_all()

    # Close aiomysql connections
    await engine.dispose()
