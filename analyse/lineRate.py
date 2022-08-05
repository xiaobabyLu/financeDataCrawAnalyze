import numpy as np
import matplotlib.pyplot as plt
import dataScripy as ds
import datetime

''''
根据派息记录模拟直线，根据斜率获取股利增长率，对于大多数企业不太适用

求取stock_value的趋势拟合直线的斜率
'''


# 损失函数是系数的函数，另外还要传入数据的x,y
def compute_cost(w,b,x,y):
    total_cost=0
    M =len(y)
    for i in range(M):
        xx=x[i]
        yy=y[i]
        total_cost += (yy-w*xx-b)**2
    return total_cost/M
    #一除都是浮点 两个除号是地板除，整型。 如 3 // 4


# 先定义一个求均值的函数 问题 求均值是不是可以直接用np.mean（data）来实现？
# def average(data):
#     sum=0
#     num=len(data)
#     for i in range(num):
#         sum += data[i]
#     return sum/num
# print(average(x))
# print(np.mean(x))
# 打印出来结果一样，可以通用。


 # 定义核心拟合函数
def fit(x,y):
    M = len(y)
    x_bar = np.mean(x)
    sum_yx = 0
    sum_x2 = 0
    sum_delta = 0
    for i in range(M):
        xx = x[i]
        yy = y[i]
        sum_yx += yy * (xx - x_bar)
        sum_x2 += xx ** 2
    # 根据公式计算w
    w = sum_yx / (sum_x2 - M * (x_bar ** 2))

    for i in range(M):
        xx = x[i]
        yy = y[i]
        sum_delta += (yy - w * xx)
    b = sum_delta / M
    return w, b

if __name__ == '__main__':

    ds.login_in()

    today = str(datetime.date.today())
    thirty_ago =str(datetime.date.today() - datetime.timedelta(60))
    one_half_year =str(datetime.date.today() - datetime.timedelta(510))
    print(one_half_year)

    df = ds.get_k_line('sh.601318', '2022-05-30', '2022-06-08')
    print(df)

    ds.login_out()

    y_str = df['close'].values.tolist()

    y_float = list(map(float,y_str))

    print(len(y_str))

    x = list(range(0,len(y_str)))


    w,b =fit(x,y_float)

    print("w is :", w)
