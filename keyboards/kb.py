from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup # ReplyKeyboardRemove узнать нахуй я это юзал

# TO DO нада сделать кнопки, которые будут отправлять в бд даные о лавэ по классофикацуии.

menu = [
    [InlineKeyboardButton(text="📝Записать доход", callback_data="generate_text"),
    InlineKeyboardButton(text="📝 Записать расход", callback_data="generate_image"),],
    
    [InlineKeyboardButton(text="🖼 Посмотореть доход", callback_data="generate_text"),
    InlineKeyboardButton(text="🖼 Посмотореть расход", callback_data="generate_image"),],
    ]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])