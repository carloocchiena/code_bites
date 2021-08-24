import re 
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# you can bind it to specific domains or format     


def check(email):
  if(re.search(regex,email)):
    print("Valid Email")  
  else:
    print("Invalid Email")  
      
