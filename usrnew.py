import random
from random import *
import hashlib
import getpass
import os.path
import os
import time

accf = os.path.basename("account.txt")

while True:
 NewAcct = input("Do you have an account? (Y/N): ")

 if NewAcct.upper() == "Y":
     UserAcct = input("What is your Username? " )
     if UserAcct in open(accf).read():
         Pass = getpass.getpass("Please enter your password: ")
         Passhash = hashlib.sha256(str(UserAcct + Pass).encode('utf-8')).hexdigest()
         Accthash = UserAcct + ":" + Passhash
         if Accthash in open(accf).read():
             print(UserAcct, " has been logged in")
             break
         if Accthash not in open(accf).read():
             print("Password is incorrect")
     if UserAcct not in open(accf).read():
         print("Username not valid")

 if NewAcct.upper() == "N":
     UserAcct = input("Enter Username you would like to use: ")
     if UserAcct in open(accf).read():
        print("Username already exists")
     if UserAcct not in open(accf).read():
        Pass = getpass.getpass("Please enter a password: ")
        Passhash = hashlib.sha256(str(UserAcct + Pass).encode('utf-8')).hexdigest()
        print(UserAcct, " created!")
        print(UserAcct, UserAcct + ":" + Passhash, sep='\n', file=open(accf, "a"))

os.system('clear' or 'cls')
