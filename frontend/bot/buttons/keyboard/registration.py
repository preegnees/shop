from aiogram import types
from consts.buttons_and_handlers import *

email_add = types.KeyboardButton(add_email)
email_not = types.KeyboardButton(refuse)

btns_registr = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btns_registr.add(email_add).insert(email_not)
