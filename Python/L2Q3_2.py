import L2Q3_1
def ast_array():
        '''(number,number) -> pattern * * *
        Returns pattern of asterisks and spaces on different rows based on the function asterisks()
        '''
	return L2Q3_1.asterisks(1,0) + '\n' + L2Q3_1.asterisks(2,1) + '\n' + 	L2Q3_1.asterisks(3,1)

print(ast_array())
	
