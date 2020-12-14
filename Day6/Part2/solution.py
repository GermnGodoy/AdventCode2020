import sys 

#Oen the input txt and split it by groups (empty lines or '\n\n')
input_txt = open("input.txt", "r")
input = input_txt.read().split('\n\n')

#We declare those characters that mustnt be counted
invalid_chars = [' ', '\n'] 

#Total of afirmative answers
yes = 0

had_chara = []

#MAIN LOOP
for i in range(len(input)):
    
    #List that takes the count of seen characters ina group

    input[i] = input[i].split('\n')

    had_chara = []

    #Iterate every person
    for e in range(len(input[i])):
        
        if e==0:
            print("The input is {}".format(input[i][e]))
            for d in range(len(input[i][e])):
                if input[i][e][d] not in had_chara:
                    had_chara.append(input[i][e][d])
                    print("Added {}".format(input[i][e][d]))
                
        else:
            print(had_chara)
            for t in range(len(had_chara) - 1):
                if had_chara[t] not in input[i][e]:
                    print("Popped {}".format(had_chara[t]))
                    had_chara.pop(t)
            
            for t in range(len(had_chara)- 1):
                yes += 1
                    



#Print result
print("The sum of all the affirmative answers is: {}".format(yes))


#TERMINAL   
# The sum of all the affirmative answers is: 6625
