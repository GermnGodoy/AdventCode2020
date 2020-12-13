import sys
import numpy as np

input_txt = open("input.txt", "r")
input = input_txt.read().splitlines()
input_txt.close()

sites = np.zeros((128, 8))

string = ''

high_id = 0

for i in range(len(input)):
    id = 0
    string = ''
    for e in range(len(input[i])):
        if input[i][e] == 'B' or input[i][e] == 'R':
            char = '1'
        else:
            char = '0'

        string += char

    row = string[0] + string[1] + string[2] + string[3] + string[4] + string[5] + string[6]
    column = string[7] + string[8] + string[9] 
    result_row = int(row, 2)
    result_column = int(column, 2)

    id = result_row * 8 + result_column

    if id > high_id:
        high_id = id

    sites[result_row][result_column] = 1


print(column)
print(row)
print(result_column)
print(result_row)
print(high_id)
