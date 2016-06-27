# encoding:utf8
import re
import pymysql
from bs4 import BeautifulSoup
from urllib.request import urlopen
def sqlinsert(url,stock,type):
    url1 = urlopen(url)
    soup = BeautifulSoup(url1.read().decode('gbk'))
    try:
        tag1 = soup.find(class_='datelist').get_text()
        tag2 = soup.find(class_='datelist')
        q = re.compile(r'\d{4}-\d{2}-\d{2}')
        db =[]
        db = q.findall(tag1)
        l = len(db)
        n=0
        while(n<l):
            tag = tag2.select('a')[n].get_text()
            print(stock)
            print(db[n])
            print(tag)
            sql_insert = "insert into `"+stock+"`(id,date,title)values('%s','%s','%s')"%(type,db[n],tag)
            cur.execute(sql_insert)
            n = n+1
    except Exception as e:
        print(e)
        return 

conn = pymysql.connect(host='localhost',user='root',passwd='',db='test',charset='utf8')
cur = conn.cursor()
f = open('stock_num.txt')
stock_num = []
for line in f.readlines():
    line = line.replace('\n','')
    stock_num.append(line)
for each in stock_num:
    stock = str(each)
    sql_cre = "create table `"+stock+"`(id varchar(10),date varchar(30),title varchar(50) character set gbk);"
    cur.execute(sql_cre)
    url1 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=gzbc"
    url2 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=gqfzgg"
    url3 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=hfbg"
    url4 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=ndbg"
    url5 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=pgsms"
    url6 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=qzssgg"
    url7 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=qzsms"
    url8 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=sjdbg"
    url9 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=ssggs"
    url10 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=yjdbg"
    url11 = "http://vip.stock.finance.sina.com.cn/corp/go.php/vCB_AllBulletin/stockid/"+stock+".phtml?ftype=zqbg"
    sqlinsert(url1,stock,'gzbc')
    sqlinsert(url2,stock,'gqfzgg')
    sqlinsert(url3,stock,'hfbg')
    sqlinsert(url4,stock,'ndbg')
    sqlinsert(url5,stock,'pgsms')
    sqlinsert(url6,stock,'qzssgg')
    sqlinsert(url7,stock,'qzsms')
    sqlinsert(url8,stock,'sjbdg')
    sqlinsert(url9,stock,'ssggs')
    sqlinsert(url10,stock,'yjdbg')
    sqlinsert(url11,stock,'zqbg')    
conn.commit()    
cur.close()
conn.close()
print('done')






