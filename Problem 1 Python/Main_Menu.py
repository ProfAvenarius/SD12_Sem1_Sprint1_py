#Description: A program that opens a menu for the selection of one of five programs.
#Author: Group 22 (DCE, NP)
#Date: Jun 17 - 26

#Program libraries
import FizzBuzz
import Chocolate_Travel_Claims
import Cool_Stuff_with_Strings_and_Dates
import XYZ_Company
import Something_New



#Prgram functions        5 functions used in this program, 2 functions in Program 2,  
def FB():              # 0 functions used in Program 3, 7 functions used in Program 4,
    FizzBuzz.main()    # 6 functions used in Program 5 and 6 in Program 6. There are 
                       # functions repeated, such as Money(), and this count does not 
def ChocTrav():        # include the Main() functions that entail the whole of each program.
    Chocolate_Travel_Claims.main()

def CoolStuff():
    Cool_Stuff_with_Strings_and_Dates.main()

def LttleBit():
    XYZ_Company.main()

def SomeNew():
    Something_New.main()
    
while True:
    print()
    print()
    print()
    print()
    print (" Midterm Sprint - Main Menu")
    print()
    print ("1. Complete a Travel Claim.")
    print ("2. Fun Interview Question.")
    print ("3. Cool Stuff with Strings and Dates.")
    print ("4. A Little Bit of Everything.")
    print ("5. Something Old, Something New.")
    print ("6. Quit.")
    print()
    while True:
        choice =input ("         Enter choice (1-6): ")
        try:
            int(choice)
            break
        except ValueError:
            print ("Data Entry Error: An number must be entered.")
    choice = int(choice)    
    print()
    print()
    print()



    if choice == 1:
        print(f"You have selcted {choice}, Complete a Travel Claim.")
        print()
        print()
        print()
        ChocTrav()
    if choice == 2:
        print(f"You have selcted {choice}, Fun Interview Question.")
        print()
        print()
        print()
        FB()
    if choice == 3:
        print(f"You have selcted {choice}, Cool Stuff with Strings and Dates.")
        print()
        print()
        print()
        CoolStuff()
    if choice == 4:
        print(f"You have selcted {choice}, A Little Bit of Everything.")
        print()
        print()
        print()
        LttleBit()
    if choice == 5:
        print(f"You have selcted {choice}, Something Old, Something New.")
        print()
        print()
        print()
        SomeNew()
    if choice == 6:
        print(f"You have selcted {choice}, Quit Program.")
        print()
        print()
        print()
        break

print()
print()
print ("Thank you for using this program. Have a nice day.")
print()
print()
print()





    