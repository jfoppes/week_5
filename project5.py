#!usr/bin/env python3
# week 5 project : Secure Drive

'''This Prokect ewill alloow a user to create an accoun that is stored in a dictionary
the user will then login and be able to access theier files '''
accounts = {}
auth_usr = ""
with open("accounts.txt") as auth:
    for line in auth:
        (usr,pw) = line.split()# Create tuple of username/pw combo 
        accounts[(usr)] = pw #break the tuple in to doctiuonary key,value
import time
def welcome(): # this is where the user will be greeeted and asked to login or create account 
    print("\n\nSecure Drive")
    while True: # this while loop will handle user input and call login/ new account functions
        action = input("\nWelcome to SecureDrive!\n \n What would you like to do? \n \n Login? or create an account?\n\n Type Login or NewUser\n\n").lower()
        if action == "login":
            login()
            break        
        elif action == "newuser":
            mkaccount()
            break
        elif action == "exit":
            break
        else: 
            print("Please enter a valid choice")
    
def login(): # if user has an account they login here 
    breaker = True
    while breaker == True:
        print("\n Please login to Secure Drive \n")
        cusername = input("Enter your username: ") # Storeing username and password 
        cpassword = input("Enter your password: ")
        login = {cusername : cpassword}
        if cusername not in accounts:
            print("\n User not found. Try agian. \n")
            time.sleep(1)
        elif accounts[cusername] == cpassword: #checks username and passwrod againsts known good credentails to allow or stop login 
            print("\n Login Succesful \n")
            auth_usr = cusername
            print("Logged in as", auth_usr,"\n")
            auth.close() # close username and passwrod file
            break
        else:
            print("\n Incorrect Login. Try agian. \n")
            time.sleep(1)
            
    

def mkaccount(): # if the user does not have an account they can make one
    breaker = True
    while breaker == True:
        print("\n Create a Secure Drive account \n")
        nusername = input("Create your username: ")
        npassword = input("Create your password: \n")
        if nusername in accounts:
            print("Username already taken. Please Choose Another\n")
        else:
            accounts[nusername] = npassword
            print("Account creation sucessfull. Logged in as:", nusername,"\n")
            break
                

def accessFiles(): # once account created and or logged in, user can access thier files 
    breaker = True
    while breaker == True:
        pass


welcome()   
while True: # this is where the logged in user  user will be able to view thier files and open them 
    action = input("What would you like to do? View Files:(View), Delete a file (Delete), Create a new file (New) or Exit(Exit)\n\n").lower()
    if action == "view":
        view()        
    elif action == "delete":
        delete()
    elif action == "new":
        new()    
    elif action == "exit":
        break
    else: 
        print("Please enter a valid choice")
        