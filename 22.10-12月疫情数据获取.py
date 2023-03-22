import requests
import json
import csv

def china_total_data():
    chinatotal_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other'
    response = requests.get(chinatotal_url).json()  # 发出请求并json化处理
    # 将获取到的json格式的字符串类型数据转换为python支持的字典类型数据
    data = json.loads(response['data'])
    chinaDayList = data["chinaDayList"]
    with open("病例.csv", "w+", newline="") as csv_file:
        writer = csv.writer(csv_file)
        header = ["date", "confirm", "suspect", "dead", "heal"]  # 定义csv表头
        writer.writerow(header)
        # 通过for循环获取json中的相关数据
        for i in range(len(chinaDayList)):
            data_row1 = [chinaDayList[i]["date"], chinaDayList[i]["confirm"], chinaDayList[i]["suspect"],
                         chinaDayList[i]["dead"], chinaDayList[i]["heal"]]
            # 写入数据
            writer.writerow(data_row1)

if __name__ == '__main__':
    china_total_data()