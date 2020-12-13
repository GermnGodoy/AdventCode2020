
import sys

input_txt = open("input.txt", "r")
input = input_txt.read()
input_txt.close()

#Split the input in an array one field for each document
input = input.split('\n\n')

#Take the iterations(number of documents)
iterations = len(input)
valids = 0



#cid = False 

for i in range(iterations):

    #Passport fields
    byr = False 
    iyr = False 
    eyr = False 
    hgt = False 
    hcl = False 
    ecl = False 
    pid = False 

    #Take the fields that a document have
    doc = input[i].split()

    for e in range(len(doc)):
        #Take just the field name
        field = doc[e].split(":")
        field = field[0]

        #Check if the field name matches one of the fields if it does we will put a true in the field value
        if field == 'byr':
            byr = True
        elif field == 'iyr':
            iyr = True
        elif field == 'eyr':
            eyr = True
        elif field == 'hgt':
            hgt = True
        elif field == 'hcl':
            hcl = True
        elif field == 'ecl':
            ecl = True
        elif field == 'pid':
            pid = True
    
    #After checking all the fields of a doc we check if the doc has had all of them if it has we add one to the valids
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valids += 1
    
#We print results on the screen
print("---Validation--Finished---")
print("There are {} valid documents".format(valids))


#TERMINAL
# ---Validation--Finished---
# There are 228 valid documents