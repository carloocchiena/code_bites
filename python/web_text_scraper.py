from bs4 import BeautifulSoup as BS4  
import lxml
import requests as req


url = 'https://smarttrack.io/'

url_list = ['https://smarttrack.io/', \
            'https://smarttrack.io/prodotti/best-safe/', \
            'https://smarttrack.io/prodotti/connected-worker/', \
            'https://smarttrack.io/casi-d-uso/', \
            'https://smarttrack.io/progetti-di-ricerca/', \
            'https://smarttrack.io/faq/', \
            'https://smarttrack.io/azienda/', \
            'https://smarttrack.io/case-history/', \
            'https://smarttrack.io/contatti/', \
            'https://smarttrack.io/training/']


def tag_scraper(url):
    """
    To get all  the elements in a web page, grouped for HTML tag type (not in page order).
    """

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}

    content = req.get(url, "html.parser", headers=header ).content
    soup = BS4(content, "lxml")  
   
    h1_raw = soup.find_all('h1')
    h2_raw = soup.find_all('h2')
    h3_raw = soup.find_all('h3')
    h4_raw = soup.find_all('h4')
    p_raw = soup.find_all('p')

    try:
        h1 = [h1.get_text() for h1 in h1_raw]
    except Exception as e:
        h1 = 'Parameter not found'

    try:
        h2 = [h2.get_text() for h2 in h2_raw]
    except Exception as e:
        h2 = 'Parameter not found'

    try:
        h3 = [h3.get_text() for h3 in h3_raw]
    except Exception as e:
        h3 = 'Parameter not found'

    try:
        h4 = [h4.get_text() for h4 in h4_raw]
    except Exception as e:
        h4 = 'Parameter not found'

    try:
        p = [p.get_text() for p in p_raw]
    except Exception as e:
        p = 'Parameter not found'
   
    return f'H1: {h1}\n H2: {h2}\n H3: {h3}\n P: {p}\n'
  
  
 def text_scraper(url):
    """
    To get all the text in a page, regardless of the HTML tags, in page order.
    """

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'}

    content = req.get(url, "html.parser", headers=header ).content
    soup = BS4(content, "lxml")  
    
    return soup.get_text(' ', strip=True)
  
  
  for element in url_list:
    print(f'URL: {element}\n {text_scraper(element)}\n')
    
