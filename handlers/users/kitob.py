from aiogram import types
from states.persanaldata import PersanalData
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import Message
from loader import dp
from keyboards.inline import inlinekey1, inlinekeymm

@dp.message_handler(text_contains="electron")
async def bot(message: Message):
    await message.answer('Siz quyidagi kitoblarni topishingiz mumkin !', reply_markup=inlinekey1)


@dp.message_handler(text_contains="audio")
async def bot(message: Message):
    await message.answer('Siz quyidagi kitoblarni topishingiz mumkin !', reply_markup=inlinekeymm)
