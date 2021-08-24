#check whether a given argument contains a set of parameters given in a list or an external dataset 

def checkletter(string):
    alfa=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","y","z"]
    string=string.lower()
    for i in string:
        if i in alfa:
            alfa.remove(i)
        if alfa==[]:
            return True
    print (alfa)
    
#check if a function is a palyndrome
def palindrome(s):
  return s==s[::-1]
      
#many ways to handle or check unique items in a list (given or as an input)
#as an input:
def nomeunico():
    lista=[]
    while len(lista)<10:
        name=input("inserisci un nuovo nome\n")
        if name in lista:
            print ("il nome è duplicato")
        else:
            lista.append(name)
            print ("ok inserito")

#given list:
lista =["carlo", "ragno", "tonno", "carlo", "tonno", "noce"]

#list comprehension method: 
dups = [x for x in lista if lista.count(x) > 1]

#using set() method:
unico=set()

for i in lista:
    if i in unico:
        print (f"elemento duplicato:{i}")
    else:
        unico.add(i)
        print (f"elemento aggiunto:{i}")
