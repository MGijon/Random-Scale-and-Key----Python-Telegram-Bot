import telebot
import random

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

# KEYS
NOTES = ["C", "C\#", "D", "D\#", "E", "F", "F\#", "G", "G\#", "A", "A\#", "B"]
# SCALES
SCALES = ["Mayor Scale", "Minor Scale", "Dorian", "Frigian", "Lidian", "Mixolidian", "Locrian"]


@bot.message_handler(commands = ['start'])
def obterid(message):
    chat_id = message.chat.id
    print(chat_id)

@bot.message_handler(commands = ['Key'])
def returnRandomScale(message):
    '''
    Returns a random key
    :param message:
    :return: a random key
    '''
    ind = random.randint(0, 11)
    bot.reply_to(message, NOTES[ind])

@bot.message_handler(commands = ['scale'])
def returnRandomScale(message):
    '''
    Returns a random scale
    :param message:
    :return: a random scale
    '''
    ind = random.randint(0, len(SCALES))
    bot.reply_to(message, SCALES[ind])

@bot.message_handler(commands = ['all'])
def randomAll(message):
    '''
    Returns a random scale and a random key
    :param message:
    :return: random scale in a random key
    '''
    ind1 = random.randint(0, 1)
    ind2 = random.randint(0, len(SCALES))
    bot.reply_to(message, NOTES[ind1] + SCALES[ind2])

bot.polling(none_stop = False, interval = 0, timeout = 20)