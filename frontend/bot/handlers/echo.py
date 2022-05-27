from utils import tengers
from buttons import types, kb_cli

class Echo:
    dp = tengers.get_dispatcher() 
    bot = tengers.get_bot()

    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await message.reply(text="hello", reply_markup=kb_cli)
    
    @dp.message_handler()
    async def other(message: types.Message):
        print(message.contact.phone_number)

        try:
            msg = message.reply_to_message.text # if replied
        except AttributeError:
            msg = 'not replied'
        
        print(msg)

        # не знаю как получить reply на мое сообщение

        await message.reply(message.contact.phone_number)
    
echo = Echo()