import requests
from bs4 import BeautifulSoup as bs
import os

# website with images  你要的网址
url = 'https://www.google.com/search?q=%E9%AB%98%E5%9C%86%E5%9C%86&tbm=isch&tbas=0&source=lnt&sa=X&ved=0ahUKEwjDxcSEtsTeAhWBa7wKHULrCycQpwUIHw&biw=1280&bih=664&dpr=1'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# 找到搜有的图片
image_tags = soup.findAll('img')

# 创立文件夹用来储存图片
if not os.path.exists('高圆圆'):
    os.makedirs('高圆圆')

# move to new directory 移到新的文件夹
os.chdir('高圆圆')

# image file name variable 图片文件的名字
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('高圆圆-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
       pass