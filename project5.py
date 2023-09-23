#!usr/bin/env python3
# week 5 project : Secure Drive
import time
import sys
import os
from pathlib import Path

'''This Prokect ewill alloow a user to create an accoun that is stored in a dictionary
the user will then login and be able to access theier files '''
accounts = {}
auth_usr = ""

with open("accounts.txt") as auth:
    for line in auth:
        (usr,pw) = line.split()# Create tuple of username/pw combo 
        accounts[(usr)] = pw #break the tuple in to doctiuonary key,value


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
        print("\n Please login to Secure Drive. To exit type 'Exit'\n")
        cusername = input("Enter your username: ") # Storeing username and password check if user wants to exit 
        if cusername == "exit":
            welcome()
        cpassword = input("Enter your password: ")
        login = {cusername : cpassword}
        
        if cusername not in accounts:
            print("\n User not found. Try agian. OR Type Exit to return to the main screen \n")
            time.sleep(1)
        elif accounts[cusername] == cpassword: #checks username and passwrod againsts known good credentails to allow or stop login 
            global auth_usr
            auth_usr = cusername
            print("\n Login Succesful \n")
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
        npassword = input("Create your password: ")
        if nusername in accounts:
            print("Username already taken. Please Choose Another\n")
        else:
            global auth_usr
            auth_usr = nusername
            accounts[nusername] = npassword
            with open("accounts.txt","w") as auth: #opens the accounts fike to write the new useres accou nt to the master accounts file 
                for key, value in accounts.items():
                    auth.write('%s %s\n' % (key, value))
            owd = os.getcwd()
            p = Path(nusername)
            os.chdir("usrDrives") # changes firectory to the user drive foleder so that a new user drive folder cna be created 
            p.mkdir()
            os.chdir(owd) # retuen to original working directory 
        
            print("Account creation sucessfull. Logged in as:", nusername,"\n")
            break
    
       ####Crates new folder for user 
                


welcome()

'''View will open currently exiting files '''
def view():
    print("Your Files:\n")
    owd = os.getcwd()
    os.chdir("usrDrives/" + auth_usr)
    
    while True:
        dirList = os.listdir()
        print("Files:\n",dirList)
        fileName = input("\nType the file name you would like to view or type 'exit'\n")
        if fileName == "exit":
            break
        elif fileName not in dirList:
            print("Please enter a valid file name\n")
            continue
        else:
            print("\n",fileName,";\n\n\n")
            file = open(fileName)
            print(file.read(),"\n\n")
            time.sleep(2)
    os.chdir(owd)# move back to main progrma direcrory 
    
'''Deleete will allow usere to select and deletea fiale'''
    
def delete():
    print("Your Files:\n")
    owd = os.getcwd() # save root directory for use later 
    os.chdir("usrDrives/" + auth_usr)
    while True:
        dirList = os.listdir()
        print("Files:\n",dirList)
        fileName = input("\nType the file name you would like to delete or type 'exit' \n\n")
        if fileName == "exit":
            break
        elif fileName not in dirList:
            print("Please enter a valid file name\n")
            continue
        else:
            sure = input(("Are you sure you want to delete ", fileName,"?/n Yes/No \n")).lower()
            if sure == "yes":
                os.remove(fileName) #delete file
                print("\n",fileName," Deleted")
                time.sleep(1)
            else:
                break
    os.chdir(owd)# move back to root program direcrory 
            
'''new will help user creat a new file'''
def new():
    owd = os.getcwd()
    print("Your Files:\n")
    os.chdir("usrDrives/" + auth_usr)
    while True:
        dirList = os.listdir()
        print("Files:\n",dirList)
        fileName = input("What would you like to call your file? Type 'Exit' to cancel\n\n")
        if fileName == "exit":
            pass
        elif fileName in dirList:
            print("Name in use. Please chose a new file name\n")
            continue
        else:
            newfile = open(fileName,"w") #create new file 
            fileData = input(("Write or paste the data for ", fileName, "below: \n"))
            newfile.write(fileData) # write to mneyl created file 
            print("\n",fileName," Created, and saved")
            break
    os.chdir(owd)# move back to main progrma direcrory 
    time.sleep(1)

'''This is the wile loop tha twill keep the user engaded with the program untill they log out or quit '''
while True: # this is where the logged in user  user will be able to view thier files and open them 
    action = str(input("What would you like to do? View Files:(View), Delete a file (Delete), Create a new file (New), Logout, (Logout)or Exit(Exit)\n\n")).lower()
    if action == "view":
        view()
    elif action == "delete":
        delete()
    elif action == "new":
         new()  
    elif action == "exit":
        break
    elif action == "logout":
        welcome()
    else: 
        print("Please enter a valid choice")
        
