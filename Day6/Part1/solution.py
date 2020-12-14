import sys 

#Oen the input txt and split it by groups (empty lines or '\n\n')
input_txt = open("input.txt", "r")
input = input_txt.read().split('\n\n')

#We declare those characters that mustnt be counted
invalid_chars = [' ', '\n'] 

#Total of afirmative answers
yes = 0

#MAIN LOOP
for i in range(len(input)):
    
    #List that takes the count of seen characters ina group
    had_char = []

    #Iterate every letter
    for e in range(len(input[i])):

        #If the letter hasnt appear before it will be added to had_char and we will have one more affirmative answer
        if input[i][e] not in had_char and input[i][e] not in invalid_chars:
            
            yes += 1
            had_char.append(input[i][e])

#Print result
print("The sum of all the affirmative answers is: {}".format(yes))


#TERMINAL   
# The sum of all the affirmative answers is: 6625
