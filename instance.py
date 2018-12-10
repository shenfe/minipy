# coding: utf8

'''
参考：https://blog.csdn.net/taiyang1987912/article/details/44850999，乌托邦2号，CSDN
'''

import sys
import socket


PORT = 60123


def ApplicationInstance(port=PORT):
    try:
        global s
        s = socket.socket()
        host = socket.gethostname()
        s.bind((host, port))
    except:
        print 'instance is already running...'
        sys.exit(0)


def main():
    '''示例函数'''

    import time

    c = 0
    while True:
        print '%d: %s\n' % (c, time.ctime())
        c += 1
        time.sleep(1)


if __name__ == '__main__':
    ApplicationInstance()
    main()
