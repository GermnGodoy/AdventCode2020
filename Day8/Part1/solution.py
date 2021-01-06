factor = 25

input_txt = open('input.txt', 'r')

input = input_txt.read().splitlines()

control_var = True 

for i in range(len(input) - factor):
    
    control_var = True  

    print('-------\n  {}\n-------'.format(input[i + factor]))

    for e in range(factor):
        for t in range(factor):
            if control_var:
                if int(input[i + factor - e -1]) + int(input[i + factor - t -1]) == int(input[i + factor]) and e != t:
                    control_var = False
                    print('· {} + {}'.format(input[i + factor - e], input[i + factor - t]))

                else:
                    pass
            else:
                pass
                
    if control_var:
        print("The first error number is: {}".format(input[i + factor]))
        break
    else:
        pass
        