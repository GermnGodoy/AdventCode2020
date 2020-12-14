import sys

#Open the file ans split it by lines (each line is a boarding pass)
input_txt = open("input.txt", "r")
input = input_txt.read().splitlines()
input_txt.close()

#BinString is the place where bin numbers will be stored
bin_string = ''

#Define the var where the highest id is going to be stored
high_id = 0

#MAIN LOOP
for i in range(len(input)):
    
    #Define the actual id and restore the bin_string
    id = 0
    bin_string = ''

    #Convert BFLR in binary
    for e in range(len(input[i])):
        if input[i][e] == 'B' or input[i][e] == 'R':
            char = '1'
        else:
            char = '0'

        bin_string += char
    
    #We separate the bins for the row and for the collum
    row = bin_string[0] + bin_string[1] + bin_string[2] + bin_string[3] + bin_string[4] + bin_string[5] + bin_string[6]
    column = bin_string[7] + bin_string[8] + bin_string[9] 

    #Convert bin into int
    result_row = int(row, 2)
    result_column = int(column, 2)

    #calculate ID
    id = result_row * 8 + result_column

    #Change the highest id if actual is greater
    if id > high_id:
        high_id = id

#Print Results
print("The highest id has ben: {}".format(high_id))


#TERMINAL
# The highest id has been: 826
