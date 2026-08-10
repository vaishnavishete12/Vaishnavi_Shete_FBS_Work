# Program to verify User ID, Password and CAPTCHA

import random

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == "admin" and password == "1234":
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    user_captcha = int(input("Enter Captcha: "))

    if user_captcha == captcha:
        print("Login Successful")
    else:
        print("Captcha Verification Failed")

else:
    print("Invalid User ID or Password")