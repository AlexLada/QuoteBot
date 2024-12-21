import telebot
import requests


API_TOKEN = '7879823801:AAHeU3iRKcVtLaaCt_BPPAJyd1bVjQgjzTw'

# Создаем экземпляр бота
bot = telebot.TeleBot(API_TOKEN)

# Функция для получения случайной цитаты
def get_random_quote():
    response = requests.get('https://zenquotes.io/api/random')
    if response.status_code == 200:
        quote = response.json()[0]  # Получаем первый элемент списка
        return f"{quote['q']} — {quote['a']}"
    else:
        return "Не удалось получить цитату. Попробуйте позже."

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, который отправляет случайные цитаты. Отправьте команду /quote, чтобы получить цитату.")

# Обработчик команды /quote
@bot.message_handler(commands=['quote'])
def send_quote(message):
    quote = get_random_quote()
    bot.reply_to(message, quote)

# Запускаем бота
bot.infinity_polling()
