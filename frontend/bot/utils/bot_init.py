from aiogram import Bot, types
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from .config import config

class Tengers():
    _bot = None
    _dp = None
    _types = None

    def __init__(self) -> None:
        self._bot = Bot(token=config.get_token())
        self._dp = Dispatcher(self._bot)
        self._types = types

    def run(self) -> None:
        executor.start_polling(dispatcher=self._dp, skip_updates=True)

    def get_bot(self) -> aiogram.Bot:
        return self._bot

    def get_dispatcher(self) -> aiogram.Dispatcher:
        return self._dp

    def get_types(self) -> aiogram.types:
        return self._types


tengers = Tengers()
