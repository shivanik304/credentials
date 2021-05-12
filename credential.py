# -*- coding: utf-8 -*-
"""
Created on Wed May 12 12:06:37 2021

@author: IT LAB
"""

credentials = {}    #Dictionary defined
def Display_Menu():            #Start Menu:Ask if user exists or create new user
    status =input("Are you a registered user? (Yes/No)? Press enter to exit: ")
    if status == "Yes":
        existing_user()   #existing_user function calling
    else:
        new_user()       #new_user function calling
                          
        
def existing_user():                 
    username =input("Enter login name: ")       #Login if existing user
    Password =input("Enter password: ") 
    if username in credentials and credentials[username] == Password:  #if username exists in credential dictionary and matches with the created credentials then login successful
        print("Login successful!")
    else:
        print("User doesn't exist or wrong password!")
        print('\n')
        print('Create your account')
        new_user()                            
    

def new_user():                              #new_user function calling
    username =input("Create username: ")     
    if username in credentials:
        print ("Login name already exist!")
    else:
        password =input("Create password: ")    #Creates New User
        credentials[username] = password      #assigning password to username entered in credential dictionary.
        name=input('Enter your name')
        credentials[username] = name
        Mobile_no=input('Enter your Mobile No')
        credentials[username] = Mobile_no
        print('\n')
        print("Account successfully created!")             
        
    status1=input('To go back to login page!(Yes/No)?')      
    if status1 == "yes":   #if 'yes' entered then 'existing_user' fucntion get called.
     existing_user()
    elif status1=='no':   #if 'no' entered then 'new_user' fucntion called.
     new_user()
    else:                 #to exit, just press enter.
      return None   
    
print(credentials)   # after exiting, type credentials to see created username & password dictionary.
Display_Menu()       #display_mmenu function calling