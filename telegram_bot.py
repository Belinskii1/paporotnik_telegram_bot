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
    buttons = ReplyKeyboardMarkup([[
        'Суп-солянка со свинной рулькой', 'Тыквенный суп'], 
        ['Куриный бульон с домашней лапшой', 'Уха из Лосося и судака'],
        ['Копченый борщ со свинными ребрышками и языком', 'вернуться в "Меню"'
    ]], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text = 'Супы на любой вкус',
        reply_markup=buttons
    )


def get_menu(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([[
        'Супы', 'Салаты', 'Основные блюда'],
        ['Закуски', 'Гарниры', 'Напитки'],
        ['Десерты', 'Торты', 'Главное меню'
    ]], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id,
        text = random.choice(menu_unswers),
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
