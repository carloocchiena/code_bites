import requests
import bs4
import lxml
import re

urls = ("https://www.repubblica.it", "https://www.ilsecoloxix.it/")


for url in urls: 
    result = requests.get(url)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    links = soup.findAll('a', attrs={'href': re.compile("^http://")})
    links_clean= []
    for link in links:
        links_clean.append(link.get("href"))
    for link in links:
        print (link.get('href'))
    broken_links = []
    for link in links_clean:
        try:
            requests.get(link, timeout=10).status_code
            if requests.get(link, timeout=10).status_code != 200:
                broken_links.append(link)
        except requests.exceptions.RequestException as e:
            print (e)
