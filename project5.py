#!usr/bin/env python3
# week 5 project : Secure Drive

'''This Prokect ewill alloow a user to create an accoun that is stored in a dictionary
the user will then login and be able to access theier files '''


def welcome(): # this is where the user will be greeeted and asked to login or create account 
    pass

def login(): # is usr has accoun t ehy cna login 
    pass

def mkaccount(): # if the user does not ahve a accoun t they can make one
    pass

def accessFiles(): # once account created and or logged in, user can access thier files 
    pass

while True: # this while loop will handle user input from the welcome function and login/ new account functions
    action = input("\nWelcome to SecureDrive!\n \n What would you like to do? \n \n Login? or create an account?\n\n Type Login or NewUser").lower()
    if action == "login":
        login()        
    elif action == "newuser":
        mkaccount()
    elif action == "exit":
        break
    else: 
        print("Please enter a valid choice")
        
while True: # this is where the logged in user  user will be able to view thier files and open them 
    action = input("What would you like to do? View Files:(View), Delete a file (Delete), Create a new file (New) or Exit(Exit)").lower()
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
        