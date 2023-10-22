from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

sen = ReplyKeyboardRemove()

contacktkey = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📞 telefon raqam', request_contact=True)

        ]
    ],
    resize_keyboard=True
)

choiskey = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="electron kitoblar"),
            KeyboardButton(text="audio kitoblar")
        ]
    ], resize_keyboard=True
)