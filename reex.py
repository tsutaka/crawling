from bs4 import BeautifulSoup
import urllib.request as req
import re

url = "https://github.com/"

# メモリにダウンロード
with req.urlopen(url) as r:
    mem = r.read()
    text = mem.decode("utf-8")
    # print(text)

soup = BeautifulSoup(text, "html.parser")


li = soup.find_all(href=re.compile(r"^https://.*"))
for e in li:
    print(e.attrs['href'])
