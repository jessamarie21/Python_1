def backwards():
    L = []
    word = 'hoobla'
    New_word = ''
    for x in range(len(word)):
        L.append(word[x])
    for y in range(-1,-len(L)-1,-1):
        New_word += L[y]
    return New_word

def smallest():
    L = [-3,4,-2,1,5,0]
    smallest = 0
    for x in range(len(L)):
        index = L[x]
        if index < smallest:
            smallest = index
    return smallest

def LCM():
    b = 3
    c = 5
    x = True
    a = 0
    if b > c:
        big = b
        small = c
    else:
        big = c
        small = b
    if big % small == 0:
        for i in range(big):
            d = small * i
            if d == big:
                LCM = d
        return LCM
    while x == True:
        a += 1
        b *= a
        c *= a
        if b == c:
            LCM = b
            x = False
    return LCM
        
def count_letters(word):
    
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1
    return count
word = "jessa"

days = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

def code():
    items = ["up", "down", "left", "right", "forward", "backward"]
    suffix = ''
    for item in items:
        item = item + suffix
        suffix = suffix + '.'
    print("Items are: ", items)

dictionary1 = {}
dictionary1["tomato"] = "fruit"
dictionary1["apple"] = "fruit"
dictionary1["potato"] = "vegetable"
dictionary1["tomato"] = "vegetable"

L1 = [1,2,3,4,5]

string = "Peanut butter and chocolate chunk cookie"

def switch():
    newspeak = {"key1":"value1", "key2":"value2", "key3":"value3"}
    keys = list(newspeak.keys())
    values = list(newspeak.values())
    the_book = "I key1 and key2 like key3 key1 key2"
    list_the_book = the_book.split()
    for x in range(len(list_the_book)):
        for y in range(len(keys)):
            if list_the_book[x] == keys[y]:
                list_the_book[x] = values[y]
    the_book = ''
    for x in range(len(list_the_book)):
        the_book += list_the_book[x] + ' '
    return the_book

def replace():
    input_str = "jesasisosu"
    output_str = ''
    list_input_str = list(input_str)
    vowels = ['a','e','i','o','u']
    length = len(input_str)
    z = 0
    while z < length:
        for y in range(len(vowels)):
            if list_input_str[z] == vowels[y]:
                del list_input_str[z]
        if length == len(list_input_str):
            z += 1
        else:
            length -= 1
    for x in range(len(list_input_str)):
        output_str += list_input_str[x]
    return output_str
print(replace())
