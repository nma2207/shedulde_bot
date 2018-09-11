import telebot

bot = telebot.TeleBot('686183580:AAFysA0Ny3B3H2y7bZ11nblzJgWQu64yg9g')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello am bot! Marat bot")
    else:
        bot.send_message(message.from_user.id, "Sorry, I dont understand you")
# Обработчик команд '/start' и '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

 # Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

bot.polling(none_stop=True, interval = 10)