from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


from keyboards import kb
from lexicon import text_for_bot

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        text_for_bot.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu
    )


@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
@router.message(F.text == "◀️ Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text_for_bot.menu, reply_markup=kb.menu)


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
