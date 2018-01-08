import pandas as pd
import numpy as np
import re
from datetime import datetime

df = pd.read_excel("豆瓣电影.xlsx")
pattern = re.compile(r'\d+-\d+-\d+')

for i, item in df.iterrows():
    #original data likes：['Class 234', '美国', 'Gordon Forbes III', '"海豹"突击队
    item['演员'] = (item['演员'] if item['演员'].endswith(']') else item['演员']+']')
    #Convert string to list
    item['演员'] = item['演员'].replace("'", '').strip('[]').split(',')
    if type(item['时间']) == datetime:
        item['时间'] = item['时间'].strftime('%Y-%m-%d')
        print(item['时间'], item['演员'])
    else:
        try:
            item['时间'] = pattern.search(item['时间']).group()
            print(item['时间'], item['演员'])
        except:
            break