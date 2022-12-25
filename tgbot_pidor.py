import logging
import ENV
import pid_func
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOT TOKEN HERE'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=ENV.API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Yo, педрилки, поиграем! Регайтесь /regme")



@dp.message_handler()
async def echo(message: types.Message):
    if message.text == '/regme':

        await message.reply(pid_func.reg_user(str(message.from_user.id), message.from_user.username))

    if message.text == '/stata':
        await message.reply(pid_func.return_statistic())

    if message.text == '/pidoviktorina':
        await message.reply(pid_func.viktorina())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)