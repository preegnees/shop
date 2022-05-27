from dotenv import dotenv_values
from . import parse
from loguru import logger
import sys


def _read_env() -> str:
    (path, err) = parse()
    if err != None:
        logger.error(err)
        sys.exit()
    return path


class Config():
    _path = None
    _env = None

    _token = None

    def __init__(self) -> None:
        path = _read_env()
        self._path = path
        self._env = dotenv_values(path)

        self._token = self._env["token"]

    def get_token(self) -> str:
        return self._token


config = Config()
