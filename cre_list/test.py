# encoding:gbk
import os
import re
def cre_list(hangyeid):
    info = "D:\\Stock\\"+hangyeid
    listfile=os.listdir(info)
    f = open("D:\\Stock\\"+hangyeid+"\\list.txt",'w')
    q = re.compile(r'(.txt)$')
    p = re.compile(r'^[0-9]')
    for line in listfile:
        if(p.search(line)):
            line = q.sub("",line)
            f.write(line+'\n')
            print(line)
    f.close()
    print('done')
# 创建行业股票代码列表