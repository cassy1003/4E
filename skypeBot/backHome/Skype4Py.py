#-*- coding: utf-8 -*-
class Skype():
  print 'skype'

  class Attach():
    print 'Attach'

  class Chat():
    Topic = u'帰らせマスターから貴方へ伝えたいこと'
    Topic = Topic.encode('utf-8')

    def SendMessage(self, msg):
      print msg

  Chats = [1]
  Chats[0] = Chat()

  #class onMessageStatus():
    #return argv[1], arv[2]
