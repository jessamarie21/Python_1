marks = [78, 81, 45, 91, 85, 79, 63, 86, 67, 96, 52, 60, 81, 83, 65, 71, 90]
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
        print(result)
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(L):
    m=1
    while m < len(L):
        i= 0
        while i < len(L)-m:
            new = merge(L[i:i+m], L[i+m:min(i+2*m, len(L))])
            L[i:i+len(new)] = new
            i=i+2* m
        m=m* 2
        print(L)
    return L
merge_sort(marks)
##import time
##import random
##def random_generator():
##    L = []
##    for i in range(20000):
##        L.append(random.randrange(20000))
##    return L
##random_list = random_generator()
##    
##start_time = time.time()
##merge_sort(random_list)
##end_time = time.time()
##print(end_time - start_time)
