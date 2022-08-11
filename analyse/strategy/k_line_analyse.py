import time
import dataScripy as ds
from datetime import date
import datetime



'''
分析k线 ，寻找机会
'''





'''
strategy 1.分析k线数据 ，周线低点到现在比值,获取满足条件的codes
'''
def get_codes_we_min_now_rate(code,start_date,end_date,k):
    df_week = ds.get_k_line(code, start_date, end_date, 'w')
    w_min   =  float(df_week['close'].min())

    yestaday_close_price = 0.0

    #获取dataframe指定列最后一行的值
    if len(df_week['close'].tail(3).tolist()) <2 :
        print('暂时没有查询出来或者数据较少：', code)
    else:
        yestaday_close_price = float(df_week['close'].tail(2).tolist()[0])
        last_week_close_price = float(df_week['close'].tail(2).tolist()[1])


    growth_rate = (yestaday_close_price - w_min) / w_min

    if growth_rate > 0.08 and growth_rate < k and yestaday_close_price > last_week_close_price:
        print(stock_code, ':', w_min, yestaday_close_price, growth_rate)
        return code



if __name__ == '__main__':
    #指定时间范围
    today = str(date.today())
    one_half_year =str(datetime.date.today() - datetime.timedelta(210))

    stocks_code = ds.get_stock_codes()

    ds.login_in()
    codes = []
    for stock_code in stocks_code:
        time.sleep(1)
        code = get_codes_we_min_now_rate(stock_code,one_half_year,today,0.2)
        codes.append(code)


    print('符合条件个数：',len(codes),codes)
