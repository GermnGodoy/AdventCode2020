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

    mint = int(policy[0])
    maxt = int(policy[1])

    #We check if the actual data is correct if it is we add one to the valid int
    if int(passwd.count(letter)) <= maxt and int(passwd.count(letter)) >= mint:
        valid+=1
    

print("We have found {} valid passwords".format(valid))

sys.exit()

#TERMINAL
# We have found 500 valid passwords
