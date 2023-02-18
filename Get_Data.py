import time
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By

# 实例化Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://m.111.com.cn/yyw/activities/broadcast/#/home")

time.sleep(2)

'''
连接至阿里云服务器搭建的mysql数据库
'''
connection = pymysql.connect(host='47.113.218.92',user='root',password='cdj54188',database='Data')
'''
将数据存入数据库
'''
# 游标实例化
cursor = connection.cursor()
# 测试数据库是否连接成功
try:
    select = cursor.execute("select * from TOTAL_EPIDEMIC_DATA")
    result = cursor.fetchall()
    print("DBConnectSuccessfully")
except Exception as DBConnectError:
    print("DBConnectError")
'''
获取全国疫情总览数据
'''
class GetEpidemicData:
    def get_domestic_epidemic_data(self):
    #全国确诊
        total_number = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/ul[2]/li[1]/div[2]/div[1]/div[2]').text
    #境外输入
        aboard_number = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/ul[2]/li[1]/div[2]/div[2]/div[2]').text
    #治愈人数
        cure_number = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/ul[2]/li[1]/div[2]/div[3]/div[2]').text
    #死亡人数
        death_number = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/ul[2]/li[1]/div[2]/div[4]/div[2]').text
    #更新数据库数据
        cursor.execute("update TOTAL_EPIDEMIC_DATA set totalNumber = %s",total_number)
        cursor.execute('select totalNumber from TOTAL_EPIDEMIC_DATA')
        total = cursor.fetchall()
        print(total)
    #输出数据
        print("全国确诊"+total_number,"境外输入"+aboard_number,"治愈人数"+cure_number,"死亡人数"+death_number)

    def get_provincial_epidemic_data(self):
    #中国台湾数据：
        taiwan_confirm = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[2]").text
        taiwan_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[3]').text
        taiwan_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[4]').text
    #中国香港数据：
        hongkong_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[2]/div[1]/div[2]').text
        hongkong_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[2]/div[1]/div[3]').text
        hongkong_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[2]/div[1]/div[4]').text
        print(taiwan_confirm,taiwan_cure,taiwan_death,hongkong_confirm,hongkong_cure,hongkong_death)
# 实例化GetEpidemicData类
data = GetEpidemicData()
data.get_domestic_epidemic_data()
data.get_provincial_epidemic_data()


cursor.close()
connection.close()

print("DataCollectSuccessfully")
