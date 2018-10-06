
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import re
resp = urlopen("http://cs.whu.edu.cn/news_list.aspx?category_id=54").read().decode("utf-8")
soup = BeautifulSoup(resp, "html.parser")
search_urls = soup.find_all('a', href=re.compile(r"/news_show\.aspx\?"))
#这只能获取第一页前12个通知的内容

for search_url in search_urls:

    add_url = search_url['href']
    root_url = "http://cs.whu.edu.cn/news_list.aspx?category_id=54"
    all_url = parse.urljoin(root_url, add_url)


    resp2 = urlopen(all_url).read().decode("utf-8")
    soup2 = BeautifulSoup(resp2, "html.parser")




    news_title = soup2.select('div[class="sp1"]')

    news_text = soup2.select('div[class="right_list_sp"]')
    #寻找内容时找不到单纯将时间和内容包含的标签，只好扩大范围将标题又获取了一次
    #内容里一些非文字（如\n，\xa0等）也无法出去


    lists1 = []
    lists2 = []

    for x in news_title:
        lists1.append(x.get_text())

    for y in news_text:
        lists2.append(y.get_text())

    print("{title:", lists1, "text:", lists2, "}")








