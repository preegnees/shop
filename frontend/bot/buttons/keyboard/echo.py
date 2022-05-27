from aiogram import types

b1 = types.KeyboardButton("поделить номером телефона", request_contact=True)
b2 = types.KeyboardButton("поделится местоположением", request_location=True)

kb_cli = types.ReplyKeyboardMarkup(resize_keyboard=True)

kb_cli.add(b1).insert(b2)
