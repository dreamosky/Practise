# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
# soup = BeautifulSoup(html, features='lxml')
# month = soup.find_all('li', {"class": "month"})
# for m in month:
#     print(m.get_text())

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.baidu.com')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.findAll('span', {'class':'green'})
for name in nameList:
    print(name.get_text())