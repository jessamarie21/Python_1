def play():
    grid_size = 0
    while grid_size != 4 or grid_size != 9 or grid_size !=16:
        grid_size = int(input("Please enter a square number between 4 and 16: "))
        if grid_size == 4 or grid_size == 9 or grid_size == 16:
            return grid_size
    return grid_size

def show():
    grid_size = play()
    m = int(grid_size**0.5)
    n = '' 
    for j in range(grid_size):
        for i in range(m):
            n += '0 ' * m
            n = n.rstrip(' ') + '|'
        n = n.rstrip('|') + '\n'
        if (j + 1) % m == 0 and j != grid_size - 1:
            n += (grid_size * 2 - 1)* '-' + '\n'      
    print(n)

    
        

