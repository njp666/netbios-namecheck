"""abcd"""
# import platform module to grab the current user's machine name...
from platform import node as hostname
host = hostname()

def mainMenu():
    while (True):
        print("Enter your menu option:"+
          "\n(1) Check current hostname"+
          "\n(2) Check proposed hostname length"+
          "\n(3) Exit")
        userInput = int(input("\nOption: "))

#prints the current machine hostname and gives length.
        if userInput == 1:
            print("Your current hostname is:\n"+host+
                  "\nHostname length: "
                  +str(len(host))+"\n")
        
        if userInput == 2:
            print("\nCurrent hostname: "+host)
            userHost = input("Enter your desired hostname: ")
            if len(userHost) > 15:
                print("\nHostname too long! Length is: "+str(len(userHost))+"\nMax: 15 characters.\n")
            
            if len(userHost) <= 15:
                print("Length OK.\nYour hostname is: "+userHost+". \nLength: "+str(len(userHost))+"\n")

        if userInput == 3:
            print("Exiting...\n")
            quit()
mainMenu()
