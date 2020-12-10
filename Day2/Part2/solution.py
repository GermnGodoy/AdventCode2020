import sys

#We open the input and we split it by lines 
raw_input = open("input.txt", "r") 


input = raw_input.read()
input = input.splitlines()

raw_input.close()

#We define valid int that will be the amount of correct passwords
valid = 0

for i in range(len(input)):

    #We take the necesary data by spliting each line of the input
    line = input[i]

    line = line.split(":")

    policy = line[0]
    passwd = line[1]

    policy = policy.split()

    letter = policy[1]
    policy = policy[0]

    policy = policy.split("-")

    pos1 = int(policy[0])
    pos2 = int(policy[1])

    #We check if the actual data is correct if it is we add one to the valid int
    if  passwd[pos1] == letter and passwd[pos1] != passwd[pos2] or passwd[pos2] == letter and passwd[pos1] != passwd[pos2]:
        valid+=1
    

print("We have found {} valid passwords with the new policy".format(valid))

sys.exit()

#TERMINAL
# We have found 313 valid passwords with the new policy
