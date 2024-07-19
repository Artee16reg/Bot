from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command


from keyboards import kb
from lexicon import text_for_bot

router = Router()

LOKLE_BD = {}

# TODO нада состояния придумать, когда юзер будет тыкать в эти 4 ебане кнопки
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        text_for_bot.greet.format(name=msg.from_user.full_name),
        reply_markup=kb.inline_menu,
    )


@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("БОТ будет записывать Доходы и расходы")


@router.callback_query(F.data == "money_income")
async def add_money_income(callback: CallbackQuery):
    if callback.message.text != "Запись дохода":
        await callback.message.edit_text(
            text="Запись дохода",
            reply_markup=callback.message.reply_markup,
        )
    await callback.answer()


@router.callback_query(F.data == "waste_of_money")
async def waste_of_money(callback: CallbackQuery):
    if callback.message.text != "Запись расхода":
        await callback.message.edit_text(
            text="Запись расхода",
            reply_markup=callback.message.reply_markup,
        )
    await callback.answer()


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
