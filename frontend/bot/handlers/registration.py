from utils import tengers
from buttons.keyboard.registration import types, btns_registr
from consts.buttons_and_handlers import *

class Registration:
    dp = tengers.get_dispatcher() 
    bot = tengers.get_bot()

    @dp.message_handler(commands=["start"])
    async def start(message: types.Message):
        await message.answer(text=answer_welcome, reply_markup=btns_registr)
    
    @dp.message_handler(text=add_email)
    async def adding_email(message: types.Message):
        await message.answer(text=answer_email_is_added)

    @dp.message_handler(text=refuse)
    async def is_refuse_email(message: types.Message):
        await message.answer(text=answer_is_refuse)

    
registration = Registration()