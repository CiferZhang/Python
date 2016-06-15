# encoding:utf8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import math
import urllib.parse
import urllib.request
import pymysql
from pages_main import PageMain
f = open('stock_num.txt')
stock_num = []
for line in f.readlines():
    line = line.replace('\n','')
    stock_num.append(line)
for each in stock_num:    
    stock = each;
    num = PageMain()
    url = 'http://guba.eastmoney.com/list,'+stock+'.html'
    num1 = num.main_pageNum(url)
    num2 = 1
    conn = pymysql.connect(host='localhost',user='root',passwd='',db='test_all',charset='utf8')
    cur = conn.cursor()
    while num2<=num1:
        url = "http://guba.eastmoney.com/list,600460_"+str(num2)+".html"
        print(url)
        urls = urlopen(url)
        soup = BeautifulSoup(urls.read().decode('utf8'))
        tag1 = soup.find_all(class_='articleh')
        for tag in tag1:
            tag2 = tag.find('a',href=re.compile(r'^\/?news'))
            tag3 = tag2['href']
            q = re.compile(r'\.html')
            p = re.compile(r'^\/')
            tag4 = q.sub("",tag3)
            tag5 = p.sub("",tag4)
            reading = tag.contents[1].get_text()
            comment = tag.contents[2].get_text()
            title = tag.contents[3].get_text()
            writer = tag.contents[4].get_text()
            new = tag.contents[6].get_text()
                
            com_page = math.ceil(float(comment)/30)
            page_url = "http://guba.eastmoney.com/"
            count = 1
            while count<=com_page:
                new_url = tag5+"_"+str(count)+".html"
                full_url = urllib.parse.urljoin(page_url,new_url)
                req = urllib.request.Request(full_url)
                req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0')
                page = urllib.request.urlopen(req)
                soup2 = BeautifulSoup(page.read().decode('utf8'))
                try:
                    tags = soup2.find_all(class_='zwlitxt')
                    if count == 1:
                        tagg = soup2.find(class_='zwfbtime').get_text()
                        q = re.compile(r'\d{4}-\d{2}-\d{2}'+' +'+'\d{2}:\d{2}:\d{2}')
                        publish = q.search(tagg)
                    for tag in tags:
                        name = tag.find(class_='zwlianame').get_text()
                        time = tag.find(class_='zwlitime').get_text()
                        p=re.compile(r'\d{4}-\d{2}-\d{2}'+' +'+'\d{2}:\d{2}:\d{2}')
                        time1 = p.search(time)
                        try:
                            content = tag.find(class_='zwlitext stockcodec').get_text()
                        except:
                            content = tag.find(class_='zwlitext yasuo stockcodec').get_text()
                        print(count)
                        print('reading'+reading,'comment'+comment,'title'+title,'writer'+writer,'publish'+publish.group(),'new'+new,name,time1.group(),content)
                        try:
                            sql_insert = "insert into test1(stock,reading,comment,title,writer,publish,new,comment_name,comment_time,comment_content) values(%s,%s,%s,'%s','%s','%s','%s','%s','%s','%s')"%(stock,reading,comment,title,writer,publish.group(),new,name,time1.group(),content)
                            cur.execute(sql_insert)
                        except Exception as e:
                            print(e)    
                except:
                    time = '0'
                    name = '0'
                    content = '0'
                    publish = '0'
                    print('reading'+reading,'comment'+comment,'title'+title,'writer'+writer,'publish'+publish,'new'+new,name,time,content)
                    try:
                        sql_insert = "insert into test1(stock,reading,comment,title,writer,publish,new,comment_name,comment_time,comment_content) values(%s,%s,%s,'%s','%s','%s','%s','%s','%s','%s')"%(stock,reading,comment,title,writer,publish,new,name,time,content)
                        cur.execute(sql_insert)
                    except Exception as e:
                        print(e)
                      
                    conn.commit()
                count +=1
        num2 +=1
    cur.close()
    conn.close()
    print('done')
