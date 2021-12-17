from bs4 import BeautifulSoup as BS4   
import requests as req  
from datetime import date  


today = date.today()
link = "https://pulsee.it/offerte-casa-luce-gas"   
r1  = req.get(link)   
coverpage = r1.content   
soup1 = BS4(coverpage, "html.parser")   

print(soup1.prettify())   

price1 = soup1.find_all(class_="c-definition-list-alt__value")   

pricetoday = []  
for i in price1:
    pricetoday.append(i.text)
    
for i in price1:    
    print(i.text)
    
# write prices on a txt file, with mode "a"=append to keep the historical records 
with open("prezzi.txt", mode = "a", encoding= "UTF-8" ) as f:    
    #f.write(str(today)
    #f.write(str(pricetoday))
    f.writelines([str(today), str(pricetoday)]) 
