import sys 

#Import the input and make it an array spliting it by lines
input_txt = open("input.txt", "r")
input = input_txt.read()
input_txt.close()
input = input.splitlines()

#Variables definition
y = 0
x = 0
step_y = 0
step_x = 0
collisions = 0
collisions_array = [0,0,0,0,0]
collisions_m = 1

#Because we have to check multiple options we will make an array with the steps options to iterate around it
steps_array = [[1,1] , [3,1] , [5,1] , [7,1] , [1,2]]

#We define the x_max (lenght of the segment of the path they give us) for being able to replicate it
x_max = len(input[1])

#PRINCIPAL LOOP
for e in range(len(steps_array)):
    #We put the step value
    step_x = steps_array[e][0]
    step_y = steps_array[e][1]

    y=0
    x=0
    collisions = 0

    #This time iterations must be inside the loop
    iterations = len(input) - (y + step_y)
    
    for i in range(iterations):
        #We take the sum of the steps
        y += step_y
        x += step_x

        if y > len(input):
            print("- We have fell apart")
            break
        
        #If we find a tree we add one to the collisions var
        if input[y][x % x_max] == '#':
            collisions += 1

    #We keep the value in an array and print it 
    collisions_array[e] = collisions
    print("- With the values of {} and {}, we take {} collisions".format(step_x, step_y, collisions))

#We get the product of all the collisions
for i in range(len(collisions_array)):
    collisions_m *= collisions_array[i]

#Print Results
print("----Process End Reached----")
print("Muliplied Collisions: {}".format(collisions_m)) 

#TERMINAL
# - With the values of 1 and 1, we take 75 collisions
# - With the values of 3 and 1, we take 294 collisions
# - With the values of 5 and 1, we take 79 collisions
# - With the values of 7 and 1, we take 85 collisions
# - We have fell apart
# - With the values of 1 and 2, we take 39 collisions
# ----Process End Reached----
# Muliplied Collisions: 5774564250
    
    




