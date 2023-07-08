import requests
import time
import datetime
import os
import pandas as pd    # import this lib if you want to run the dt.round function 

url = "https://google.com/"
count = 0

while True:
    
    status = requests.head (url)
    timestamp = time.time()
    #time_now = pd.Series(datetime.datetime.fromtimestamp(timestamp)).dt.round("1s") # rounded to seconds with Pandas
    time_now = datetime.datetime.fromtimestamp(timestamp) 
    
    # creating a txt file and appending the info
    with open ("status.txt", "a") as file:    
        file.write ("Count: " + str(count) + "\n")
        file.write (str(time_now) + "\n")
        file.write (str(status) + "\n" + "\n")
        count += 1
    
    time.sleep (3600)     # logging every 30 min 
