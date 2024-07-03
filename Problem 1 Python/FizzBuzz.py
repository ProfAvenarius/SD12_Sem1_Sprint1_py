#Description: A program that returns the FizzBuzz patern - 1 - 100 with Fizz replacing all  
#            multiples of 5, Buzz replacing multiples of 8 and FizzBuzz replacing multiples of 8 and 5.
#Author: Group 22(DCE, NP)
#Date: June 17 -26 

#No inputs, no functions, only output

def main():


    Mess_List = []
    turns =1
    x = [1,2,3,4]
    while turns < 101:
        if (turns % 5) == 0 and (turns % 8) == 0:
            message = "FizzBuzz"
        elif (turns % 8) == 0:
            message = "Buzz"
        elif (turns % 5) == 0:
            message = "Fizz"
        else:
            message = turns
        Mess_List.append(message)
        turns += 1
    print()
    print()  #The output was put into 5 columns simply to save screen space
    print()
    print ("THE FIZZBUZZ SOLUTION:")
    print ("(1 - 20)      (21 - 40)      (41 - 60)      (61 - 80)      (81 - 100)")  
    print()         
    for i in range(0,20):
        
        print (f"   {Mess_List[i]:<8}       {Mess_List[x[0]*20+i]:<8}       {Mess_List[x[1]*20+i]:<8}       {Mess_List[x[2]*20+i]:<8}       {Mess_List[x[3]*20+i]:<8}")
        i += 1
    print()
    print()
    print()
    print ("Running Fizzbuzz.")

if __name__ == "__main__":
    main()