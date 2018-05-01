#!/usr/bin/python
import os
import sys
import time
from colorama import Fore, Back, init
import string as s
from getpass import getpass

a = s.digits
b = s.ascii_letters
c = s.punctuation

logo = '''
 _____ _____ _                
|_   _|____ | |               
  | |     / / |     ___   ___ 
  | |     \ \ |    / _ \ / __|
  | | .___/ / |___| (_) | (__ 
  \_/ \____/\_____/\___/ \___|
                              
'''
about = '''
Author       : EPIC                      | Tool Name    : T3Loc
Team         : SkyKnight                 | Tool Version : V1.0
Date         : 26/04/2018                | Made By      : EPIC
Time         : 4:23 PM (India)           |
Author Email : epic.skyknight@gmail.com  |
-----------------------------------------------------------------
'''
os.system("clear")
print(Fore.CYAN+logo)
print(Fore.YELLOW+about)
def register():
    #os.system("clear")
    print(Fore.RED+"           \n\nRegister :\n\t")
    fname = input(Fore.GREEN+"First Name :"+Fore.YELLOW+"")
    if fname not in a+b+c:
        print(Fore.CYAN+"\nSuccessfully Add\n")
        lname = input(Fore.GREEN+"Last Name  :"+Fore.YELLOW+"")
        if lname not in a+b+c:
            print(Fore.CYAN+"\nSuccessfully Add\n")
            usr = input(Fore.GREEN+"User Id    :"+Fore.YELLOW+"")
            if usr not in a+b+c:
                print(Fore.CYAN+"\nSuccessfully Add\n")
                passwd = getpass(Fore.GREEN+"Password   :"+Fore.YELLOW+"")
                if passwd not in a+b+c:
                    print(Fore.CYAN+"\nSuccessfully Add\n")
                    passwd1 = getpass(Fore.GREEN+"Confirm Password :"+Fore.YELLOW+"")
                    if passwd == passwd1:
                        print(Fore.CYAN+"\nSuccessfully Confirm Password\n")
                        os.system("mkdir /data/data/com.termux/files/usr/security")
                        f = open("/data/data/com.termux/files/usr/security/log.txt","w")
                        f.write(fname+"\n")
                        f.close()
                        s = open("/data/data/com.termux/files/usr/security/log.txt","a")
                        s.write(lname+"\n")
                        s.write(usr+"\n")
                        s.write(passwd+"\n")
                        s.write(passwd1+"\n")
                        s.close()
                        
                    else:
                        print(Fore.RED+"Please Enter Correct Password.")
                else:
                    print(Fore.RED+"Please Enter Password.\n")
            else:
                print(Fore.RED+"Please Enter User Id.\n")
        else:
            print(Fore.RED+"Please Enter Last Name.\n")
    else:
        print(Fore.RED+"Please Enter First Name.\n")
register() 
init(autoreset=True) 
os.system("mv register.py /data/data/com.termux/files/usr/bin")  
   
