def my_round(number):
'''(float) --> string

Returns the given decimal as a rounded integer.
'''
    if number < (number//1 + 0.5):
        b = number//1
    elif number >= (number//1 + 0.5):
        b = number//1 + 1
    print(str(b))

number = float(input('Please enter number: '))
my_round(number)

