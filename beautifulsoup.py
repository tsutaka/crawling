import sys

from bs4 import BeautifulSoup
import urllib.request as req


url = "https://github.com/"

# メモリにダウンロード
with req.urlopen(url) as r:
    mem = r.read()
    text = mem.decode("utf-8")
    # print(text)

soup = BeautifulSoup(text, 'html.parser')

# tag search
h1 = soup.html.body.h1
p = soup.html.body.p

if h1 != None:
    print("h1 : " + str(h1.string))
else:
    print("h1 : None")

if p != None:
    print("p : " + str(p.string))
else:
    print("p : None")

# id search
id1 = soup.find(type="submit")
#
if id1 != None:
    print("title : " + str(id1.string))
else:
    print("id1 : None")

# links search
links = soup.find_all("a")

for a in links:
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)
