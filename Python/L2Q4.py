#This function takes two positive integers and finds the greatest common divisor of the two.

def gcd(a,b):
    '''(number, number) -> number
    Takes two positive integers.
    Returns the greatest common divisor between the two integers.
    '''
    if a<0 and b<0:
        print("The number you entered is not positive")
        return
    elif a%1!=0 and b%1!=0:
        print("The number you entered is not an integer")
        return
    while a:
        b,a = a,b%a
    return b
a = int(input("Please enter a positive integer: "))
b = int(input("Please enter a positive integer: "))

number = print(gcd(a,b))
