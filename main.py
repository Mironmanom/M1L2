import telebot
    

bot = telebot.TeleBot('Token')

# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')

# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "Ха" * count_heh)
# 
@bot.message_handler(commands=['meaw'])
def send_meaw(message):
    bot.reply_to(message,'Мяу')
# Запуск бота
bot.polling()
