file = open('data.csv', 'w', encoding='utf-8', newline="")
        csv_write = csv.writer(file)
        csv_write.writerow(['地区','确诊','治愈','死亡'])

        csv_write.writerow(['中国台湾',taiwan_confirm,taiwan_cure,taiwan_death])
        file.close()
