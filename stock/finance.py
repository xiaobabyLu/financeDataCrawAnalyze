
from selenium import webdriver

'''
参考文章 ：https://cloud.tencent.com/developer/article/1358519
'''


# 当测试好能够顺利爬取后，为加快爬取速度可设置无头模式，即不弹出浏览器
# 添加无头headlesss 1使用chrome headless,2使用PhantomJS
# 使用 PhantomJS 会警告高不建议使用phantomjs，建议chrome headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.PhantomJS()
# browser.maximize_window()  # 最大化窗口,可以选择设置

# 加载启动项，这里设置headless，表示不启动浏览器，只开一个监听接口获取返回值
browser = webdriver.Chrome("E:\\software\chromedriver.exe",80,chrome_options)


browser.get('http://data.eastmoney.com/bbsj/201806/lrb.html')
element = browser.find_element_by_css_selector('tbody')  # 定位表格，element是WebElement类型
# 提取表格内容td
td_content = element.find_elements_by_tag_name("td") # 进一步定位到表格内容所在的td节点
lst = []  # 存储为list
for td in td_content:
    lst.append(td.text)
print(lst) # 输出表格内容

col = len(element.find_elements_by_css_selector('tr:nth-child(1) td'))
print(col)

browser.quit()