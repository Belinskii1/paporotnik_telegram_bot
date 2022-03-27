from telegram import ReplyKeyboardMarkup

menu_unswers = [
    'А вот наше меню. Рекомендуем рыбу на пару',
    'У нас свежие десерты каждый день',
    'Только у нас карельские калитки'
]

main_menu_buttoms = ReplyKeyboardMarkup([[
        'Меню', 'Доставка'],
        ['Фуршеты', 'Банкеты'],
        ['Отзывы','Контакты'
    ]], resize_keyboard=True)

