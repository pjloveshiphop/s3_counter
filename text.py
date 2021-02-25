import os
import json
import sys
import pandas as pd
from os import listdir
from os.path import isfile, join
import time
import jsonlines
import textwrap
import collections

myfiles = [f for f in listdir(r'D:\myData\한국어-영어1') if isfile(join(r'D:\myData\한국어-영어1',f))]
#print(myfiles)

result=list()
root = r'D:\myData\한국어-영어1'
count=0


for i in range(len(myfiles)):
    with open(os.path.join(root, myfiles[i]), encoding='utf8') as f:
    
        data=json.load(f)
        cnt=collections.Counter()
        for txt in data['data']:
            count+=1
            cnt[txt['sn']]+=1
        result.append('{}: {}'.format(myfiles[i][0:myfiles[i].find('(')], len(cnt)))
        #print(len(cnt))
        #cnt.append('{}: {}'.format(myfiles[0][0:myfiles[0].find('(')], count))
        cnt.clear()
        #print(len(cnt))
        
        #result=list()
        count=0




for el in result:
    print(el)
            

#df= pd.DataFrame()
#df.insert(0, 'text', text)

#df.to_csv(os.path.join(root, 'myresult.csv'), index=False, encoding='utf-8-sig')
