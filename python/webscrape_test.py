import urllib
import urllib2
 
#import this to open search results for viewing
import webbrowser
 
#'item' is the key for form input field, for more fields keep adding elements in dictionary
search = urllib.urlencode({'item': 'Python'})
 
#url of form submission - mentioned in action attribute of form
url = 'http://www.wordreference.com/'
full_url = url + '?' + search
response = urllib2.urlopen(full_url)
 
#Get the result on form submission in response
with open("search-results.html", "w") as f:
    f.write(response.read())
 
#open the contents in browser 
webbrowser.open("search-results.html")
 
 
#For better understanding view source of the website
