#This function returns the number of pennies left over after dividing it by all the possible coin breakdowns.  
  
def pennies_leftover(a):  
    '''(number) --> number 
    Takes any cost in canadian dollars, multiplies it by 100 to get the         number of pennies, and then divides it by 5 giving back the remainder. 
    '''  
    return int(a*100%5)  
  
#cost in canadian dollars  
  
a = float(input("Please input cost in CAD: "))  
  
#number of pennies leftover  
  
number_pennies_left = pennies_leftover(a)  
  
print(number_pennies_left)  
  
