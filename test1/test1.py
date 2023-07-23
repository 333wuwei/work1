import csv
import pprint
import time
import requests

# 请求伪装，防止服务器检测
cookies = {
    'apache': '4a63b086221745dd13be58c2f7de0338',
    '_ulta_id.ECM-Prod.ccc4': '9f910d42c2352db2',
    '_ulta_ses.ECM-Prod.ccc4': '0062ef549aae80bc',
    'AlteonP10': 'AT7WLSw/F6yjfZJbbdd5Ww$$',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://iftp.chinamoney.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://iftp.chinamoney.com.cn/english/bdInfo/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

"""打开csv写入，通过页数和JSON数据循环取值"""
with open("data.csv",mode="w",encoding="utf-8",newline="") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['ISIN',' Bond Code',' Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
    for i in range(4):
        data = {
            'pageNo': str(i+1),
            'pageSize': '15',
            'isin': '',
            'bondCode': '',
            'issueEnty': '',
            'bondType': '100001',
            'couponType': '',
            'issueYear': '2023',
            'rtngShrt': '',
            'bondSpclPrjctVrty': '',
        }

        response = requests.post(
            'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        # pprint.pprint(response.json())
        data_jsons = response.json()["data"]["resultList"]
        for j in data_jsons:
            ISIN = j['isin']
            Bond_Code = j['bondCode']
            Issuer = j['entyFullName']
            Bond_Type = j['bondType']
            issue_Date = j['issueEndDate']
            Latest_rating = j['debtRtng']

            print(ISIN,Bond_Type,Issuer,Bond_Code,issue_Date, Latest_rating)
            csv_writer.writerow([ISIN, Bond_Code, Issuer, Bond_Type, issue_Date, Latest_rating])
        print(f"第{i+1}面数据提取完毕===============还剩下{3-i}面没有提取")
        print(f"第{i+1}面数据提取完毕===============还剩下{3-i}面没有提取")
        print(f"第{i+1}面数据提取完毕===============还剩下{3-i}面没有提取")
        time.sleep(2)