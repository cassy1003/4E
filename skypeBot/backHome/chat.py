# coding: utf-8
def getChatId(skype, title):
  for i in range(len(skype.Chats)):
    if skype.Chats[i].Topic == unicode(title, 'utf-8'):
      return i
