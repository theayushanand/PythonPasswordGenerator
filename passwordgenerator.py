# importing essentials
from random import * 

#setting the characters set
char1="ABCDEFGHIJKLMNOPQRTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()0123456789"

#asking the password length from user
length = int(input('Enter the length of your Password : '))

# creating an empty password string
Password1 = ''

#adding random characters to the password
for x in range(length):
    Password1 += choice(char1)

#print the password
print(Password1)