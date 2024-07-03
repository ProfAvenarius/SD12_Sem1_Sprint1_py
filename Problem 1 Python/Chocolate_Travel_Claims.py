#Description: A program designed for NL Chocolate Company to produce travel claims for employees.
#Author: Group 22 (DCE, NP)
#Date: Jun 17 - 26

#Program libraries
import datetime


#Program constants
PER_DIEM_RATE = 85.00

MILEAGE_OWN_RATE = 0.17
MILEAGE_RENT_RATE = 65.00

MILEAGE_BONUS_RATE=0.04
EXEC_BONUS_RATE = 45.00
XMAS_BONUS_RATE = 50.00

CURR_DATE = datetime.date.today()
CURR_YEAR = CURR_DATE.year

XMAS_DATE1 = datetime.datetime(CURR_YEAR, 12, 15)
XMAS_DATE2 = datetime.datetime(CURR_YEAR, 12, 22)

HST_RATE = 0.15

BONUS = 0.00


#Program functions

def FDate(userdate):
    #Function to turn string object to date object
    day = int(userdate[0:2])
    month = int(userdate[3:5])
    year =int(userdate[6:10])
    date_dsp = datetime.datetime(year, month, day)
    return date_dsp

def Money(enter_num):
    #Formats a float into a cash value.
    price_dsp = "${:,.2f}".format(enter_num)
    return price_dsp



