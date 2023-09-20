#!usr/bin/env python3
# week 5 project : Create an account 

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

while True: # this while loop will handle user input from the welcome function  user input 
    action = input("\nWelcome to the Reservation Portal!\n \n What would you like to do? \n \n View: View All Sites \n Reserve: Reserve A Site \n Cancel: Cancel a Reservation \n Exit: Exit Reservation System\n\n").lower()
    if action == "login":
        login()        
    elif action == "NewUser":
        mkaccount()  
    elif action == "access":
        accessFiles()
    elif action == "exit":
        break
    else: 
        print("Please enter a valid choice")