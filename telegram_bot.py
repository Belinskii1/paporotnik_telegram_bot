import os
from telegram import Bot, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import requests
import random
from dotenv import load_dotenv

from cafe_menu import menu_unswers, contacts, main_menu_buttoms

load_dotenv()

token = os.getenv('TOKEN')

updater = Updater(token)

chat_id = 288573595


def get_soups_menu(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([
        ['Суп-солянка со свинной рулькой', 'Тыквенный суп'], 
        ['Куриный бульон с домашней лапшой', 'Уха из Лосося и судака'],
        ['Копченый борщ со свинными ребрышками и языком', 'вернуться в "Меню"']
    ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text = 'Супы на любой вкус',
        reply_markup=buttons
    )


def get_salat_menu(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([
        ['Классический "цезарь"', 'Шар сельди под шубой'],
        ['Салат микс с куриным филе и копченым сыром', 'Овощной салат с яйцом пашот'],
        ['Теплый с салат с тигровыми креветками, лососем и авокадо'],
        ['Оливье с цесаркой и говяжьим языком', 'вернуться в "Меню"']
    ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text = 'Салаты для разогрева аппетита',
        reply_markup=buttons
    )


def get_menu(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([
        ['Супы', 'Салаты', 'Вторые блюда'],
        ['Закуски', 'Гарниры', 'Напитки'],
        ['Десерты', 'Торты', 'Главное меню']
    ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text = random.choice(menu_unswers),
        reply_markup=buttons
    )


def get_second_courses(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([
        ['Лапша в азиатском стиле', 'Свиные медальоны с картофельным ризотто'],
        [
            'Треска в кляре с овощным рататуем и соусом Тартар',
            'Бефстроганов на картофельных драниках'
        ],
        [
            'Судак на картофельном пюре с луковыми кольцами и соусом из креветок',
            'Утка конфи'
        ],
        ['Сёмга со стружкой из цукини', 'Отварное/гриль куриное филе с овощами'],
        ['Свиная вырезка на подушке из грибов и лука порея','вернуться в "Меню"']
    ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text = 'Наши изысканные вторые блюда',
        reply_markup=buttons
    )


def get_snacks(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([
        [
            'Карельская калитка с креветкой и авокадо',
            'Карельская калитка с картофельным ризотто'
        ],
        [
            'Закуска из сельди с маринованным луком и жареным хлебом',
            'Карельская калитка с жульеном'
        ],
        ['Тарелка с фермерскими сырами', 'Жаренный сыр с ягодным и цитрусовым соусом'],
        [
            'Карельская калитка со слабосолёным лососем и творожным сыром',
            'Чесночные ржаные гренки с соусом'
        ],
        [
            'Тигровые креветки в панировке с томатно-сливочным соусом',
            'вернуться в "Меню"'
        ]
    ], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text = 'Разнообразные закуски',
        reply_markup=buttons
    )
    

def get_main(update, context):
    chat = update.effective_chat
    buttons = main_menu_buttoms
    context.bot.send_message(
        chat_id=chat.id,
        text='Вы на главном меню',
        reply_markup=buttons
    )


def analyzed_command(update, context):
    chat = update.effective_chat
    if update.message.text == 'Меню' or update.message.text == 'вернуться в "Меню"':
        get_menu(update, context)
    elif update.message.text == 'Контакты':
        context.bot.send_message(chat_id=chat.id,text=contacts)
    elif update.message.text == 'Доставка':
        context.bot.send_message(chat_id=chat.id,text='Условия доставки и карта города')
    elif update.message.text == 'Сайт':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/74qcoq7Mot76gg') 
        context.bot.send_message(chat_id=chat.id, text='http://paporotnikkafe.ru')
    elif update.message.text == 'Мероприятия':
        context.bot.send_message(chat_id=chat.id,text='Проведем от дня рождения до свадьбы')
    elif update.message.text == 'Отзывы':
        context.bot.send_message(chat_id=chat.id,text='Здесь будут наши благодарные клиенты')
    elif update.message.text == 'Главное меню':
        get_main(update, context)
    elif update.message.text == 'Супы' or update.message.text == 'вернуться в "Супы"': 
        get_soups_menu(update, context)
    elif update.message.text == 'Суп-солянка со свинной рулькой':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/TAggR_duLTQhGQ') 
        context.bot.send_message(chat_id=chat.id, text='300руб')
    elif update.message.text == 'Тыквенный суп':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/b6cykIW3WbKmsw') 
        context.bot.send_message(chat_id=chat.id, text='250руб')
    elif update.message.text == 'Куриный бульон с домашней лапшой':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/IH3HZiFESVut_Q') 
        context.bot.send_message(chat_id=chat.id, text='230руб')
    elif update.message.text == 'Уха из Лосося и судака':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/9znsGXvnXxHHzw') 
        context.bot.send_message(chat_id=chat.id, text='400руб')
    elif update.message.text == 'Копченый борщ со свинными ребрышками и языком':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/NMN2yRMhH07Jfw') 
        context.bot.send_message(chat_id=chat.id, text='320руб')
    elif update.message.text == 'Салаты':
        get_salat_menu(update, context)
    elif update.message.text == 'Классический "цезарь"':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/eO1KzyvUfoWN3A') 
        context.bot.send_message(chat_id=chat.id, text='от 380руб')
    elif update.message.text == 'Шар сельди под шубой':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/N80QFCqBNwRljw') 
        context.bot.send_message(chat_id=chat.id, text='230руб')
    elif update.message.text == 'Салат микс с куриным филе и копченым сыром':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/OOdFlETuegnmng') 
        context.bot.send_message(chat_id=chat.id, text='350руб')
    elif update.message.text == 'Овощной салат с яйцом пашот':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/HMVguI7xsLYy7w') 
        context.bot.send_message(chat_id=chat.id, text='250руб')
    elif update.message.text == 'Теплый с салат с тигровыми креветками, лососем и авокадо':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/CF6-cu29ggWvIQ') 
        context.bot.send_message(chat_id=chat.id, text='450руб')
    elif update.message.text == 'Оливье с цесаркой и говяжьим языком':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/SFKvjCpB9NuMrQ')
        context.bot.send_message(chat_id=chat.id, text='290руб')
    elif update.message.text == 'Вторые блюда':
        get_second_courses(update, context)
    elif update.message.text == 'Лапша в азиатском стиле':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/cckg5oqLGHoyKA')
        context.bot.send_message(chat_id=chat.id, text='390руб')
    elif update.message.text == 'Свиные медальоны с картофельным ризотто':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/S87_gaD7i4lK7g')
        context.bot.send_message(chat_id=chat.id, text='500руб')
    elif update.message.text == 'Треска в кляре с овощным рататуем и соусом Тартар':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/6Fgga90sbLBfuQ')
        context.bot.send_message(chat_id=chat.id, text='400руб')
    elif update.message.text == 'Бефстроганов на картофельных драниках':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/y6AK-5Kv6o7Qqw')
        context.bot.send_message(chat_id=chat.id, text='520руб')
    elif update.message.text == 'Судак на картофельном пюре с луковыми кольцами и соусом из креветок':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/WU4P4Y0di_QZ-w')
        context.bot.send_message(chat_id=chat.id, text='450руб')
    elif update.message.text == 'Утка конфи':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/Wlk0lcO8WumxYA')
        context.bot.send_message(chat_id=chat.id, text='800руб')
    elif update.message.text == 'Сёмга со стружкой из цукини':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/WICRPAzYfRn4UQ')
        context.bot.send_message(chat_id=chat.id, text='700руб')
    elif update.message.text == 'Отварное/гриль куриное филе с овощами':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/ajcZhCwHRJDvsg')
        context.bot.send_message(chat_id=chat.id, text='340руб')
    elif update.message.text == 'Свиная вырезка на подушке из грибов и лука порея':
        context.bot.send_photo(chat.id, 'https://disk.yandex.ru/i/gaPTehTxciAwng')
        context.bot.send_message(chat_id=chat.id, text='450руб')
    elif update.message.text == 'Закуски':
        get_snacks(update, context)
    else:
        context.bot.send_message(chat_id=chat.id,text='Набери /start, чтобы начать')
    

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = main_menu_buttoms
    context.bot.send_message(
        chat_id=chat.id,
        text='Привет, {}! Рады видеть в нашем кафе "Папоротник"'.format(name),
        reply_markup=buttons
    )


updater.dispatcher.add_handler(CommandHandler('start', wake_up))

updater.dispatcher.add_handler(MessageHandler(Filters.text, analyzed_command))

updater.start_polling()
updater.idle() 
