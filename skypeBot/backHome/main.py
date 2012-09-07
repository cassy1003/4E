# coding: utf-8

import Skype4Py, os, sys, glob, datetime, time
from call import call

skype = Skype4Py.Skype()
skype.Attach()

title = '帰らせマスターから貴方へ伝えたいこと'

chat_id = getChatId(skype, title)

def handler(msg, event):
    if event == u"RECEIVED":
        if msg.Chat.Topic == unicode(title, 'utf-8'):
            if msg.Body.startswith(u"@back"):
                item = msg.Body.split(' ')
                name = item[1]
                filename = "back_log/" + name + ".dat"
                if os.path.exists(filename):
                    file = open(filename, "a")
                    if len(item) >= 3:
                        file.write(item[2]+" "+item[3]+"\n")
                    else:
                        file.write(str(datetime.datetime.now())+"\n")
                    file.close()
                    msg.Chat.SendMessage(u"ほなね!お気をつけて(h)")
                else:
                    msg.Chat.SendMessage(u"そんなusernameおらへんで。@new username で新しく追加してなっ。")
            elif msg.Body.startswith(u"@new"):
                name = msg.Body.split(' ')[1]
                filename = "back_log/" + name + ".dat"
                if os.path.exists(filename):
                    msg.Chat.SendMessage(u"そのusernameの人、もういてはるわー(bow)")
                else:
                    file = open(filename, "w")
                    file.write("")
                    file.close()
                    msg.Chat.SendMessage(u"username登録したで(*)")
            elif msg.Body.startswith(u"@look"):
                item = msg.Body.split(' ')
                name = item[1]
                filename = "back_log/" + name + ".dat"
                if os.path.exists(filename):
                    lineList = [line for line in open(filename, "r")]
                    l = len(lineList)
                    if len(item) == 3:
                        num = int(item[2])
                    elif l >= 7:
                        num = 7
                    else:
                        num = l
                    for i in range((l - num), l):
                        msg.Chat.SendMessage(lineList[i])
                else:
                    msg.Chat.SendMessage(u"そんなusernameおらへんで。@new username で新しく追加してなっ。")
            elif msg.Body.startswith(u"@list"):
                message = ""
                for list in glob.glob('back_log/*.dat'):
                    name = os.path.basename(list).split(".")[0]
                    message += name + ("\n")
                msg.Chat.SendMessage(message)
            elif msg.Body.startswith(u"@readme"):
                msg.Chat.SendMessage(u"[ @readme ]で説明を表示できんで。")
                msg.Chat.SendMessage(u"新しくuserを追加するときは[ @new username ]")
                msg.Chat.SendMessage(u"帰るときに[ @back username ]して帰ってなー")
                msg.Chat.SendMessage(u"[ @back username ]し忘れたときは[ @back username yyyy-mm-dd HH:MM ]でもOK")
                msg.Chat.SendMessage(u"履歴を見たいときは[ @look username ]で見れんで")
                msg.Chat.SendMessage(u"[ @look username num]で指定した分、見れるから！")
                msg.Chat.SendMessage(u"あとは、[ @list ]で誰が登録されてるかわかんで。")
                msg.Chat.SendMessage(u"ERROR回避はしてへんからイタズラはやめてや(sweat)")
                msg.Chat.SendMessage(u"機能はこれからどんどん追加していくで(dance)")

skype.OnMessageStatus = handler

call(skype, chat_id, title)
