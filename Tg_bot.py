import telebot
from config import keys, TOKEN
from extensions import ConventerV, ConvertionException



bot = telebot.TeleBot(TOKEN)






@bot.message_handler(commands=['start', 'help'])
def hello(message: telebot.types.Message):
    text = ('Чтобы начать работу, введите команду боту в следующем формате: \n <имя валюты> \
<в какую валюту перевести>\
<количество переводимой валюты>\nУвидеть список всех доступных валют: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys:
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):

    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров')

        quote, base, amount = values  # что покупаем, валюта в которой покупаем, кол-во
        total_base = ConventerV.convertCon(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'цена {amount} {quote} в {base} - {total_base} '
        bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)
