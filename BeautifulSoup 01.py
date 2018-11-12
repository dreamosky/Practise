# import builtwith
# tec = builtwith.parse('http://example.webscraping.com')
# print(tec)

# import whois
# print (whois.whois('appspot.com'))


# from urllib.request import urlopen
# html = urlopen('http://pythonscraping.com/pages/page1.html')
# print(html.read())

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
# print(bs.h1.text)

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'lxml')
# print(bs.h1.text)

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('https://google.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not be found!')
else:
    print('It Worked!')
