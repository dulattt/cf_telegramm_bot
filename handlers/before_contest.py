from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message
from cf import get_upcoming_contest, update_upcoming_contest


router = Router()


@router.message(Text("Предстоящие контесты"))
async def cmd_start(message: Message) -> None:
    for el in get_upcoming_contest.get():
        await message.answer(el)


@router.message(Command("update_contests"))
async def cmd_update(message: Message) -> None:
    update_upcoming_contest.main()
    await message.answer("Предстоящие контесты обновлены!")
