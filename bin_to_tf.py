# bnkosi
# Jan 2020

var_list = ['a', 'b', 'c']
line = []
num_of_rows = len(var_list) ** 2
widest_num = len(str(bin(num_of_rows - 1)[2:]))

for i in reversed(range(num_of_rows)):
    current_bin = bin(i)[2:].zfill(widest_num)
    for letter in str(current_bin):
        if letter == '0':
            line.append('False')
        elif letter == '1':
            line.append('True')

print(line)