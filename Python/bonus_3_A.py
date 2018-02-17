dictionary = {}
dictionary['name'] = 'Jessa'
dictionary['number'] = '1000372438'
dictionary['course'] = 'csc180'
print(dictionary)
dict_list = list(dictionary.items())
for item in dict_list:
    print(item)
del dictionary['course']
print(dictionary)
