import sys
import numpy as np

#Import the txt and split it by lines
input_txt = open("input.txt", "r")
input = input_txt.read().splitlines()
input_txt.close()

#Declare bin_string
bin_string = ''

#Declares an array with all the possible ids
id_array = np.zeros(827)

#MAIN LOOP
for i in range(len(input)):

    #Set string and actual id to empty
    id = 0
    bin_string = ''

    #Convert BFLR into bin
    for e in range(len(input[i])):
        if input[i][e] == 'B' or input[i][e] == 'R':
            char = '1'
        else:
            char = '0'

        bin_string += char

    #Store the actual row and column
    row = bin_string[0] + bin_string[1] + bin_string[2] + bin_string[3] + bin_string[4] + bin_string[5] + bin_string[6]
    column = bin_string[7] + bin_string[8] + bin_string[9]

    #Convert bin to int  
    result_row = int(row, 2)
    result_column = int(column, 2)

    #calculate actual id
    id = result_row * 8 + result_column

    #Change the index id of the array to 1 (ocupied)
    id_array[id] = 1

#So the result will be the only index with a 0 (unocupied)
a=np.where(id_array == 0)
print(a)
