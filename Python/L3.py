#This function takes a grade in letter form and returns it as a number
def convert_letter_to_number(course):
    '''(str) -> float
    Returns the value of the letter grade in terms of GPA
    '''
    
    if course == 'A+':
        return 4.0
    elif course == 'A':
        return 4.0
    elif course == 'A':
        return 3.7
    elif course == 'B+':
        return 3.3
    elif course == 'B':
        return 3.0
    elif course == 'B-':
        return 2.7
    elif course == 'C+':
        return 2.3
    elif course == 'C':
        return 2.0
    elif course == 'C-':
        return 1.7
    elif course == 'D+':
        return 1.3
    elif course == 'D':
        return 1.0
    elif course == 'D-':
        return 0.7
    elif course == 'F':
        return 0.0

#This function calculates GPA by taking input from a user
def calculate_gpa():
    ''' (int,str,float) -> float
    Takes the number of courses as an integer,
    the letter grades for each course,
    and the weight of each course as a float.
    Returns GPA.
    '''
    if __name__ == '__main__':
        n = int(input('Please input number of courses: '))
        grade_sum = 0
        weight_sum = 0
        for course_index in range(1,n+1,1):
            grade = input('Please enter course grade %d in letters: '%course_index)
            x = convert_letter_to_number(grade)
            print(x)
            weight = float(input('Please enter course weight %d in decimal form: '%course_index))
            grade_weight = float(weight*x)
            grade_sum += grade_weight
            weight_sum += weight
        gpa = float(grade_sum/weight_sum)
        print('Your GPA is', gpa)

calculate_gpa()


