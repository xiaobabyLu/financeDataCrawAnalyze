import dataScripy as ds
import datetime

'''
获取k曲线的增长/下降百分比
'''
def get_stock_K_rate():
    print('a')

if __name__ == '__main__':
    #调用登录信息
    ds.login_in()

    today = str(datetime.date.today())
    thirty_ago =str(datetime.date.today() - datetime.timedelta(30))

    codes = ds.main(1,400)
    for code_num in codes:
        if(code_num[0] == 6 or code_num[0] == 9):
            code = 'sh.' + code_num
            code_url = 'sh'+code_num
        else:
            code = 'sz.' + code_num
            code_url = 'sz'+code_num

        df = ds.get_k_line(code,thirty_ago,today)

        lt = df.values.tolist()

        lenth = len(lt) - 1
        if (lenth > 10):
            thirty = (float(lt[lenth][5]) - float(lt[0][5])) / float(lt[0][5])
            ten = (float(lt[lenth][5]) - float(lt[lenth // 2][5])) / float(lt[10][5])
            if (thirty > 0.25 and ten > 0.1):
                url = f'http://quote.eastmoney.com/{code_url}.html'
                print(url)

#调用登出方法
    ds.login_out()