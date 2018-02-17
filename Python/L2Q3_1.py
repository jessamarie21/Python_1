#This function takes the number of spaces provided and the number of asterisks provided, and places the number of spaces between the asterisks.

def asterisks(n,m):
	'''(number,number)--> * * * *
	The function takes the number of spaces 'm' provided and adds 		it to an asterisk. Then it multiplies that string by the number of 		asterisks 'n' selected, producing a pattern of asterisks and spaces
	'''
	if n<1 or m<0:
		exit
	return (n*(('*')+m*(' ')))


