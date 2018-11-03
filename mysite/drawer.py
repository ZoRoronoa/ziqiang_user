from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import requests
import re

resp = urlopen("http://cs.whu.edu.cn/news_list.aspx?category_id=54").read().decode("utf-8")
soup = BeautifulSoup(resp, "html.parser")
search_urls = soup.find_all('a', href=re.compile(r"/news_show\.aspx\?"))
#这只能获取第一页前12个通知的内容

info = []
for search_url in search_urls:

    add_url = search_url['href']
    root_url = "http://cs.whu.edu.cn/news_list.aspx?category_id=54"
    all_url = parse.urljoin(root_url, add_url)

    resp2 = requests.get(all_url)
    soup2 = BeautifulSoup(resp2.content, "html.parser")

    news_list = soup2.find_all('div', class_='right_list_sp')
    #创建一个列表储存所有结果

    for news in news_list:
        mydict = {}
        result_list = []
        mydict['title'] = news.find('div', class_='sp1').get_text()
        mydict['content'] = news.find('div', class_='').get_text().replace('\xa0', '').replace('\n', '')
        result_list.append(mydict)

        for item in result_list:
            info.append(item)


        fout = open('oldblog.txt', 'w')


        for i in info:
            g = i.get('title')
            k = i.get('content')
            fout.write(g)
            fout.write("\r\n")
            fout.write(k)
            fout.write("\r\n")













