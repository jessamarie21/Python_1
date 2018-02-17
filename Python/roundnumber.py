#This function takes a decimal and rounds it up or down to a whole number

def my_round(number):
'''(number) --> (string)

Returns decimal rounded to an integer and saved as a string
'''

    if number < (number//1 + 0.5):
        b = number//1
    elif number >= (number//1 + 0.5):
        b = number//1 + 1
    print(str(b))

number = float(input("Please enter a number: "))
my_round(number)
