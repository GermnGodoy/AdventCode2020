input_txt = open("input.txt", "r")
input = input_txt.read().splitlines()
input_txt.close()

main_dic = {} 
new_dic = {}
total_shinies = 0
hola = 0


def shynies(bag, main_dic):
    value = 0
    a = 0 
    global total_shinies

    if main_dic[bag] == 0:
            print("0 FOUND")
            a=int(1)
            print("Finished {}".format(bag))
            return a 
    else:
        for key in main_dic[bag]:
            
            if key in main_dic:
                print("REPETING PROCESS WITH {}".format(key))
                a=int(main_dic[bag][key]) * shynies(key, main_dic)
                print("The above bag contains: {}".format(int(main_dic[bag][key])))
                print("Total shinies inside: {}".format(total_shinies))
            total_shinies = a + 1
            print("Total Shinies = {}".format(total_shinies))

    print("Finished {}".format(bag))
    return total_shinies

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
    print("The bag is {}".format(bag))
    print(dic)
    main_dic[bag] = dic


print(main_dic['shiny gold'])




print("-----Analizes bag is {}-----".format("Shiny Gold"))
hola = int(shynies('shiny gold', main_dic))

print("The amount of bags in a shiny is {}".format(hola))