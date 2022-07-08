import time

import dataScripy as ds

import datetime
from tqdm import tqdm
from multiprocessing.pool import ThreadPool

#创建线程池

pool = ThreadPool(5)  # 创建一个线程池

err_lst =[]
codes = ds.main(1,400)
codes.reverse()

i = 0
for code in tqdm(codes):
    indict = ''
    try:
        print('-------------' + code + '----------')
        lst = ds.get_search_theche_direct_url(code)
    except Exception as e:
        err_lst.append(code)
        with open('data.txt', 'a+') as f:  # 设置文件对象
            f.write(code + ',')  # 将字符串写入文件中
        print('运行错误：'+code)
        continue

    c = len(lst)
    if c == 0:
        with open('data.txt', 'a+') as f:  # 设置文件对象
            f.write(code + ',')  # 将字符串写入文件中
        print('运行错误：'+code)
        print(" ")
    else:

        indict = lst[18].split(':')[3]

    if(indict == '强力买入'):
        print("请关注：")
        print(code)

print(err_lst)