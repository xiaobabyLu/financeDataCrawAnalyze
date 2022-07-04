import pandas as pd


'''
参考文章：https://zhuanlan.zhihu.com/p/351603761
'''


url = 'https://q.stock.sohu.com/cn/600900/index.shtml'
# index:0 代表利润 2 代表业务构成
tb = pd.read_html(url)[0]  # 经观察发现所需表格是网页中第4个表格，故为[3]
# tb.to_csv(r'C:\Users\xxx\Desktop\1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
# print('第' + str(i) + '页抓取完成')
print(tb)