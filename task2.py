#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
username=input("Enter username")
password=input("Enter password")
while "admin" in username and ("12345") in password:
    print("access denied")
    exit(1) 
while "admin" in username and ("12345") in password:
    print("Access granted")
    exit(1)
