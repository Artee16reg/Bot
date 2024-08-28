from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

from keyboards import kb
from lexicon import text_for_bot

router = Router()
storage = MemoryStorage()
LOKLE_BD = {}

bd = {"money_income": 0, "waste_of_money": 0}


# TODO I need to change variable name
# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM для инлайн кнопок (расход\доход)
class FSM_Money(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодействия с пользователем
    worke = State()
    money_income = State()
    waste_of_money = State()


@router.message(Command("start"), StateFilter(default_state))
async def start_handler(message: Message):
    await message.answer(
        text_for_bot.greet.format(name=message.from_user.full_name),
        reply_markup=kb.inline_menu,
    )


@router.message(Command("help"), StateFilter(default_state))
async def process_help_command(message: Message):
    await message.answer("БОТ будет записывать Доходы и расходы")


# Сработает после нажатия кнопки в меню (Финанасы)
@router.callback_query(F.data == "FSM_mone_waste")
async def fsm_mone_waste(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Финансы/вы в состоянии FSM_Money.worke", reply_markup=kb.kb_money_waste
    )
    await state.set_state(FSM_Money.worke)
    await callback.message.delete()


# Хендлер реагирует на нажатие инлайн кнопки money_income
@router.callback_query(F.data == "money_income")
async def add_money_income(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Введите число")
    await state.set_state(FSM_Money.money_income)
    await callback.answer()


# Хендлер реагирует на нажатие инлайн кнопки waste_of_money
@router.callback_query(F.data == "waste_of_money")
async def waste_of_money(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Введите число")
    await state.set_state(FSM_Money.waste_of_money)
    await callback.answer()


# Хендлер реагирует на нажатие инлайн кнопки celect_money_income
@router.callback_query(F.data == "celect_money_income")
async def celect_money_income(callback: CallbackQuery):
    await callback.message.answer(text=f"Ваш доход {bd['money_income']}")
    await callback.answer()


# Хендлер реагирует на нажатие инлайн кнопки celect_waste_of_money
@router.callback_query(F.data == "celect_waste_of_money")
async def celect_waste_of_money(callback: CallbackQuery):
    await callback.message.answer(text=f"Ваш доход {bd['waste_of_money']}")
    await callback.answer()


# Этот хендлер ловит цифру в состоянии FSM_Money.money_income
# TODO Сюда можно мб сразу добавить и на расход цифру
@router.message(StateFilter(FSM_Money.money_income))
async def add_money_income_num(message: Message, state: FSMContext):
    if str(
        message.text
    ).isdigit():  # TODO Разобрать message.text.isdigit() поч так не работает
        bd["money_income"] += int(message.text)
        print(bd)
        await message.answer(
            text=f"Вы ввели даходы + {message.text}", reply_markup=kb.kb_money_waste
        )
        await state.set_state(FSM_Money.worke)
    else:
        await message.answer(text="ДАлбаеб число введи, пока не введешь не отьебусь")


# Этот хендлер ловит цифру в состоянии FSM_Money.waste_of_money
@router.message(StateFilter(FSM_Money.waste_of_money))
async def add_waste_of_money(message: Message, state: FSMContext):
    if str(
        message.text
    ).isdigit():  # TODO Разобрать message.text.isdigit() поч так не работает
        bd["waste_of_money"] += int(message.text)
        print(bd)
        await message.answer(
            text=f"Вы ввели расходы - {message.text}", reply_markup=kb.kb_money_waste
        )

        await state.set_state(FSM_Money.worke)
    else:
        await message.answer(text="ДАлбаеб число введи, пока не введешь не отьебусь")


# Хендлер выхода из состояния FSM_Money.worke
@router.callback_query(F.data == "exit")
async def exitexit_the_FSM_Money(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(
        text_for_bot.greet.format(name=callback.from_user.full_name),
        reply_markup=kb.inline_menu,
    )
    await callback.message.delete()


# Этот хендлер отвечает на все оставшийся сообщения
@router.message()
async def message_handler(message: Message):
    await message.answer(f" это эхо {message.text}")
