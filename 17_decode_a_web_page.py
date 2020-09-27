# Exercise:
# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

# Writing github home page into a html file
# import requests

# url = 'http://github.com'
# r = requests.get(url)
# r_html = r.text

# file = open("github.html", "w", encoding="utf-8")
# file.write(r_html)

from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
all_span = soup.find_all("h2") 
#title = soup.find('span', 'articletitle').string
#print(BeautifulSoup(r_html, "html.parser"))
for span in all_span:
    title = span.text.strip()
    print(title)