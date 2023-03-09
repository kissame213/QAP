import telebot
from config import keys, TOKEN
from extensions import APIException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты цену которой Вы хотите узнать> " \
           "<имя валюты в которой надо узнать цену первой валюты> " \
           "<количество первой валюты> \n Посмотреть список всех доступных валют: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise APIException('Неверное количество параметров')

        asset_id_base, asset_id_quote, amount = values
        total_base = CurrencyConverter.get_price(asset_id_base, asset_id_quote, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f'Цена {amount} {asset_id_base} в {asset_id_quote} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()