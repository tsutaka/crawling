import sys

from bs4 import BeautifulSoup
import urllib.request as req


url = "https://www.yahoo.co.jp/"
url = "https://dekiru.net/article/13003/"

# メモリにダウンロード
with req.urlopen(url) as r:
    mem = r.read()
    text = mem.decode("utf-8")
    print(text)

soup = BeautifulSoup(text, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p

print("h1 : " + str(h1))
print("p1 : " + str(p1))
print("h1 : " + str(h1.string))
print("p1 : " + str(p1.string))
