import sys 

#Import the input and make it an array spliting it by lines
input_txt = open("input.txt", "r")
input = input_txt.read()
input_txt.close()
input = input.splitlines()

#Variables definition
y = 0
x = 0
step_y = 1
step_x = 3
collisions = 0

#We define the x_max (lenght of the segment of the path they give us) for being able to replicate it
x_max = len(input[1])

#We define the number of loops it will have to do by the lenght - the start point +1 (+1 means that it start inside of the map)
iterations = len(input) - (y + 1)

#PRINCIPAL LOOP
for i in range(iterations):
    #We take the sum of the steps
    y += step_y
    x += step_x
    
    #If we find a tree we add one to the collisions var
    if input[y][x % x_max] == '#':
        collisions += 1

#Print Results
print("----End Reached----")
print("Total Collisions: {}".format(collisions)) 

#TERMINAL
# ----End Reached----
# Total Collisions: 294
    
    




