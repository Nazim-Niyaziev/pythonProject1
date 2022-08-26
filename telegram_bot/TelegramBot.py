import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        f"Welcome, {message.chat.username}, to get started, enter the command to the bot in the format:\n<currency name> \
        <what currency to convert?> \
        <the amount of the transferred currency>.\nView a list of available currencies: /values")


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Available currency:"
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Enter valid data!')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'User error.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Failed to process command.\n{e}')
    else:
        text = f'{amount} {quote} cost {str("%.2f" % (float(total_base) * float(amount)))} {base}s'
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['voice'])
def resp_audio(message):
    bot.send_message(message.chat.id, "I can't hear your voice.")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, "Don't pic, only text!")


bot.polling()
