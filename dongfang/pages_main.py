# coding:utf8
# 获取股吧页数
import math
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
class PageMain(object):
    def main_pageNum(self,url):
        urls = urlopen(url)
        soup = BeautifulSoup(urls.read().decode('utf8'))
        tags = soup.find(class_='pager').get_text()
        p = re.compile('\d+')
        tag = p.search(tags)
        tag1 = tag.group()
        tag2 = math.ceil(float(tag1)/80)
        return tag2
    def base(self,url,num):
        urls = urlopen(url)
        soup = BeautifulSoup(urls.read().decode('utf8'))
        tag1 = soup.find_all(class_='articleh')
        for tag in tag1:
            con = tag.contents[num].get_text()
            return con
        