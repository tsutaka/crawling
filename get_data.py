from bs4 import BeautifulSoup
import urllib.request as req

# HTMLを取得
url = "https://baseball.yahoo.co.jp/npb/standings/"
res = req.urlopen(url)

# HTMLを解析
soup = BeautifulSoup(res, "html.parser")



# #sta_c > div:nth-child(1) > table:nth-child(2) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(2) > a:nth-child(1)
li_list = soup.select("div > table > tbody > tr > td")
for li in li_list:
    a = li.a
    if a != None:
        name = a.string
        href = a.attrs["href"]
        print(name, ">", href)
