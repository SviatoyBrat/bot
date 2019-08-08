# -*- coding: utf-8 -*-
#import config
import telebot

bot = telebot.TeleBot('923067513:AAHnP-MdT0sE0qGR2eFK3yl3k_jE_0UIOCg')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Это всё хорошо , но ты пидор")
    #bot.reply_to(message, "Это всё хорошо , но ты пидор"

if __name__ == '__main__':
     bot.polling(none_stop=True)