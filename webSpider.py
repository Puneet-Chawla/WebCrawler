import requests
# fetching data from internet

from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while (page <= max_pages):
        url="https://thenewboston.com/videos.php?cat=11"
        source_code=requests.get(url)
        plain_text=source_code.text
        soup= BeautifulSoup(plain_text,"html5lib")

        for link in soup.find_all('a',{'class':'item-name'}):
            href=link.get(href)
            title=link.string
            print(href)
            print(title)
    page += 1






trade_spider(1)

