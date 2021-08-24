url = "https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)"   #url of the target page with the images we want to acquire 

request = requests.get(url)   #create the request

soup = bs4.BeautifulSoup(request.text, "lxml")   #make the soup 

pic1 = soup.select(".thumbimage")[0]     #let's select the proper image tag from the html (first image)
pic2 = soup.select(".thumbimage")[1]     #let's select the proper image tag from the html (second image)

image_url1 = "https:"+pic1["src"]        #let's make the url for the request to grab the image (first image)
image_link1 = requests.get(image_url1)   #let's grab the image with a new GET request (first image)

image_url2 = "https:"+pic2["src"]        #let's make the url for the request to grab the image (second image)
image_link2 = requests.get(image_url2)   ##let's grab the image with a new GET request (second image)

with open ("computer_image.jpg", "wb") as f:    #lets' save the image (writing the binary input ("wb") to a new .jpg file)
    f.write(image_link1.content)
    
