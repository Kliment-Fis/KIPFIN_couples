from bs4 import BeautifulSoup as BS
from requests import get
import telebot
from config import Tocken


def serch():
# поиск pdf документа с расписанием
	url = 'http://www.fa.ru/org/spo/kip/Pages/lesson_schedule.aspx'
	page = get(url)
	soup = BS(page.text, 'html.parser')
	return 'http://www.fa.ru' + soup.find('a', {'class':'block-item'}).get('href')

def write():
	with open('расписание.pdf', 'wb') as file:
		file.write(get(serch()).content)


bot = telebot.TeleBot(Tocken)

@bot.message_handler(commands=['start'])
def hello(msg):
	bot.send_message(msg.chat.id, 'Привет, если тебе нужно расписание напиши /couples')

@bot.message_handler(commands=['couples'])
def send(msg):
	write()
	with open('расписание.pdf', 'rb') as file:
		bot.send_document(msg.chat.id, file)

@bot.message_handler(commands=['secret'])
def dowland(msg):
	write()



bot.polling()