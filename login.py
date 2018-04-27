UKfrom colorama import Fore, Back, init
import sys, os, time
from getpass import getpass
animation = "|/-\\"
animation3 = "/-|\\"
animation4 = "/x/x\\x"
animation5 = "%÷%÷"
os.system("clear")



m = []

f = open("/data/data/com.termux/files/usr/security/log.txt","r")
b = f.read()

#c = len(b)
#a.append(b)
l = b.split("\n")
print(Fore.RED+"Log In : \n")

usr = input(Fore.GREEN+"User Id : "+Fore.CYAN+"")
m.append(usr)

#print(a)
if l[2] == m[0] :
    print(Fore.GREEN+"\nUser Id Matched. \n")
    passwd = getpass(Fore.GREEN+"\nPassword : "+Fore.CYAN+"")
    m.append(passwd)
    if l[3] == m[1]:
        print(Fore.GREEN+"\nPassword Matched.\n ")
        for i in range(100):
            #sys.stdout.write(Fore.GREEN+"Logging in..... ")
            time.sleep(0.1)
            sys.stdout.write(Fore.YELLOW+"\r" + animation[i % len(animation)])
            sys.stdout.write(Fore.GREEN+" ........Logging In.... ")
            sys.stdout.write(Fore.YELLOW+"" + animation[i % len(animation)]) 
            sys.stdout.flush()
            #do something
        os.system("clear")
        print(Fore.YELLOW+"\t[  Welcome ===> "+l[0]+"  ]")
        init(autoreset=True)
    else:
        print(Fore.RED+"Password Not Matched.")
        time.sleep(3)
        os.system("killall -9 com.termux")
else:
    print(Fore.RED+"User Id Not Matched.")
    time.sleep(3)
    os.system("killall -9 com.termux")
