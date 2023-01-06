import logging
from logging import Formatter
from logging.handlers import RotatingFileHandler


def set_logger(logger, debugging=False, log_file: str = None):
    logger.setLevel(logging.DEBUG if debugging else logging.WARNING)
    formatter = Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s|%(funcName)s:%(lineno)d]'
    )

    if log_file is not None:
        handler = RotatingFileHandler(log_file,
                                      maxBytes=1000000,
                                      backupCount=90,
                                      encoding="utf-8")
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    uvicorn_logger = logging.getLogger("uvicorn")
    for h in uvicorn_logger.handlers:
        h.setFormatter(formatter)
        logger.addHandler(h)
