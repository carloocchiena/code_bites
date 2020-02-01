days=[]
months=[]
years=[]
palindromebeta=[]
palindrome=[]

#create days
for i in range (1,32):
    if i < 10:
        days.append("0"+str(i))
    else:
        days.append(str(i))

#create months
for i in range (1,13):
    if i < 10:
        months.append("0"+str(i))
    else:
        months.append(str(i))

#create years
for i in range (1000,2300):
    if len(str(i))==1:
        years.append("000"+str(i))
    elif len(str(i))==2:
        years.append("00"+str(i))
    elif len(str(i))==3:
        years.append("0"+str(i))
    else:
        years.append(str(i))

#verify if palindrome        
palindromebeta=[]        
for day in days:
    for month in months:
        for year in years:
            if day + month + year == year[::-1] + month[::-1] + day[::-1]:
                palindromebeta.append(day+month+year)

#create a clean list with date dd/mm/yyyy format                
for i in palindromebeta:
    palindrome.append(i[0:2]+"/"+i[2:4]+"/"+i[4:9])
    
                
print (palindrome)            
