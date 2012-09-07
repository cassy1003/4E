#-*- coding: utf-8 -*-
from datetime import datetime
import time

def call(skype, chat_id, title):
  while(True):
    now = datetime.now()
    if (skype.Chats[chat_id].Topic == title):

      if (now.second == 0):
        if (now.hour == 9):
          if (now.minute == 30):
            skype.Chats[chat_id].SendMessage(now.strftime('おはよーさん！%m月%d日が始まんで！今日も１日きばっていこやっ(flex)'))
            time.sleep(10)
          elif (now.hour == 21):
            if (now.minute > 50):
              skype.Chats[chat_id].SendMessage(now.strftime('%M分'))
              time.sleep(10)
            elif (now.minute >= 30 & now.minute % 10 == 0):
              leftTime = 60 - now.minute
              message = '22時まであと' + str(leftTime) + '分やで！？'
              skype.Chats[chat_id].SendMessage(message)
              time.sleep(10)
          elif (now.hour == 22):
            if (now.minute == 0):
              skype.Chats[chat_id].SendMessage(now.strftime('%H時になったで！おつかれさん！そろそろ帰ってやー(bow)'))
              time.sleep(10)
            elif (now.minute % 10 == 0):
              skype.Chats[chat_id].SendMessage(now.strftime('%H時を%M分過ぎてもうたで！はよ帰ってや！(envy)'))
              time.sleep(10)
          elif (now.hour == 23):
            if (now.minute == 0):
              skype.Chats[chat_id].SendMessage(now.strftime('%H時やで！こんな時間までおるん！？もうお前なんて知らんわ(punch)'))
              time.sleep(10)
    else:
      chat_id = getChatId()
