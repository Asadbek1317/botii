import time
from states.persanaldata import PersanalData
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.default.buttons import contacktkey, choiskey
from aiogram import bot
from data.config import ADMINS

@dp.message_handler(Command('start'))
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu allaykum, <b>{message.from_user.full_name}</b>!\n"
                         
                         
                         f"Ushbu  botdan  foydalanish  uchun  <b>Ismingizni</b>  kiriting!")

    await PersanalData.name.set()


@dp.message_handler(state=PersanalData.name)
async def mess_name(message: types.Message, state: FSMContext):
    Name = message.text
    await state.update_data(big=Name)
    await message.answer('Va Telefon raqamingizni kiriting 👇', reply_markup=contacktkey)



    await PersanalData.phone.set()


@dp.message_handler(state=PersanalData.phone, content_types=types.ContentType.CONTACT)
async def get_con(message: types.contact, state: FSMContext):
    con = message.contact
    await state.update_data(sim=con)

    data = await state.get_data()
    namee = data.get('big')
    phonee = data.get('sim', ['phone_number'])

    #
    #do = await con.get_data()
    #di = do.get(['phone_number'])

    print(con['phone_number'])

    mes = "quydagi lar qabul qilindi \n"
    mes += f'Ismingiz = {namee} \n'
    mes += f"<a href='tg://user?id={phonee['user_id']}'>{namee}</a>\n"
    mes += f"tel raqamingiz - {phonee['phone_number']} \n"

    await message.answer("Siz Muvafaqqiyatli ro'yxatdan o'tdingiz \n"
                         "Kitoblarni topish uchun quydagilarni tanlang! ", reply_markup=choiskey)

    for adm in ADMINS:
        await dp.bot.send_message(adm, text='yangi bot foydalanuvchisi')
        time.sleep(5)

        await dp.bot.send_message(adm, mes)

        await state.finish()

