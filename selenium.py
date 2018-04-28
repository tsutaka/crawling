from selenium import webdriver

url = "http://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

# PhantomJSのドライバを得る
browser = webdriver.PhantomJS()
# PhantomJS起動まで3秒待機
browser.implicitly_wait(3)
# URLを読み込む
browser.get(url)
# 画面をキャプチャしてファイルに保存
browser.save_screenshot("website.png")
# ブラウザを終了
browser.quit()
