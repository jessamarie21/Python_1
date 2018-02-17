#This function mag_complex finds the magnitude of a complex number and returns it as the mag_value

def mag_complex(a,b):
	''' (number, number) -> number
	Returns the magnitude of a complex number
	It reads separately the real and imaginary parts of a complex number
	'''
	return((a**2 + b**2)**(1/2))

#Takes a number for 'a' as the real part of the complex number

a = float(input("Please input a number for 'a': "))

#Takes a number for 'b' as the imaginary part of the complex number

b = float(input("Please input a number for 'b': "))

#Prints the value of the magnitude of the complex number

mag_value = print(mag_complex(a,b))





