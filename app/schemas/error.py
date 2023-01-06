from typing import Dict, Optional

from pydantic import BaseModel

from app.core.contants import ErrorCode


class ErrorResponse(BaseModel):
    error: str
    code: Optional[ErrorCode] = None


class ErrorWithDataResponse(ErrorResponse):
    data: Dict
