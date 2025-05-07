# Check Last Digit
# Write a program to check if the last digit of two numbers is the same.
num1=int(input("Enter a number"))
num2 =int(input("Enter a number"))


def is_last_digit_of_two_number_is_equal(n1,n2):
    for i in range(1):
        r1=n1%10
        r2=n2%10
        if r1==r2:
            return "last digit of two numbers is same"
        else:
            return "last digit of two numbers is not same"

print(is_last_digit_of_two_number_is_equal(num1,num2))