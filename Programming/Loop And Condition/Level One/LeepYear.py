# 11. Check Leap Year
# Write a function that checks whether a given year is a leap year or not using conditions.
def isLeapYear(y):
    if y<0:
        print("Enter Positive number")
    elif (y%4==0 and y%100!=0) or (y%400==0):
        print("Given year is leap year")
    else:
        print("Given year is not a leap year")



year=int(input("Enter a year to check weather given year is leap year or not: "))
if year>0:
    isLeapYear(year)
else:
    print("The given number is negative! Please try again")
