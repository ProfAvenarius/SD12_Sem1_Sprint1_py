#Description: A program in which you enter your Birthday, the day you started work,
#             and your favorite day of the week to get how many Bdays you worked in the past
#             based on a workweek of mon - fri, and tells you how many days off you will now
#             enjoy as new policy gives a B-day off IF it falls on a pre-selected 'Favorite Day".
#             Program is robust enough to calculate leap year birthdays

#Author: Group 22 (DCE, NP)
#Date: Jun 17 - 26

#Program libraries

import datetime

#Program constants

CUR_DATE = datetime.datetime.now()

curyear = CUR_DATE.year

WORK_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#Program functions

def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.
    DateValueStr = DateValue.strftime("%A, %B %d, %Y")
    return DateValueStr


def FDate3Str(Date):
    #Formats DD-MM-YYYY to (YYYY,MM,DD)
    day0 = Date[0:2]
    day1 =day0.strip("0")
    mth0 = Date[3:5]
    mth1 = mth0.strip("0")
    year1 = Date[6:10]
    return (day1, mth1, year1)


def DayWeek(fav):
    #Formats the day of the week from input
    if fav == "M":
        fav_day = "Monday"
    if fav == "Tu":
        fav_day = "Tuesday"
    if fav == "W":
        fav_day = "Wedsneday"
    if fav == "Th":
        fav_day = "Thursday"
    if fav == "F":
        fav_day = "Friday"
    if fav == "Sa":
        fav_day = "Saturday"
    if fav == "Su":
        fav_day = "Sunday"
    return (fav_day)


def FDay2Date(Bday1):
    #formats a list into a Datetimw obiject and retuns it and other variables for use throughout the program.
    dayx =Bday1[0]             
    mthx =Bday1[1]
    yrx =Bday1[2]
    agey = int(yrx)
    agem = int(mthx)
    aged = int(dayx)
    date_BD = datetime.datetime(agey,agem,aged)
    return (date_BD,dayx,mthx,yrx,agey,agem,aged)
 

def HowMany(year, day, Bday):
    #number of bdays landing on specified days left in the specified number of years, handles leap year b-days as well.
    num = 0
    for i in range(0,year):     
        byr = curyear+i
        if FDay2Date(Bday)[5] == 2 and FDay2Date(Bday)[6] == 29 and (byr % 4) != 0:
            n = 0
        else:
            date_B = datetime.datetime(byr,FDay2Date(Bday)[5],FDay2Date(Bday)[6])
            day_week =date_B.strftime("%A")
            n = day_week.count(day)
        num += n 
    return num


def HowMany2 (year1,year2,Bday):
    #number of bdays landing on specified days left in the specified number of years, handels leap year b-days as well.
    num = 0
    for i in range (0,year1):     
        num_temp = 0
        byr = year2+i
        if FDay2Date(Bday)[5] and FDay2Date(Bday)[6] == 29 and (byr % 4) != 0:
            num_temp = 0
        else:
            date_B = datetime.datetime(byr,FDay2Date(Bday)[5],FDay2Date(Bday)[6])
            day_week =date_B.strftime("%A")
            num_temp = WORK_DAYS.count(day_week)
        num += num_temp
    return num


