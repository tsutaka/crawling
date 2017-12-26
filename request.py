import sys

import urllib.request as req
import urllib.parse as parse


# url = "https://www.yahoo.co.jp/"
# url = "http://api.aoikujira.com/zip/xml/get.php"
url = "http://api.aoikujira.com/hyakunin/get.php"

# コマンドライン
if len(sys.argv) <= 1:
    print("USAGE: request.py (keyword)")
    sys.exit()
keyword = sys.argv[1]

# パラメータのURLへのエンコード
values = {
    'fmt': 'ini',
    'key': keyword
}
params = parse.urlencode(values)
url = url + "?" + params
print(keyword)
print("url=", url)

# メモリにダウンロード
with req.urlopen(url) as r:
    mem = r.read()
    text = mem.decode("utf-8")
    print(text)
