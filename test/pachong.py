
import re
import requests
import parsel
import os

for page in range(1, 6):
    print(f'=======================正在爬取第{page}页数据=====================')
    base_url = f'https://www.hexuexiao.cn/meinv/guzhuang/list-{page}.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

    try:
        response = requests.get(base_url, headers=headers)
    except:
        continue
    data = response.text

    html_data = parsel.Selector(data)
    data_list = html_data.xpath(
        '//div[@class="waterfall_1box"]/dl/dd/a/img/@title|//div[@class="waterfall_1box"]/dl/dd/a/@href').getall()

    data_list = [data_list[i:i + 2] for i in range(0, len(data_list), 2)]

    for alist in data_list:
        html_url = alist[0]
        file_name = alist[1]

        if not os.path.exists('img\\' + file_name):
            os.mkdir('img\\' + file_name)
        print('正在下载：', file_name)

        try:
            response_2 = requests.get(html_url, headers=headers).text
        except:
            continue

        page_num = re.findall('\(1/(.*?)\)', response_2, re.S)[0]

        for url in range(0, int(page_num) + 1):
            url_list = html_url.split('.')
            all_url = url_list[0] + '.' + url_list[1] + '.' + url_list[2] + '-' + str(url) + '.' + url_list[3]

            try:
                response_3 = requests.get(all_url, headers=headers).text
            except:
                continue
            html_3 = parsel.Selector(response_3)

            img_url = html_3.xpath('//div[@class="col-xs-4 text-left"]/a/@href').get()

            try:
                img_data = requests.get(img_url, headers=headers).content
            except:
                continue

            img_name = str(url) + '.jpg'


            with open('img\\{}\\'.format(file_name) + img_name, 'wb') as f:
                print('下载完成：', img_name)
                f.write(img_data)