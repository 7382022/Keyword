#take user input

a = input ("Enter a word")
#program to check break keyword
for i in a: #iterate for loop
    if (i == 'A' or i == 'a'): #condition 1
        #display result
        print ("A is found")
        break #break statement
    else:
    #display result
       print("A not found")