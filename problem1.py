##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
import time
import math
username=(input("Enter username")).strip()
password=(input("Enter password")).strip()
count=0
while username !="admin" or password !=("12345"):
    print("access denied")
    username=(input("Enter username")).strip()
    password=(input("Enter password")).strip()
    count=count+1
    if count>3:
        break
if username =="admin" and password==("12345"):
    print("Access granted")
    username=(input("Enter username")).strip()
    password=(input("Enter password")).strip()
