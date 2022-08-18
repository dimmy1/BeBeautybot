import telebot
import config

from telebot import types
bot = telebot.TeleBot(config.Token)


@bot.message_handler(commands=['start'])
def welcome(message):


    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(text = 'Pestanas')
    item2 = types.KeyboardButton(text='Limpesa da pele')
    item3 = types.KeyboardButton(text='Depilação à laser')
    item4 = types.KeyboardButton(text='Unhas')
    item5 = types.KeyboardButton(text='Tattoo')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Olá, {0.first_name}, como posso ajudar?".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Pestanas':
            bot.send_message(message.chat.id, "Em que tipo de volume tem interesse?")
    elif message.text == 'Limpesa da pele':
        pass


bot.polling(none_stop=True, interval=0)