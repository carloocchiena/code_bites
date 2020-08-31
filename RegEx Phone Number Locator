def findit():
    
    import os  #import os to navigate thru folders
    import re  #import re for the regular expression library
    
    #this is the path we want to find, and it's a standard U.S phone number in the format ###-###-###
    search_path = ("\d{3}-\d{3}-\d{4}")
    
    count = 0 #just a token to count how many files we analyzed 

    # with os.walk we are able to "walk" in the folder structure in the desired folder. You can look for it with the os.getcwd() or os.listdir() 
    for folders, subfolders, files in os.walk('C:\\FOLDER\\SUBFOLDER 1\\SUBFOLDER 12\\SUBFOLDER 123\\SUBFOLDER 1234\\SUBFOLDER 12345\\'):
        for file in files:   #let's go work on the single files we found 
            file_path = os.path.join(folders, file)  #we use os.path.join to create a static uri for the single files otherwise single .txt won't be found
            with open (file_path) as content:   #let's open each single file 
                search_number = re.search(search_path, content.read())   #let's run the re.search function. Looks how we put content.read() otherwise the content of the file is not usable 
                if search_number:
                    count +=1
                    print (f"Searched Number: {search_number.group()}") #let's just print it 
                    print (f"File Location: {file_path}")
                else:
                    count +=1
    print (f"Item Scanned: {count}") #let's see how many item we analyzed 
