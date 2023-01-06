from enum import Enum


class ErrorCode(int, Enum):
    others = 0


class DateFormat(str, Enum):
    YmdHMS = "%Y-%m-%d %H:%M:%S"
