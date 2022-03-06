from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bs = BeautifulSoup(html.read(), "html.parser")
print(bs.h1)
