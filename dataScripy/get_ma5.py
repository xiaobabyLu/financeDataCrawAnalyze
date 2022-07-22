import tushare as ts

# 通过tushare获取股票信息
df = ts.get_k_data('300580', start='2017-01-12', end='2017-05-26')

print(df)
# 提取收盘价
closed = df['close'].values

dd=ts.get_hist_data('002837') #爬取股票近三年的全部日k信息

print(dd)