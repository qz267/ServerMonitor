#!/usr/bin/env Python 
import os, sys, time 
 
while True: 
    time.sleep(4)
try: 
    ret = os.popen('ps -C apache -o pid,cmd').readlines()
    if len(ret) < 2:
        print "apache error, restart in 4s"
        time.sleep(3)
    os.system("service apache2 restart")
except: 
    print "Error", sys.exc_info()[1]
