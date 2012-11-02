# coding: utf-8

import Skype4Py, os, sys, glob, datetime, time

skype = Skype4Py.Skype()
skype.Attach()

def getChatId():
    for i in range(len(skype.Chats)):
        if skype.Chats[i].Topic == u'帰らせマスターから貴方へ伝えたいこと':
            return i

chat_id = getChatId()

def handler(msg, event):
    if event == u"RECEIVED":
        if msg.Chat.Topic == u'帰らせマスターから貴方へ伝えたいこと' or msg.Chat.Topic == u'4Eチャット':
            if msg.Body.startswith(u"@bye"):
                item = msg.Body.split(' ')
                try:
                    name = item[1]
                    try:
                        filename = glob.glob('back_log/' + name + '%*%0%00.dat')[0]
                        file = open(filename, "a")
                        if len(item) >= 3:
                            file.write(item[2]+" "+item[3]+"\n")
                        else:
                            file.write(str(datetime.datetime.now())+"\n")
                        file.close()
                        msg.Chat.SendMessage(u"ほなね!お気をつけて(h)")
                        cmd = 'mv ' + filename + ' ' + filename.replace('%0%00.dat', '%1%00.dat')
                        os.system(cmd)

                    except:
                        try:
                            filename = glob.glob('back_log/' + name + '%*%1%00.dat')[0]
                            msg.Chat.SendMessage(u"もう今日は帰ったことになってんで。")
                        except:
                            msg.Chat.SendMessage(u"そんなusernameおらへんで。@new username で新しく追加してなっ。")
                except:
                    msg.Chat.SendMessage(u"[@bye username] ってふうに、usernameも指定した？！もう一回やってみて。")

            elif msg.Body.startswith(u"@new"):
                try:
                    name = msg.Body.split(' ')[1]
                    if name.find("%") < 0:
                        filename = glob.glob('back_log/' + name + '%*%*%*.dat')
                        if len(filename) > 0:
                            msg.Chat.SendMessage(u"そのusernameの人、もういてはるわー(bow)")
                        else:
                            skypeID = msg.FromHandle
                            filename = "back_log/" + name + "%" + skypeID + "%0%00.dat"
                            file = open(filename, "w")
                            file.write("")
                            file.close()
                            msg.Chat.SendMessage(u"username登録したで(*)")
                    else:
                        msg.Chat.SendMessage(u"usernameに % は使われへんねん。ちゃうusernameにしてー。")
                except:
                    msg.Chat.SendMessage(u"[@new username] ってふうに、usernameも指定した？！もう一回やってみて。")

            elif msg.Body.startswith(u"@history"):
                try:
                    item = msg.Body.split(' ')
                    name = item[1]
                    try:
                        filename = glob.glob('back_log/' + name + '%*%*%*.dat')[0]
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
                    except:
                        msg.Chat.SendMessage(u"そんなusernameおらへんで。@new username で新しく追加してなっ。")
                except:
                    msg.Chat.SendMessage(u"[@history username] ってふうに、usernameも指定した？！もう一回やってみて。")
            elif msg.Body.startswith(u"@list"):
                message = ""
                for list in glob.glob('back_log/*%*%*%*.dat'):
                    name = os.path.basename(list).split("%")[0]
                    message += name + ("\n")
                msg.Chat.SendMessage(message)
            elif msg.Body.startswith(u"@help") or msg.Body.startswith(u"@readme"):
                msg.Chat.SendMessage(u"[ @help ]で説明を表示できんで。")
                msg.Chat.SendMessage(u"新しくuserを追加するときは[ @new username ]")
                msg.Chat.SendMessage(u"帰るときに[ @bye username ]して帰ってなー")
                msg.Chat.SendMessage(u"[ @bye username ]し忘れたときは[ @bye username yyyy-mm-dd HH:MM ]でもOK")
                msg.Chat.SendMessage(u"履歴を見たいときは[ @history username ]で見れんで")
                msg.Chat.SendMessage(u"[ @history username num]で指定した分、見れるから！")
                msg.Chat.SendMessage(u"あとは、[ @list ]で誰が登録されてるかわかんで。")
                msg.Chat.SendMessage(u"ERROR回避はしてへんからイタズラはやめてや(sweat)")
                msg.Chat.SendMessage(u"機能はこれからどんどん追加していくで(dance)")

skype.OnMessageStatus = handler


while(True):
    now = datetime.datetime.now()
    if now.weekday() != 5 and now.weekday() != 6:
        if (skype.Chats[chat_id].Topic == u'帰らせマスターから貴方へ伝えたいこと'):

            if (now.second == 0):
                if (now.hour == 9):
                    if (now.minute == 30):
                        skype.Chats[chat_id].SendMessage(now.strftime('おはよーさん！%m月%d日が始まんで！今日も１日きばっていこやっ(flex)'))
                        filenameList = glob.glob('back_log/*%*%1%*.dat')
                        for filename in filenameList:
                            cmd = 'mv ' + filename + ' ' + filename.replace('%1%', '%0%')
                            os.system(cmd)
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

