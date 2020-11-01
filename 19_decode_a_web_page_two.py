# Exercise:
# https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

from bs4 import BeautifulSoup
import requests

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
all_span = soup.find_all("p") 
#title = soup.find('span', 'articletitle').string
#print(BeautifulSoup(r_html, "html.parser"))
for span in all_span:
    title = span.text.strip()
    print(title)