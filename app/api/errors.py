from typing import Any

from fastapi import HTTPException, status

from app.core.contants import ErrorCode
from app.schemas import ErrorResponse

error_responses = {
    422: {"model": ErrorResponse},
    400: {"model": ErrorResponse},
}


class CustomCodeException(HTTPException):
    def __init__(
            self,
            code: ErrorCode,
            detail: Any = None,
    ) -> None:
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
        self.code = code
