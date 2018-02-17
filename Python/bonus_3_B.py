inventory = {}
sample = open("inventory_sample.txt", "r")
for line in sample:
    text = line.split(', ')
    if text[0] in inventory:
        print("Duplicate Entry of: " + text[0])
    
    inventory[text[0]] = text[1]
print(inventory)
sample.close()
