import dataScripy as ds
import datetime
from tqdm import tqdm
from multiprocessing.pool import ThreadPool

#创建线程池

pool = ThreadPool(5)  # 创建一个线程池

codes =[]
a = ds.get_code_pe(1,400)
for code in a:
    if(code[2] != '"-"'):
        if(float(code[2])>0 and float(code[2])<70):
            print(code[0])
            cod = code[0].strip('"')
            print(cod)
            try:
                df = ds.get_profit_by_code(cod,0)
            except:
                continue
            if df.iat[3, 2] == '-':
                s = 0
            else:
                s = float(df.iat[3, 2])
            if(df.iat[2,2]) == '-':
                p= 0
            else:
                p=float(df.iat[2,2])
            print(s,p)
            if(s>10 and p>10):
                print(code[1])
                codes.append(code[0])
print(len(codes))
codes.reverse()

i = 0
for code in tqdm(codes):
    indict = ''
    try:
        print('-------------' + code + '----------')
        lst = ds.get_search_theche_direct_url(code)
    except Exception as e:
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

