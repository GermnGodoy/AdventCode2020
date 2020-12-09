#Day 1 Solution
import sys 
#We define the number we want to get
goal=2020

#Read the input
input_txt = open("input.txt", "r")
input = input_txt.read()

#Clean the input
input = input.splitlines()

#We iterate through all the numbers in the input 
for i in range(len(input)):
    for e in range(len(input)):
        #We take the sum of the iteration numbers and if it is equal to 2020
        #we break the loop and take both numbers
        sum = int(input[i]) + int(input[e])
        if sum == goal:
            print("The numbers whose sum is {} are {} and {}".format(goal, input[i], input[e]))
            print("Their product is {}".format(int(input[i]) * int(input[e])))

            #After printing the result we leave the program
            sys.exit()





#TERMINAL RESULT
#The numbers whose sum is 2020 are 1751 and 269
#Their product is 471019

