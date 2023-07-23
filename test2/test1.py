import requests
from bs4 import BeautifulSoup
import pandas as pd

# 设置获取数据的条件
params = {
    'bondType': 'Treasury Bond',
    'issueYear': '2023'
}

# 发送GET请求获取页面内容
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'
response = requests.get(url, params=params)

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到表格数据
table = soup.find('table')

# 提取表格列名
columns = [th.text.strip() for th in table.find_all('th')]

# 提取表格数据行
data = []
for tr in table.find_all('tr'):
    row = [td.text.strip() for td in tr.find_all('td')]
    if row:
        data.append(row)

# 创建DataFrame对象
df = pd.DataFrame(data, columns=columns)

# 保存为CSV文件
df.to_csv('bond_data.csv', index=False)