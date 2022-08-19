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
def services(message):
    if message.chat.type == 'private':
        if message.text == 'Pestanas':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            subitem1 = types.KeyboardButton(text='1D')
            subitem2 = types.KeyboardButton(text='2D')
            subitem3 = types.KeyboardButton(text='3D')
            subitem4 = types.KeyboardButton(text='4D')
            subitem5 = types.KeyboardButton(text='Volume russo')
            subitem6 = types.KeyboardButton(text='Mega volume')
            subitem7 = types.KeyboardButton(text='Laminação')
            back = types.KeyboardButton(text='Voltar')

            markup.add(subitem1, subitem2, subitem3, subitem4, subitem5, subitem6, subitem7, back)

            bot.send_message(message.chat.id, "Em que tipo de volume tem interesse?".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
        elif message.text == 'Limpesa da pele':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            subitem1 = types.KeyboardButton(text='Informação')
            subitem2 = types.KeyboardButton(text='Preço')
            back = types.KeyboardButton(text='Voltar')


            markup.add(subitem1, subitem2, back)

            bot.send_message(message.chat.id, "Que tipo de informação precisa?".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
        elif message.text == 'Depilação à laser':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            subitem1 = types.KeyboardButton(text='Corpo todo')
            back = types.KeyboardButton(text='Voltar')


            markup.add(subitem1, back)

            bot.send_message(message.chat.id, "Que tipo de zona quer fazer?".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
        elif message.text == 'Unhas':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            subitem1 = types.KeyboardButton(text='Pedicure')
            subitem2 = types.KeyboardButton(text='Manicure')
            subitem3 = types.KeyboardButton(text='Pedicure e manicure')
            back = types.KeyboardButton(text='Voltar')


            markup.add(subitem1, subitem2, subitem3, back)

            bot.send_message(message.chat.id, "O que gostava de fazer?".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
        elif message.text == 'Tattoo':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            subitem1 = types.KeyboardButton(text='WhatsApp')
            subitem2 = types.KeyboardButton(text='Instagram')
            back = types.KeyboardButton(text='Voltar')


            markup.add(subitem1, subitem2, back)

            bot.send_message(message.chat.id, "Para obter mais informação, contacta-nos através:".format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
        elif message.text == 'Voltar':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton(text='Pestanas')
            item2 = types.KeyboardButton(text='Limpesa da pele')
            item3 = types.KeyboardButton(text='Depilação à laser')
            item4 = types.KeyboardButton(text='Unhas')
            item5 = types.KeyboardButton(text='Tattoo')

            markup.add(item1, item2, item3, item4, item5)

            bot.send_message(message.chat.id,
                             "{0.first_name}, parece que mudou de ideias ;)".format(message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)
        elif message.text == '1D':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton(text='WhatsApp')
            item2 = types.KeyboardButton(text='Instagram')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Preço:\n 1ª aplicação - 25€\n Man 4 sem - 25€\n Man 3 sem - 20€\n "
                                              "Man 2 sem - 15€\n "
                                              "para fazer marcação contacta-nos através:".format(message.from_user,
                                                                                                 bot.get_me()),
                             parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True, interval=0)