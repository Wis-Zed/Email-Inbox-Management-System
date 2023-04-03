#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:28:39 2023

@author: wissamzendjebil
"""

class Email():

    has_been_read = False
    is_spam = False
    
    def __init__(self,email_contents,from_address):
        
        self.email_contents = email_contents
        
        self.from_address = from_address
        
    def mark_as_read(self):
        self.has_been_read = True
        
    def mark_as_spam(self):
        self.is_spam = True
        
        
    def __str__(self):
        return(f"{self.email_contents}")

#list called inbox to store all emails
inbox = []

#Creating email objects and adding them to inbox

email1  = Email("Hello World","wissam.zend@gmail.co.uk")
inbox.append(email1)

email2  = Email("This is very urgent1","wissam.z@outlook.com")
inbox.append(email2)

email3  = Email("I found my bag","smith.alice@gmail.com")
inbox.append(email3)

email4  = Email("I am running late,sorry","kevin_corporate@gmail.co.uk")
inbox.append(email4)







#Funtion which takes in the contents and email address from the received email to make a new Email object.
def add_email(): 
    email_contents = input("Enter the contents of the email: ")
    sender = input("Enter the email address from the received email: ")
    new_email = Email(email_contents,sender)
    inbox.append(new_email)
    

#Returns the number of messages in the store
def get_count(inbox): 
    total = len(inbox)
    print(f"There are {total} messages in the store")

# Returns the contents of an email in the list
def get_email(index): 
    chosen_email = inbox[index]
    chosen_email.mark_as_read()
    return(chosen_email.email_contents)

# Should return a list of all the emails that haven’t been read.
def get_unread_emails(inbox): 
    unread = []
    for idx,i in enumerate(inbox):
        if i.has_been_read == False:
            unread.append(i)
            print(idx,i)
    return(unread)

    

# Should return a list of all the emails that have been marked as spam.
def get_spam_emails(inbox): 
    # create list to store all spam emails in
    spam = [] 

    for idx,i in enumerate(inbox):
        if i.is_spam == True:
            # Output each email on screen with its index before it
            print(idx, i)
    return(spam)


# Deletes an email in the inbox.
def delete(): 
    for idx,i in enumerate(inbox):
        print(idx,i)
        
    delete_email = int(input("Which email would you like to delete"))
    inbox.pop(delete_email)
    
    
user_choice = ""

#Keep iterating through menu untill user wants to exist
while user_choice != 6:
    user_choice = int(input('''Select one of the following Options below:
1 - Read email
2 - Send email
3 - Delete email
4 - View spam emails
5 - See number of emails in inbox
6- Quit
: '''))
    
    
    if user_choice == 1:
        get_unread_emails(inbox)
        
        option = int(input("Please select either a email or input ‘-1’ to return to the main menu."))
        if option  == -1:
            pass #return to main menu
        else:
            chosen = get_email(option)
            change = str(input("Do you want to mark email as spam? Y/N: "))
            if change  == 'Y':
                to_change = inbox[option]
                to_change.mark_as_spam() 
            
            else:
                pass #return to main menu
        
        
    elif user_choice == 2:
        add_email()
        
    elif user_choice == 3:
        delete()
        
    elif user_choice == 4:
        get_spam_emails(inbox)
    
    elif user_choice == 5:
        get_count(inbox)
        
    elif user_choice == 6:
        print("Goodbye")
        break
     
    else:
        print("Oops - incorrect input")



