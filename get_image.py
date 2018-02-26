# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib
import os
import http.cookiejar
import json
import urllib.request as req

def get_soup(url,header):

    request = req.Request(url, headers=header)
    # メモリにダウンロード
    with req.urlopen(request) as r:
        mem = r.read()
        text = mem.decode("utf-8")
        # print(text)

    return BeautifulSoup(text, 'html.parser')

query = "Yokoyama yui"# 横山由依の画像を検索
label="0"
print(query)
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print(url)
#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print("there are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
for i , (img , Type) in enumerate( ActualImages):
    try:
        req = urllib.request.Request(img, headers={'User-Agent' : header})
        raw_img = urllib.request.urlopen(req).read()
        print("**:",req)
        print("**:",raw_img)

        cntr = len([i for i in os.listdir(DIR) if label in i]) + 1
        print(cntr)
        if len(Type)==0:
            f = open(os.path.join(DIR , label + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , label + "_"+ str(cntr)+"."+Type), 'wb')


        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : "+img)
        print(e)
