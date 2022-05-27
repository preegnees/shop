from utils import tengers

class Echo:
    dp = tengers.get_dispatcher()
    @dp.message_handler()
    async def echo_send(message: tengers.get_types().Message):
        await message.answer(message.text)

echo = Echo()