

import cloudscraper
import requests
import os
import ssl
from bs4 import BeautifulSoup
import re


ssl._create_default_https_context = ssl._create_unverified_context

# 使用者輸入Jable網址
url = input('輸入jable網址:')

# 建立番號資料夾
urlSplit = url.split('/')
dirName = urlSplit[-2]
if not os.path.exists(dirName):
    os.makedirs(dirName)
folderPath = os.path.join(os.getcwd(), dirName)

htmlfile = cloudscraper.create_scraper(browser='chrome', delay=10).get(url)

soup = BeautifulSoup(htmlfile.text, "html.parser")
#cover_name = f"{os.path.basename(folderPath)}.jpg"

vf = soup.find("video")

img_url = re.findall('https?://.+jpg', str(vf))

str_img_url = str(img_url)[2:-2]

print(str_img_url)

'''
'''
img_data = requests.get(str_img_url).content
with open(folderPath, "wb") as cover_fh:
    cover_fh.write(img_data)

