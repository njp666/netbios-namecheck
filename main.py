"""abcd"""
# import platform module to grab the current user's machine name...
from platform import node as hostname
import sys

#print statement to console...
print("Your current hostname is: " + hostname())

print("Enter your option below: \n" +
      "(1) Check your new hostname against NetBIOS rules \n"
       + "or \n" + "(2) Exit \n")
userInput = input("Option: ")

if userInput == str("1"):
    print("1")
    sys.exit()
else:
    sys.exit()