def Day2Year(days_1):
    #turns number of days into years
    years_1 = int(days_1//365.25)
    return years_1


def main():
    #User Inputs and validations:
    print()
    print()
    print("**************************************************************************************")
    print()
    print("Welcome to the ABC Corporation phone message script manager, enter the employee's details")
    print("below to generate the personalized script. Enter End at employee's first name to exit.")
    print()
    print()
    print()
    print()
    print()
    
    while True:
        first_name = input("Enter the employee's first name:                                             ").capitalize()
        if first_name == "End":
            break
        elif first_name == "":
            print ("Data Entry Error: First name cannot left be blank. ")
        elif first_name.isalpha() == False:
            print ("Data Entry Error: First name must be alphbetic characters. ")
        else:
            while True:
                print()
                last_name = input("Enter the employee's last name:                                              ").capitalize()
                if last_name == "":
                    print ("Data Entry Error: Last name cannot be left blank. ")
                elif last_name.isalpha() == False:
                        print ("Data Entry Error: Last name must be alphbetic characters. ")
                else:
                    break
            
            while True:   
                print()
                phone_num = input ("Enter the employee's phone number (999-999-9999):                            ")
                if len(phone_num) != 12:
                              print ("Data Entry Error: Phone number must be 12 digits. ")
                else:
                    break
            
            while True: #Do to the use of many of the variables defined in this block later
                print() #on in the program, the choice was made to keep this in the main().
                employ_start = input("Enter the date the employee began working (DD-MM-YYYY):                      ")
                d1_test = employ_start[0:2]
                m1_test = employ_start[3:5]
                y1_test = employ_start[6:10]
                if len(employ_start) != 10:
                    print ("Data Entry Error: Date must be in the form XX-XX-XXXX.")
                elif d1_test.isnumeric() == False or m1_test.isnumeric() == False or y1_test.isnumeric() == False:
                    print ("Data Entry Error: All date fields must be completed numerically, example 01-01-2024.")
                elif int(m1_test) > 12:
                    print ("Data Entry Error: The value entered for month is out of bounds.")
                elif int(d1_test) > 31:
                    print ("Data Entry Error: The value entered for day is out of bounds")
                else:
                    break
            
            while True: #See note above.
                print()
                b_date = input ("Enter the employee's birthday (DD-MM-YYYY):                                  ")
                d2_test = b_date[0:2]
                m2_test = b_date[3:5]
                y2_test = b_date[6:10]
                if len(b_date) != 10:
                    print ("Data Entry Error: End date must be in the form XX-XX-XXXX.")
                elif d2_test.isnumeric() == False or m2_test.isnumeric() == False or y2_test.isnumeric() == False:
                    print ("Data Entry Error: All date fields must be completed numerically, example 01-01-2024.")
                elif int(m2_test) > 12:
                    print ("Data Entry Error: The value entered for month is out of bounds.")
                elif int(d2_test) > 31:
                    print ("Data Entry Error: The value entered for day is out of bounds")
                else:
                    break
                
            while True:    
                print()
                fav_enter = input ("Enter the employee's choosen favorite day of the week (M,Tu,W,Th,F,Sa,Su):   ").capitalize()
                if fav_enter == "":
                     print ("Data Entry Error: Field cannot left be blank.")
                elif first_name.isalpha() == False:
                    print ("Data Entry Error: Field must be alphbetic characters.")
                elif fav_enter != "M" and fav_enter != "Tu" and fav_enter != "W" and fav_enter != "Th" and fav_enter != "F" and fav_enter != "Sa" and fav_enter != "Su":
                    print ("Data Entry Error: Field must be a valid day of the week.")
                else:
                    break
            print()
            print()
            print()
            print()
            print("**************************************************************************************")
            print()
            print()
            print()

            #Calculations:

            employ_name = first_name + " " + last_name

            fav_day = DayWeek(fav_enter)

            Bday = FDate3Str(b_date)

            age100 = FDay2Date(Bday)[4]+100
            yrsleft =age100 - curyear 

            date_B1 = FDay2Date(Bday)[0]                         

            if FDay2Date(Bday)[5] == 2 and FDay2Date(Bday)[6] == 29:
                retire_age = datetime.datetime(FDay2Date(Bday)[4]+65,FDay2Date(Bday)[5],28)
            else:
                retire_age = datetime.datetime(FDay2Date(Bday)[4]+65,FDay2Date(Bday)[5],FDay2Date(Bday)[6])

            day_ofbirth = date_B1.strftime("%A")

            start_time = FDate3Str(employ_start)


            date_employ = FDay2Date(start_time)[0]                   
            days_worked = (CUR_DATE - date_employ).days
            days_retire = (retire_age - CUR_DATE).days


            yrs_worked = Day2Year(days_worked)
            yrs_retire = Day2Year(days_retire)

            num_B_work = HowMany(yrs_worked,fav_day,Bday)
            num100 = HowMany(yrsleft,fav_day,Bday)
            bdays_worked = HowMany2(yrs_worked,FDay2Date(start_time)[4],Bday)
            fav_bdays = HowMany(yrs_retire, fav_day, Bday)

            retire_fav = num100 -fav_bdays




            #output
            print ()
            print ()
            print (f"TO: {employ_name}")
            print (f"PH: {phone_num}")
            print ()
            print ()
            print ("We at ABC Corporation are announcing a new birthday policy.")
            print (f"You have worked with us for {yrs_worked} years, and have {yrs_retire} years left before you retire.")
            print (f"You have worked on {bdays_worked} Birthdays since you started, without a day off...")
            print()
            print ("But from now on you can have your Birthday off if it falls on your favorite day.") 
            print (f"In a recent questionaire you indicated your favorite day of the week was {fav_day}")
            if day_ofbirth == fav_day:
                print (f"By the way did you know you were born on a {day_ofbirth}, your favorite day!")
            else:
                print (f"Even though you were born on a {day_ofbirth} and not your favorite day {fav_day}")
            print()
            print ("But from now on you can have your Birthday off if it falls on your favorite day.") 
            print (f"So you can look forward to having {fav_bdays} days off in your remaining time employed. ")
            print ()
            print ("We hope you live a long life after you retire and hope you reach 100...")
            print (f"That would give you {yrsleft} years left, 35 of which will be enjoyed in retirement.")
            print (f"You will have {retire_fav} birthdays falling on your favorite days during that retirement.")
            print()
            print ("Thank you again for your great work at ABC Corporation. Have a great day!")
            print()
            print()
            print()
            print()
            print()
            print("**************************************************************************************")
            print()
            print()
            print()
            cont = input ("Enter 'End' to terminate program or hit return to continue.  ").capitalize()
            print()
            print()
            print()
            print()
            print()
            if cont == "End":
                break
    print()
    print()
    print()
    print()
    print()
    print()
    print("**************************************************************************************")
    print()
    print()
    print ("Program ended. Have a nice day,")
    print()
    print()
    

if __name__ == "__main__":
    main()




    