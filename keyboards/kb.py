from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_money_waste = [
    [
        InlineKeyboardButton(text="📝 Записать доход", callback_data="money_income"),
        InlineKeyboardButton(text="📝 Записать расход", callback_data="waste_of_money"),
    ],
    [
        InlineKeyboardButton(
            text="🖼 Посмотореть доход", callback_data="celect_money_income"
        ),
        InlineKeyboardButton(
            text="🖼 Посмотореть расход", callback_data="celect_waste_of_money"
        ),
    ],
    [InlineKeyboardButton(text="Назад", callback_data="exit")],
]

inline_menu = [
    [
        InlineKeyboardButton(text="Мое бабло", callback_data="FSM_mone_waste")
    ],  # После нажатия будет накинуто состояние FSM_Money()
    [
        InlineKeyboardButton(
            text="Еще что угодно", callback_data="И сюда что то для калбека"
        )
    ],
]

inline_menu = InlineKeyboardMarkup(inline_keyboard=inline_menu)
kb_money_waste = InlineKeyboardMarkup(inline_keyboard=kb_money_waste)
