import random

def scramble(in_filename, out_filename):
    index = 1
    for line in in_filename:
        out_filename.append(str(index) + ':' + line)
        index += 1
    
if __name__ == '__main__':
    in_filename = open('test_s_input.txt', 'r')
    out_filename = open('shuffled_file.txt', 'w')
    scramble(in_filename, out_filename)
