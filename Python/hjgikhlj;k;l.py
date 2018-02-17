def my_round(number):
'''(float)-->string
Returns a decimal rounded to a whole number as a string
'''
    if number < (number//1 + 0.5):
	b = number//1
    elif number >= (number//1 + 0.5):
	b = number//1 + 1
    print(str(b))

number = float(input("please enter a number :"))
my_round(number)
