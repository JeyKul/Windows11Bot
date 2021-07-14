import sys
import time
import telepot
import cookie
from telepot.loop import MessageLoop
import pdb

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and msg["text"].lower() == "news":
        # let the human know that the pdf is on its way        
        bot.sendMessage(chat_id, "preparing pdf of fresh news, pls wait..")
        file="/home/ubuntu/web/test.txt"

        # send the pdf doc
        bot.sendDocument(chat_id=chat_id, document=open(file, 'rb'))
    elif content_type == 'text':
        bot.sendMessage(chat_id, "sorry, I can only deliver news")
