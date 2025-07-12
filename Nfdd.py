import telebot
from selenium import webdriver
import time

bot = telebot.TeleBot("7727202824:AAH5jLe579GGf2gNOrmGf8AqUcIC_n77UcI")

@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.reply_to(msg, "👋 TikTok View Booster Bot!\nলিংক পাঠাও: ")

@bot.message_handler(func=lambda m: "tiktok.com" in m.text)
def boost_view(msg):
    url = msg.text
    bot.send_message(msg.chat.id, "⏳ View boosting শুরু হচ্ছে...")
    
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    for i in range(5):
        driver.get(url)
        time.sleep(10)
        driver.refresh()

    driver.quit()
    bot.send_message(msg.chat.id, "✅ View Boosted!")

bot.polling()
