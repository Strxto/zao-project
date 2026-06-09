from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_menu_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Меню', callback_data='Menu')]
])

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Оформить заказ', callback_data='make an order'), InlineKeyboardButton(text='Расчет стоимости', callback_data='cost calculation')],
    [InlineKeyboardButton(text='Гайд - инструкция', callback_data='Guide')],
    [InlineKeyboardButton(text='Отзывы', callback_data='comments'), InlineKeyboardButton(text='Поддержка', url='t.me/zaodelivery'), InlineKeyboardButton(text='Наш канал', url='https://t.me/Zao_Delivery')],
    [InlineKeyboardButton(text='Отслеживание заказов', callback_data='status')]
])

comments_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Прочитать отзывы', callback_data='read comments'), InlineKeyboardButton(text='Оставить отзыв', callback_data='write comment')],
    [InlineKeyboardButton(text='Назад', callback_data='back')]
])

guide_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как зарегестрироваться на Poizon?', callback_data='how_to_reg')],
    [InlineKeyboardButton(text='Как подобрать размер обуви?', callback_data='how_to_find_size_shoes')],
    [InlineKeyboardButton(text='Как подобрать размер одежды?', callback_data='how_to_find_size_clothes')],
    [InlineKeyboardButton(text='Как скопировать ссылку на товар?', callback_data='how_to_find_item_link')],
    [InlineKeyboardButton(text='Назад', callback_data='back')]
])

how_to_reg_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Как скачать приложение?', callback_data='how_to_install')],
    [InlineKeyboardButton(text='Как зарегестрироваться в приложении?', callback_data='how_to_reg_in_app')],
    [InlineKeyboardButton(text='Назад', callback_data='back_to_guide_menu')]
])

how_to_back_to_install_and_reg_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_to_how_to_install')]
])

back_to_guide_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back_to_guide_menu')]
])
