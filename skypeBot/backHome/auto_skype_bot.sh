#!/bin/sh
while true
do
#make sure bot is always alive
isAlive=`ps -ef | grep "/usr/bin/python main.py" | grep -v grep | wc -l`
if [ $isAlive = 1 ]; then
echo "alive"
else
cp -r back_log/ ~/4E/
echo "env DISPLAY=:20 XAUTHORITY=/var/run/skype/Xauthority VERSIONER_PYTHON_PREFER_32_BIT=yes /usr/bin/python main.py"
env DISPLAY=:20 XAUTHORITY=/var/run/skype/Xauthority VERSIONER_PYTHON_PREFER_32_BIT=yes /usr/bin/python main.py
fi
sleep 1
done
