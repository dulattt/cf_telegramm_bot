from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import types


router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    kb = [
        [
            types.KeyboardButton(text="Предстоящие контесты"),
            types.KeyboardButton(text="Информация о пользователе")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )

    await message.answer("Привет!", reply_markup=keyboard)

