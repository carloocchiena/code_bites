
file1 = open('text_file.txt', 'r')
lines = file1.readlines()
 
i = 0
if i <= (len(lines)-3):
    while i in range(len(lines)):
        print (f"Hello, your name is {lines[i][:-1]}, you are {lines[i+1][:-1]} years old and you likes: {lines[i+2][:-1]}")
        i +=4
file1.close()
