import usrnew
import fileinput
import os.path
import time

UserAcct = usrnew.UserAcct

docname = "%s.txt" %UserAcct

file_exists = os.path.exists(docname)

if file_exists == False: 
  with open("genstats.txt", "r") as gs, open(docname, "a") as f:
     for line in gs:
         f.write(line)

  with open(docname, "a"):
   if "Player Not Defined" in open(docname).read():
        with fileinput.input(docname, inplace=True) as docname:
           for line in docname:
            new_line = line.replace("Player Not Defined", "Player = " + UserAcct)
            print(new_line, end='') 

print("Hello, ", UserAcct)

time.sleep(2)

Strt = input("Are you ready to play? (Y/N): " )
if Strt.upper() == "Y":
  import skull
