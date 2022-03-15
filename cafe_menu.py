from telegram import ReplyKeyboardMarkup

menu_unswers = [
    'А вот наше меню. Рекомендуем рыбу на пару',
    'У нас свежие десерты каждый день',
    'Только у нас карельские калитки'
]

contacts = (
    'САЙТ http://paporotnikkafe.ru',
    'ТЕЛЕФОН +7 (910) 429-29-69',
    'ПОЧТА info@paporotnikkafe.ru',
    'АДРЕС улица Ухова, 35, Солнечногорск, Московская область, Россия'
)


main_menu_buttoms = ReplyKeyboardMarkup([[
        'Меню', 'Доставка'],
        ['Фуршеты', 'Банкеты'],
        ['Отзывы','Контакты'
    ]], resize_keyboard=True)

