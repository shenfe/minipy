#/bin/sh

# 参考：https://blog.csdn.net/taiyang1987912/article/details/44850999，乌托邦2号，CSDN

while true
do
    count=`ps -ef | grep "daemon.py" | grep -v "grep"`
    if [ "$?" != "0" ]; then
        ./daemon.py start
    fi
    sleep 2
done
