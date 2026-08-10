# Program to check User ID and Password

user_id = input("Enter User ID: ")
password = input("Enter Password: ")

if user_id == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid User ID or Password")