import baostock as bs
import pandas as pd
import datetime
import finance

'''
参考文章： http://baostock.com/baostock/index.php/%E9%A6%96%E9%A1%B5
'''

def get_k_line(code,start_date,end_date):

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。“分钟线”不包含指数。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    # 周月线指标：date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg

    today = str(datetime.date.today())
    thirty_ago =str(datetime.date.today() - datetime.timedelta(30))

    '''
    获取code
    '''
    import stockCode
    codes = stockCode.main(1,400)
    for code in codes:
        firstNum = int(code[0])
        if(firstNum == 6 or firstNum ==9 ):
            code = 'sh.' + code
        else:
            code = 'sz.'+code

        rs = bs.query_history_k_data_plus(code,
            "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
            start_date=thirty_ago, end_date=today,
            frequency="d", adjustflag="3")
        # print('query_history_k_data_plus respond error_code:'+rs.error_code)
        # print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

        #### 打印结果集 ####
        data_list = []
        while (rs.error_code == '0') & rs.next():
            # 获取一条记录，将记录合并在一起
            data_list.append(rs.get_row_data())
        pd.set_option('display.max_columns', 20)

        result = pd.DataFrame(data_list, columns=rs.fields)

        #### 结果集输出到csv文件 ####
        # result.to_csv("D:\\history_A_stock_k_data.csv", index=False)

        shift = result['low'].shift(-5)
        # print(pd.concat([result, shift], 1))

        lt = pd.concat([result, shift], 1).values.tolist()

        lenth = len(lt) -1
        if(lenth>10):
            thirty = (float(lt[lenth][5]) - float(lt[0][5]))/float(lt[0][5])
            ten = (float(lt[lenth][5]) - float(lt[lenth//2][5]))/float(lt[10][5])
            if(thirty < -0.6):
                print(code)
        #### 登出系统 ####
    bs.logout()

