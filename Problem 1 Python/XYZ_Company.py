#Description: A program to detemine the maintenence schedule and amotization schedule
#Author: Group 22 (DCE, NP)
#Date: Jun 17 - 26

#Program Libraries

import datetime


#Program Constants

B_CLEAN = 10 #days
TUBE_FLUID = 3 #weeks
M_INSPECT = 6 #mths
USE_LIFE =15 #yrs
SALV_RATE = 0.10

Clean_List = []
Tube_List =[]
Inspect_List =[]

CURR_DATE = datetime.datetime.today()


#Program functions:

def FDateDate(Date):
    #Formats DD-MM-YYYY string to (YYYY,MM,DD) Datetime type.
    day0 = Date[0:2]
    day1 =day0.lstrip("0")
    mth0 = Date[3:5]
    mth1 = mth0.lstrip("0")
    year1 = Date[6:10]
    date_str = (day1, mth1, year1)
    dayx = date_str[0]
    mthx = date_str[1]
    yrx = date_str[2]
    agey = int(yrx)
    agem = int(mthx)
    aged = int(dayx)
    #date_int = (agey, agem, aged)
    date_date = datetime.datetime(agey, agem, aged)
    return (date_date)

def FDateDateLife(Date):
    #Formats DD-MM-YYYY string to (YYYY,MM,DD) datetime type 15 yeaars in future
    day0 = Date[0:2]
    day1 =day0.lstrip("0")
    mth0 = Date[3:5]
    mth1 = mth0.lstrip("0")
    year1 = Date[6:10]
    date_str = (day1, mth1, year1)
    dayx = date_str[0]
    mthx = date_str[1]
    yrx = date_str[2]
    agey = int(yrx)
    agem = int(mthx)
    aged = int(dayx)
    date_date = datetime.datetime(agey+15, agem, aged)
    return (date_date)


def FDateDateInspect(next_date):
    #Formats (YYYY,MM,DD) datetime type 6 months in future
    dayx = next_date.day
    mthx = next_date.month
    yrx = next_date.year
    if mthx + 6 > 12:
        mthx = mthx -6
        yrx += 1
    else:
        mthx += 6
    date_date = datetime.datetime(yrx, mthx, dayx)
    return (date_date)

def Money(enter_num):
    #Formats a float into a cash value.
    price_dsp = "${:,.2f}".format(enter_num)
    return price_dsp

def Display(random_date):
    #Foramts a date object into the display style
    display_date = random_date.strftime("%d-%b-%Y")
    return display_date

def FullList(): 
    #Takes no imputs but prints all calculated maintenance objects in three formated columns
    max_length = max(len(Clean_List), len(Tube_List), len(Inspect_List))
    Clean_List.extend([None] * (max_length - len(Clean_List)))
    Tube_List.extend([None] * (max_length - len(Tube_List)))
    Inspect_List.extend([None] * (max_length - len(Inspect_List)))
    print(f"{'CLEANING':<15} {'TUBE AND FLUID CHECKS':<25} {'MAJOR INSPECTION':<20}")
    for clean_date, tube_date, inspect_date in zip(Clean_List, Tube_List, Inspect_List):
        clean_str = Display(clean_date) if clean_date else ""
        tube_str = Display(tube_date) if tube_date else ""
        inspect_str = Display(inspect_date) if inspect_date else ""
        print(f"{clean_str:<15} {tube_str:<25} {inspect_str:<20}")


#Given the date this document is produced may be different that the purchase date of the 
#equipment, this calculates the first round or maintenance objects immediately after purchase
#and if that period has already passed will also return the next round of maintenance objects
#occuring after the current date, allowing the user to get the dates that are immediately 
#relevant. If more detail is required an option exists to return the full maintenance schedule
#at the end of output.


