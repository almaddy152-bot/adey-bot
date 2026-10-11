import telebot

TOKEN = 'أدخل_توقن_البوت_هنا'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'أهلاً بك! البوت يعمل بنجاح 24/7 🚀')

bot.polling()
