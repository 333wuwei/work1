import requests
import csv
from bs4 import BeautifulSoup

# 发送网络请求获取页面内容
url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
response = requests.get(url)

# 解析HTML页面
soup = BeautifulSoup(response.content, "html.parser")

# 找到表格数据
table = soup.find("table", class_="table table-hover")

# 创建CSV文件并写入表头
csv_file = open("bond_data.csv", "w", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"])

# 判断是否找到了表格元素
if table is not None:
    # 遍历表格行
    rows = table.find_all("tr")
    for row in rows[1:]:  # 跳过表头行
        # 解析每一行的数据
        data = [cell.get_text(strip=True) for cell in row.find_all("td")]

        # 判断是否符合条件（Bond Type = Treasury Bond, Issue Year = 2023）
        if len(data) >= 6 and data[3] == "Treasury Bond" and data[4] == "2023":
            csv_writer.writerow(data[:6])

# 关闭CSV文件
csv_file.close()