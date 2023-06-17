from aiogram import Router, F
from aiogram.filters import Text
from aiogram.types import URLInputFile
from aiogram.types import Message
from cf import get_user_info


router = Router()


@router.message(Text("Информация о пользователе"))
async def cmd_get_user_info(message: Message) -> None:
    await message.reply("Введите хэндл: ")


@router.message(F.text)
async def print_user_info(message: Message) -> None:
    p = get_user_info.Parser(str(message.text).strip())

    if p.get_status() == "failed":
        await message.answer(p.get_comment())
    else:
        img_url = URLInputFile(p.get_user_title_photo())
        await message.answer_photo(img_url)

        await message.answer(p.answer())
