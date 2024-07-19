from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, BotCommand

# TO DO нада сделать кнопки, которые будут отправлять в бд даные о лавэ по классофикацуии.
inline_menu = [
    [InlineKeyboardButton(text="📝 Записать доход", callback_data="money_income"),
    InlineKeyboardButton(text="📝 Записать расход", callback_data="waste_of_money"),],
    
    [InlineKeyboardButton(text="🖼 Посмотореть доход", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Посмотореть расход", callback_data="generate_image"),],
    ]

inline_menu = InlineKeyboardMarkup(inline_keyboard=inline_menu)
