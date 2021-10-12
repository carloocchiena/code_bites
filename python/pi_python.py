#find first numbers of pi

k = 1
pi = 0
  
for i in range(1000000): 
    if i % 2 == 0: 
        pi += 4/k 
    else: 
        pi -= 4/k 
    k += 2
      
print(pi) 
