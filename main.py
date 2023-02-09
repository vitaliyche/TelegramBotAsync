from aiogram import *
from aiogram.types import *

TOKEN = "5606282206:AAEDjV9Bft5YnRBBMVeEWHE9JKLJ_wkpn5Y"
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def begin(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Connect to StarLink", callback_data="button")
    markup.add(button)

    await bot.send_message(message.chat.id, "Hi. I'm Elon", reply_markup=markup)

@dispatcher.callback_query_handler(lambda c: c.data=="button")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "You have successfully connected to StarLink")

@dispatcher.message_handler(content_types=['text'])
async def text(message: types.Message):

    if message.text.lower() == "hello":
        await bot.send_message(message.chat.id, "Glad to see you man")

    if message.text.lower() == "bye":
        await message.reply("Wait bro. We didn't even ride a Tesla")

executor.start_polling(dispatcher)