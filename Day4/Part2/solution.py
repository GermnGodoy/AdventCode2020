
import sys
import re

input_txt = open("input.txt", "r")
input = input_txt.read()
input_txt.close()

#Split the input in an array one field for each document
input = input.split('\n\n')

#Take the iterations(number of documents)
iterations = len(input)
valids = 0

#Make a list of all the valid values of the colors
valid_hex = ('0','1','2','3','4','5','6','7','8','9', 'a','b','c','d','e','f')
valid_colors = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

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

        #Check if the field name matches one of the fields if it does we will put a true in the field value
        if field[0] == 'byr':
            
            #Check if the birthday is above 1920 and below 2002, if it is it must have 4 digits too
            if int(field[1]) >= 1920 and int(field[1]) <= 2002:
                byr = True 

        elif field[0] == 'iyr':

            #Check if the issue year is above 2010 and below 2020, if it is it must have 4 digits too
            if int(field[1]) >= 2010 and int(field[1]) <= 2020:
                iyr = True

        elif field[0] == 'eyr':

            #Check if the expiration year is above 220 and below 2030, if it is it must have 4 digits too
            if int(field[1]) >= 2020 and int(field[1]) <= 2030:
                eyr = True

        elif field[0] == 'hgt':

            #With regEx we check if the height ends with 'cm' or with 'in'            
            if re.search("cm$", field[1]):
                field[1] = field[1].split('c')
                height = int(field[1][0])
                
                #If it ends with cm we take the number and check if it is in range [150, 193]
                if height >= 150 and height <= 193:
                    hgt = True 

            elif re.search("in$", field[1]):
                field[1] = field[1].split('i')
                height = int(field[1][0])

                #If it ends with in we take the number and check if it is in range [59, 76]
                if height >= 59 and height <= 76:
                    hgt = True 

        elif field[0] == 'hcl':

            #With regEx we check if the hair color starts with '#'
            if re.search("^#", field[1]):
                
                #If it does we check if it is 7 of lenght (6 digits + the '#')
                if len(field[1]) == 7:
                    #We define is_hex
                    is_hex = True 

                    for d in range(5):
                        
                        #If the value given to a digit is not possible for hex, is_hex will be false and it will stop checking
                        if field[1][d+1] in valid_hex:
                            pass 
                        else:
                            is_hex = False 
                            break
                    
                    #If after the checking is_hex is true the value is valid so hcl is True
                    if is_hex:
                        hcl = True

        elif field[0] == 'ecl':

            #We check if the eye color is in the valid values list for it
            if field[1] in valid_colors:
                ecl = True
            
        elif field[0] == 'pid':

            #Checks if the Country ID is 9 digits
            if len(field[1]) == 9:
                pid = True
    
    
    #After checking all the fields of a doc we check if the doc has had all of them correctly if it has we add one to the valids
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valids += 1
    
#We print results on the screen
print("---Validation--Finished--Again---")
print("--There are {} valid documents--".format(valids))


#TERMINAL
# --Validation--Finished--Again---
# --There are 175 valid documents--