def main():
    #Every program is contained within a main function to allow Main Menu to make repeated calls.  
    print()  
    print()
    print("**************************************************************************************")
    print()
    print("Welcome to the  NL Chocolate Company's employee travel expense program, complete the")
    print("fields below to generate a travel claim amount.")
    print("Enter 'End' in employee's number to exit.")    # Every Program can be terminated at beginning
    print()                                               # and the end. This allows user to end program 
    print()                                               # immediately after choice from Main Menu.
    print()
    print()


    #User imputs    Inputs are validated
    while True:
        print()
        employ_num = input("Enter the employee number (99999):                              ").capitalize()
        if employ_num == "End":
            break
        elif len(employ_num) != 5:
            print ("Data Entry Error: Employee number must be 5 digits. ")
        elif employ_num.isnumeric() == False:
            print ("Data Entry Error: Employee number must be numeric characters. ")
        else:
            

            while True:
                print()
                first_name = input("Enter the employee's first name:                                ").capitalize()
                if first_name == "":
                    print ("Data Entry Error: First name cannot left be blank. ")
                elif first_name.isalpha() == False:
                    print ("Data Entry Error: First name must be alphbetic characters. ")
                else:
                    break
            
            while True:
                print()
                last_name = input("Enter the employee's last name:                                 ").capitalize()
                if last_name == "":
                    print ("Data Entry Error: Last name cannot be left blank. ")
                elif last_name.isalpha() == False:
                        print ("Data Entry Error: Last name must be alphbetic characters. ")
                else:
                    break

            while True:
                print()
                loco_trip = input("Enter the destination of the trip:                              ").title()
                if loco_trip == "":
                    print ("Data Entry Error: Manufacturer cannot be left blank.")
                else:
                    break

            while True:   #This while loop allows two date entries to be compared.

                while True:
                    print()
                    start_date = input("Enter the start date of the trip (DD-MM-YYYY):                  ")
                    d1_test = start_date[0:2]
                    m1_test = start_date[3:5]
                    y1_test = start_date[6:10]
                    if len(start_date) != 10:
                        print ("Data Entry Error: Start date must be in the form XX-XX-XXXX.")
                    elif d1_test.isnumeric() == False or m1_test.isnumeric() == False or y1_test.isnumeric() == False:
                        print ("Data Entry Error: All date fields must be completed numerically, example 01-01-2024.")
                    else:
                        break

                while True:
                    print()
                    end_date = input("Enter the end date of the trip (DD-MM-YYYY):                    ")
                    d2_test = start_date[0:2]
                    m2_test = start_date[3:5]
                    y2_test = start_date[6:10]
                    if len(start_date) != 10:
                        print ("Data Entry Error: End date must be in the form XX-XX-XXXX.")
                    elif d2_test.isnumeric() == False or m2_test.isnumeric() == False or y2_test.isnumeric() == False:
                        print ("Data Entry Error: All date fields must be completed numerically, example 01-01-2024.")
                    else:
                        break

                if FDate(end_date) < FDate(start_date):
                    print ("End date must come after Start Date, check and reenter.")
                else:
                    break


            while True:
                print()
                vehicle_status = input("Did the employee Own or Rent the vehicle used (O or R):         ").capitalize()
                if vehicle_status != "O" and vehicle_status != "R":
                    print ("Data Entry Error: Rental status entry must be 'O' or 'R'.")
                else:
                    break
                
            while True:
                print()
                total_kms = input("Enter the total vehicle mileage accumulated during the trip:    ")
                if total_kms == ():
                    print ("Data Entry Error: Milage cannot be left blank. ")
                elif total_kms.isnumeric() == False:
                    print ("Data Entry Error: Sell price must be numeric characters. ")
                else:
                    break

            while True:
                print()
                claim_type = input("Enter the claim type Standard or Executive (S or E):            ").capitalize()
                if claim_type != "S" and claim_type != "E":
                    print ("Data Entry Error: Rental status entry must be 'S' or 'E'.")
                else:
                    break

        #Program calculations

            total_kms = int(total_kms)

            full_name = (f"{last_name}, {first_name}")


            start_date_full = FDate(start_date)
            end_date_full = FDate(end_date)

            num_days = (end_date_full-start_date_full).days

            if claim_type == "S":
                claim_type_dsp = "Standard"
            if claim_type == "E":
                claim_type_dsp = "Executive"

            start_date_dsp = start_date_full.strftime("%A %b, %d, %Y")
            end_date_dsp = end_date_full.strftime("%A %b, %d, %Y")


            per_diem_amt = num_days * PER_DIEM_RATE
            per_diem_amt_dsp =Money(per_diem_amt)

            if vehicle_status == "O":
                mileage_amt = MILEAGE_OWN_RATE * total_kms
            if vehicle_status == "R":
                mileage_amt = MILEAGE_RENT_RATE * num_days
            mileage_amt_dsp = Money(mileage_amt)
        

            bonus_amt = BONUS
            if num_days >= 3:
                bonus_amt += 100.00
            if total_kms > 1000 and vehicle_status == "O":
                bonus_amt += (total_kms * MILEAGE_BONUS_RATE)
            if claim_type == "E":
                bonus_amt += (EXEC_BONUS_RATE * num_days)
            if XMAS_DATE1 <= start_date_full  <= XMAS_DATE2:
                bonus_amt += (XMAS_BONUS_RATE* num_days)
            bonus_amt_dsp = Money(bonus_amt)


            claim_amt = per_diem_amt + mileage_amt + bonus_amt
            claim_amt_dsp = Money(claim_amt)


            HST_amt = claim_amt * HST_RATE
            HST_amt_dsp = Money(HST_amt)

            claim_total = claim_amt + HST_amt
            claim_total_dsp = Money(claim_total)

            #Program Outputs
            print()
            print()
            print()
            print()
            print()
            print ("----------------------------------------------------------------------------")
            print ()
            print ("The Newfoundland Chocolate Company")
            print (f"Today's Date: {CURR_DATE}")
            print()
            print (f"Employee:           {full_name}   #{employ_num}")
            print (f"Destination:        {loco_trip}")
            print()
            print (f"Travel Start Date:  {start_date_dsp}")
            print (f"Travel End Date:    {end_date_dsp}")
            print()
            print (f"Total days travel:  {num_days} days")
            print (f"Claim Type:         {claim_type_dsp}")
            print ()
            print (f"                                                 --------------------------    ")
            print (f"Per-diem                                         {per_diem_amt_dsp}")
            print (f"Milage                                           {mileage_amt_dsp}")
            print (f"Bonus                                            {bonus_amt_dsp}")
            print (f"                                                 --------------------------   ")
            print (f"Subtotal                                         {claim_amt_dsp}")
            print (f"HST                                              {HST_amt_dsp}")
            print (f"                                                 --------------------------   ")
            print (f"Claim Total                                      {claim_total_dsp}")
            print ()
            print ()
            print ("----------------------------------------------------------------------------")
            print()
            print()
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
