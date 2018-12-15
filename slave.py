import os
import subprocess

def hdfs():
    return 0

def core():
    return 0

def sethostname():
    print ("Enter Desired Hostname (ex. X.slave.com): ", end=' ')
    x = input()
    os.system('hostnameclt set-hostname {}'.format(x))
    print("Hostname Set as : {}".format(os.system('hostname')))
    os.system('hostname')    

def makeDataDir():
    os.system('mkdir /data')

def start():
    os.system("iptables -F")
    x = subprocess.getstatusoutput("hadoop-daemon.sh start datanode")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Data Node Started")
        os.system('tput setaf 7') 
        os.system('jps')
    else:
        os.system('tput setaf 1')
        print("ALERT: Data Node Failed to Start!")
        os.system('tput setaf 7') 
        os.system('jps')

def stop():
    x = subprocess.getstatusoutput("hadoop-daemon.sh stop datanode")
    if x[0] == 0:
        os.system('tput setaf 2')
        print("Data Node Stopped")
        os.system('tput setaf 7') 
        os.system('jps')
    else:
        os.system('tput setaf 1')
        print("ALERT: Data Node Failed to Stop!")
        os.system('tput setaf 7') 
        os.system('jps')

def report():
    os.system("hadoop dfsadmin -report")