factor = 25
m = 0
f = 0
x = 0

input_txt = open('input.txt', 'r')

input = input_txt.read().splitlines()

control_var = True 

def tester(t, d, list):
    new_list = []
    for n in range(int(t), int(d)):
        new_list.append(list[n])
    
    max_item = max(new_list, key=int)
    min_item = min(new_list, key=int) 

    return (int(max_item) + int(min_item))


def stuff(number):
    input_txt = open('input.txt', 'r')
    r_input = input_txt.read().split(str(number))
    r_input = r_input[0].splitlines()
    global m 
    global x
    global f

    for r in range(len(r_input)):
        x = r
        m=0
        f=0
        while True:
            m += int(r_input[r + f])

            if m == int(number):
                return r, f
            
            elif m > int(number):
                break

            else:
                f += 1



for i in range(len(input) - factor):
    
    control_var = True 

    for e in range(factor):
        for t in range(factor):
            if control_var:
                if int(input[i + factor - e -1]) + int(input[i + factor - t -1]) == int(input[i + factor]) and e != t:
                    control_var = False
                else:
                    pass
            else:
                pass
                
    if control_var:
        print("The first error number is: {}".format(input[i + factor]))
        break
    else:
        pass
        
stuff(input[i + factor])

mini = str(x)
maxi = str(int(x)+int(f))

print("The result is: {}".format(tester(mini, maxi, input)))

