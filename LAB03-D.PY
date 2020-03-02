#
#OPEN FILE THAT WE WANT TO WRITE TO, SPCIFY THAT WE WANT TO APPEND TO IT
sumFile = open('SumTxt.txt', 'a') 
#CREATE A LOOP 
while True:
    x = input("Type first number or 'exit' to quit: ")
    if x.lower() == 'exit': break 
    y = input ("Type second number: ")
    summ = float(x) + float(y)
    sumFile.write(str(summ) + '\n')

sumFile.close()