def main():
    print()
    print()
    print("**************************************************************************************")
    print()
    print("Welcome to the XYZ Company's maintenance and amortization scheduling program, complete")
    print("fields as directed below to generate next maintenance dates and amortization schedule.")
    print("Enter 'End' for name of unit to exit.")
    print()
    print()
    print()
    print()
    print()

    #User Inputs and Validations:
    while True:
        print()
        unit_name = input("Enter the name of the unit.                       ").capitalize()
        if unit_name == "End":
            break
        if unit_name == "":
            print ("Data Entry Error:Field cannot be left blank.")
        else:
            while True:
                print()
                unit_cost =input("Enter the purchase cost of the unit (99999.99):   ")
                try: 
                    float(unit_cost)
                    break
                except ValueError:
                    print ("Data Entry Error: A value must be entered that is numerical")
            
            while True:
                print()
                enter_date  = input("Enter the date of purchase (DD-MM-YYYY):          ")
                d1_test = enter_date[0:2]
                m1_test = enter_date[3:5]
                y1_test = enter_date[6:10]
                if len(enter_date) != 10:
                    print ("Data Entry Error: Date must be in the form XX-XX-XXXX.")
                elif d1_test.isnumeric() == False or m1_test.isnumeric() == False or y1_test.isnumeric() == False:
                    print ("Data Entry Error: All date fields must be completed numerically, example 01-01-2024.")
                elif int(m1_test) > 12:
                    print ("Data Entry Error: The value entered for month is out of bounds.")
                elif int(d1_test) > 31:
                    print ("Data Entry Error: The value entered for day is out of bounds")
                elif FDateDate(enter_date) > CURR_DATE:
                    print ("Purchase Date must be prior than current date.")
                else:
                    break
            
            while True:
                print()
                print("The output below will provide the first and/or next date for each maintenance item.")
                print("A full list of dates for all maintenance items is available to appear at end of output.")
                want_list = input("Would you like this list? - Note it is very long (Y/N) ").capitalize()
                if want_list != "N" and want_list != "Y":
                    print ("Data Entry Error: A value must be entered either 'Y' or 'N'.")
                else:
                    break

            #calculations:

            unit_cost = float(unit_cost)
            unit_cost_dsp =Money(unit_cost)

            curr_date_dsp =CURR_DATE.strftime("%A %B %d, %Y")

            pur_date = FDateDate(enter_date)

            pur_date_dsp =Display(pur_date)




            life_date = FDateDateLife(enter_date)

            days_life = life_date - pur_date
            no_days_life = days_life.days

            no_clean_cycle = no_days_life//B_CLEAN
            no_tube_cycle = no_days_life//(TUBE_FLUID*7)

            for i in range(1,no_clean_cycle):
                clean_date = pur_date + datetime.timedelta(days = B_CLEAN*i)
                Clean_List.append(clean_date)

            next_clean = 0
            for date in Clean_List:
                if date > CURR_DATE:
                    next_clean = date
                    break

            for i in range(1,no_tube_cycle):
                tube_date = pur_date + datetime.timedelta(days = TUBE_FLUID*7*i)
                Tube_List.append(tube_date)

            next_tube = 0
            for date in Tube_List:
                if date > CURR_DATE:
                    next_tube = date
                    break

            date_temp = pur_date
            for i in range(1,30):
                inspect_date = FDateDateInspect(date_temp)
                Inspect_List.append(inspect_date)
                date_temp = inspect_date

            next_inspect = 0
            for date in Inspect_List:
                if date > CURR_DATE:
                    next_inspect = date
                    break

            salv_val = unit_cost * SALV_RATE
            no_mths = USE_LIFE*12
            mon_amort = (unit_cost - salv_val)/no_mths

            #Output

            print()
            print()
            print ("----------------------------------------------------------------------------")
            print()
            print("                                 XYZ COMPANY")
            print()
            print(f"TODAY'S DATE:     {curr_date_dsp}")
            print()
            print(f"UNIT ID:          {unit_name}")
            print(f"COST OF PURCHASE: {unit_cost_dsp}")
            print(f"DATE OF PURCHASE: {pur_date_dsp}")
            print()
            print ("----------------------------------------------------------------------------")
            print("CLEANING:")
            print()
            
            if CURR_DATE > (pur_date + datetime.timedelta(days=B_CLEAN)):
                print (f"The first basic cleaning took place on {Display(Clean_List[0])}.")
                print()
                print (f"The next basic cleaning will take place on {Display(next_clean)}.")
            else:
                print (f"The first basic cleaning will take place on {Display(next_clean)}.")
        
            print()
            print()    
            print("TUBE AND FLUID CHECKS:")
            print()

            if CURR_DATE > (pur_date + datetime.timedelta(days=TUBE_FLUID*7)):
                print (f"The first tube and fluid check took place on {Display(Tube_List[0])}.")
                print()
                print (f"The next tube and fluid check will take place on {Display(next_tube)}.")
            else:
                print (f"The first tube and fluid check will take place on {Display(next_tube)}.")

            print()
            print()
            print("MAJOR INSPECTION:")
            print()

            if CURR_DATE > Inspect_List[0]:
                print (f"The first major inspection took place on {Display(Inspect_List[0])}.")
                print()
                print (f"The next major inspection will take place on {Display(next_inspect)}.")
            else:
                print (f"The first major inspection check will take place on {Display(next_inspect)}.")

            print()
            print()
            print ("----------------------------------------------------------------------------")
            print (f"The salvage value is                    {Money(salv_val)}")
            print (f"The monthly amortization payment is     {Money(mon_amort)}")
            print()
            print("             AMORTIZATION SCHEDULE")
            print()
            print(" YEAR      AMOUNT PAID      AMOUNT REMAINING")
            for i in range(0, USE_LIFE+1):
                total_amort = mon_amort*12*i
                cost_remain = unit_cost - total_amort
                print (f" {i:>2d}      {Money(total_amort):>12}        {Money(cost_remain):>12} ")
            print (f" SUBTRACT SALVAGE VALUE LEAVES  {Money(cost_remain-salv_val)}  ")
            print()
            print ("----------------------------------------------------------------------------")
            print()
            print()
            if want_list == "Y":
                FullList()
            print()
            print()
            cont = input ("Enter 'End' to terminate program or hit return to continue.  ").capitalize()
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










