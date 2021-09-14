# -*- coding: utf-8 -*-
# @Time    : 2021/4/9 8:47
# @Author  : Wxl
# @Email   : 154831156@qq.com
# @File    : text2.py
# @Software: PyCharm
import requests
import json
import os
import pandas as pd
import numpy  as np
import re


data_directory  = 'D:\\BaiduNetdiskDownload\\data\\matchdata2\\chinavisdaydata\\201301\\CN-Reanalysis-daily-2013010100.csv'   # 存放每个月的文件夹的路径
save_directory  = 'D:\\BaiduNetdiskDownload\\data\\model.csv'   # 存放每个月的文件夹的路径

df = pd.read_csv(data_directory)
df= df.drop(' ', 1)     # 删除空白列
df['city'] = np.nan     # 添加新的城市列并赋初值为nan
df['province'] = np.nan     # 添加新的所在区列并赋初值为nan
df['district'] = np.nan     # 添加新的所在区列并赋初值为nan
# 循环遍历单个的dataform
print(df)
for index, row in df.iterrows():
    lat = row['lat']    # 纬度
    lon = row['lon']    # 经度
    request_url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=8QKYHibZWcrpyViOVCe4HPT88aSv9wWH&output=json' \
                  '&coordtype=wgs84ll&location={0},{1}'.format(lat,lon)

    r = requests.get(url=request_url)

    result = r.json()
    try:
        city = result['result']['addressComponent']['city']
        province = result['result']['addressComponent']['province']
        district = result['result']['addressComponent']['district']
        # print(city,'----------',province,'----------',district)
        if not city.isspace():
            df.loc[index,'city'] = city
        if not province.isspace():
            df.loc[index,'province'] = province
        if not district.isspace():
            df.loc[index,'district'] = district
        if index % 100 == 0:
            print('---------'+str(index)+'------------')
    except Exception as e:
        print(e)

print(df)
df.to_csv(save_directory,index=False)    # 数据导出
print(save_directory + '：输出成功')