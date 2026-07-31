import sys
print ("CREATE AN EMAIL")
frontname = input("Enter your first name                  : ")
backname = input("Enter your last name                   : ")
username = frontname + backname
domain = input(f"Enter your domain (gmail, yahoo, outlook.) : ")

if " " in username:
    username = username.replace(" ", "")
    username = username.lower()   

email = (f"{username}{"@"}{domain}{".com"}")
at =  email.find("@")
username = email[:at]
domain = email[at + 1:]
print("")

print(f"your username is '{username}' and your domain is '{domain}' ")
answer = input("Is it correct? y / n : ")
print("")
print(f"This is your email now : '{email}' " if answer == "y" else sys.exit() )