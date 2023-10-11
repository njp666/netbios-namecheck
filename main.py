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

#asks the user for input and         
        if userInput == 2:
            print("\nCurrent hostname: "+host)
            userHost = input("Enter your desired hostname (This is NOT the FQDN, e.g. hostname.foo.bar): ")
           
            if len(userHost) >= 1 and len(userHost) <= 15:
                print("Length OK.\nYour hostname is: "+userHost+"\nLength: "+str(len(userHost))+"\n")
            
            elif len(userHost) <= 0:
                 print("Error. Hostname must be greater than 0 characters.")

            else:
                print("\nHostname too long! Length is: "+str(len(userHost))+"\nMax: 15 characters.\n")

        if userInput == 3:
            print("Exiting...\n")
            quit()
mainMenu()
