# Email-Inbox-Management-System
This is a simple email inbox management system that allows a user to manage their inbox by adding, reading, deleting, and marking emails as spam.

## Classes

### Email
The Email class represents an email. It has the following attributes:

 - email_contents: a string representing the contents of the email.
 - from_address: a string representing the email address of the sender.
 - has_been_read: a boolean indicating whether the email has been read or not (default is False).
 - is_spam: a boolean indicating whether the email has been marked as spam or not (default is False).

The Email class has the following methods:

 - __init__(self, email_contents, from_address): Initializes the Email object with email_contents and from_address.
 - mark_as_read(self): Marks the email as read.
 - mark_as_spam(self): Marks the email as spam.
 - __str__(self): Returns the contents of the email as a string.

## Functions

The email inbox management system has the following functions:

 - add_email(): Prompts the user to enter the contents and email address of a new email and creates a new Email object with these attributes. The new email is added to the inbox.
 - get_count(inbox): Returns the number of emails in the inbox.
 - get_email(index): Returns the contents of the email at the given index and marks it as read.
 - get_unread_emails(inbox): Returns a list of all emails that haven't been read.
 - get_spam_emails(inbox): Returns a list of all emails that have been marked as spam.
 - delete(): Prompts the user to select an email to delete and removes it from the inbox.

## Running the Program

The program starts by creating an empty inbox list. It then creates four sample Email objects and adds them to the inbox list.

The program then presents the user with a menu of options to choose from:

 - Option 1: Read email - allows the user to view and mark an email as spam.
 - Option 2: Send email - allows the user to add a new email to the inbox.
 - Option 3: Delete email - allows the user to delete an email from the inbox.
 - Option 4: View spam emails - allows the user to view all emails that have been marked as spam.
 - Option 5: See number of emails in inbox - displays the number of emails currently in the inbox.
 - Option 6: Quit - exits the program.

The program will continue to loop through the menu options until the user chooses to quit the program.



