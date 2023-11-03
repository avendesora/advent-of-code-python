from __future__ import annotations

import logging


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    c_handler = logging.StreamHandler()
    c_handler.setLevel(level)
    logger.addHandler(c_handler)

    return logger
