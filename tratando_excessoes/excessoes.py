from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

try:
    html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
except HTTPError as e:
    print(e)
except URLError:
    print('The server could not be found ...')
else:
    bs = BeautifulSoup(html, "html.parser")
    print(bs.html.body.h1)
