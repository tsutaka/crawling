from bs4 import BeautifulSoup


#read file return rows_list
def read_file(path='./', fileName=''):
    with open(path + fileName,'r') as f:
        print(f)
        return f

if __name__ == '__main__':
    print(">start")

    with open('./sample.ttml','r', encoding='utf-8') as text:
        # soup = BeautifulSoup(text, 'html')
        soup = BeautifulSoup(text, 'xml')

    print(soup)

    # p tag search
    captions = soup.find_all("p")

    caption_list = []
    for caption in captions:
        begin_time = caption.attrs['begin']
        end_time = caption.attrs['end']
        text = caption. text_content()
        print("", begin_time, " - ", end_time, ":", text)
        caption_list.append("" + begin_time + " - " + end_time + ":" + text)

    # print(soup.p)
    print(caption_list)

    print(">end")
    exit(0)
