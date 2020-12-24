input_txt = open("input.txt", "r")
input = input_txt.read().splitlines()
input_txt.close()

main_dic = {} 
new_dic = {}
total_shinies = 0


def shynies(bag, main_dic, new_dic):
    value = 0
    for key in main_dic[bag]:

            if key[-1] == 's':
                key = key[:len(key)-1]
            
            if key not in main_dic:
                value += 1
            else:
                l = shynies(key, main_dic, new_dic)
                value += l 
                l = 0
    
    new_dic[bag] = value
    print("{} contains {} shynies".format(bag, new_dic[bag]))
    return value
    


#DEFINE
for i in range(len(input)):
    input[i] = input[i].split(" bags contain ", 1)
    bag = input[i][0]
    dic = {}

    input[i][1] = input[i][1].strip(".").split(",") 

    for e in range(len(input[i][1])):
        if 'no other bags' in input[i][1][e]:
            dic = 0
        else:
            for letter in range(len(input[i][1])):
                if input[i][1][letter] == 's':
                    input[i][1][letter] = ''
            if input[i][1][e][0] == ' ':
                input[i][1][e] = input[i][1][e][1:]
            input[i][1][e] = input[i][1][e].split(" ", 1)

            if " bags" in input[i][1][e][1]:
                            input[i][1][e][1] = input[i][1][e][1].replace(" bags", "")
            elif " bag" in input[i][1][e][1]:
                input[i][1][e][1] = input[i][1][e][1].replace(" bag", "")
            
            dic[input[i][1][e][1]] = input[i][1][e][0]
        
    
    main_dic[bag] = dic




print("-----Analizes bag is {}-----".format("Shiny Gold"))
shynies('shiny gold', main_dic, new_dic)

for bag in new_dic.keys():
    if int(new_dic[bag]) > 0:
        total_shinies += 1 
    
print("The amount of shinies is {}".format(total_shinies))