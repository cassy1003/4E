#!/bin/sh
while true
do
#ここではftpdのプロセス監視
isAlive=`ps -ef | grep "/usr/bin/python skype_bot.py" | grep -v grep | wc -l`
if [ $isAlive = 1 ]; then
echo "alive"
else
echo "env DISPLAY=:20 XAUTHORITY=/var/run/skype/Xauthority VERSIONER_PYTHON_PREFER_32_BIT=yes /usr/bin/python skype_bot.py"
env DISPLAY=:20 XAUTHORITY=/var/run/skype/Xauthority VERSIONER_PYTHON_PREFER_32_BIT=yes /usr/bin/python skype_bot.py
fi
sleep 3
done
