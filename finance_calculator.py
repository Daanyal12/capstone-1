#This program calculates:
#interest on investments
#homeloan repayments

#imports math functions
import math

#breakdown of what the program consists of and explains it to the user
print("welcome to FINCALC \n")
print("Choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("investment   - to calculate the amount of interest you'll earn on a investment ")
print("bond         - to calculate the amount you'll have to pay on a home loan ")

#user enters input here
i = str(input("enter here: "))
calcType = i.upper()

#conditions for the user to choose whether they want to use a bond calculator or interest calculator

#the if condition is created for the INVESTMENT option
if calcType == "INVESTMENT" :
    amount = float(input("enter the amount you'd like to deposit?: \n"))
    rate = float(input("enter the interest rate as a percentage (e.g. 10): \n"))
    r = rate/100
    years = float(input("how long would you like to invest for in years?: \n"))
    interest = input("simple or compound interest?: \n")
    i2 = interest.upper()

    #conditionals filter out whether the user wants to choose simple or compound interest
    #for simple function
    if i2 == "SIMPLE":
            S1 = (round(amount*(1+r*years)))
            print("your total interest simply is R{}".format(S1))

    #for compound function
    elif i2 == "COMPOUND":
            C1 = (round(amount * math.pow((1+r),years)))
            print("your total interest compounded is R{}".format(C1))

    #for if the user inputs nothing
    else:
        print("ERROR please select COMPOUND OR SIMPLE")

#the elif condition is created for the BOND option
elif calcType == "BOND" :
    hValue = float(input("enter the current value of the house: \n"))
    rate2 = float(input("enter interest rate: e.g 10: \n"))
    r2 = ((rate2 / 100)/12)
    months = float(input("the number of months E.g 120: \n"))
    repayments = (r2 * hValue)/(1 - (1+r2)**(-months))
    T2 = (round(repayments))
    print("your bond repayment each month will be R{}".format(T2))

#the else is the failsafe for if the user selects nothing
else:
    print("ERROR please select a valid option ('INVESTMENT' or 'BOND')")
