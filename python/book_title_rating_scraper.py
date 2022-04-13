# pick all the books from an ecommerce site where rating = two star, for all the pages of the website

two_star_books_list = []

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

for i in range (50):
  req = requests.get(base_url.format(i))
  soup = bs4.BeautifulSoup(req.text, "lxml")
  all_books = soup.select(".product_pod")

  for book in all_books:
    if len(book.select(".star-rating.Two")) != 0:
      two_star_books_list.append(book.select("a")[1]["title"])

print(two_star_books_list[0])
