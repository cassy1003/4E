#-*- coding: utf-8 -*-
class Skype():

  class Attach():
    print 'Test Skype4Py!!'

  class Chat():
    Topic = u'帰らせマスターから貴方へ伝えたいこと'

    def SendMessage(self, msg):
      print msg

  Chats = [1]
  Chats[0] = Chat()
  Chat = Chat()
