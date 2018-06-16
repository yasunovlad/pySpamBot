import telebot

TOKEN = 'WhAt'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'send_ads'])
def get_started(msg):
    bot.send_message(msg.chat.id, text='Привет')
def send_ads(msg):
    bot.send_message(msg.chat.id, text="t.me/pepe_lp ")
    bot.send_message(msg.chat.id, text="Статьи о Михаиле Светове идут в комплекте")

bot.polling()
