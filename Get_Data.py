import pymysql
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 实例化Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://m.111.com.cn/yyw/activities/broadcast/#/home")
driver.implicitly_wait(10)

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
        #更新全国概览数据
        cursor.execute('update TOTAL_EPIDEMIC_DATA set totalNumber = %s',total_number)
        cursor.execute('update TOTAL_EPIDEMIC_DATA set aboardNumber = %s',aboard_number)
        cursor.execute('update TOTAL_EPIDEMIC_DATA set cureNumber = %s', cure_number)
        cursor.execute('update TOTAL_EPIDEMIC_DATA set deathNumber = %s', death_number)
    #输出数据
        print("全国确诊:"+total_number,"境外输入:"+aboard_number,"治愈人数:"+cure_number,"死亡人数:"+death_number)

    def get_provincial_epidemic_data(self):
    #中国台湾数据：
        taiwan_confirm = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[2]").text
        taiwan_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[3]').text
        taiwan_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[4]').text

        cursor.execute('update TAIWAN set confirm = %s',taiwan_confirm)
        cursor.execute('update TAIWAN set cure = %s',taiwan_cure)
        cursor.execute('update TAIWAN set death = %s',taiwan_death)

        print("中国台湾  确诊:"+taiwan_confirm,"治愈:"+taiwan_cure,"死亡:"+taiwan_death)

    #中国香港数据：
        hongkong_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[2]/div[1]/div[2]').text
        hongkong_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[2]/div[1]/div[3]').text
        hongkong_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[2]/div[1]/div[4]').text

        cursor.execute('update HONGKONG set confirm = %s',hongkong_confirm)
        cursor.execute('update HONGKONG set cure = %s',hongkong_cure)
        cursor.execute('update HONGKONG set death = %s',hongkong_death)

        print("中国香港  确诊:"+hongkong_confirm,"治愈:"+hongkong_cure,"死亡:"+hongkong_death)

    # 湖北数据：
        hubei_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[3]/div[1]/div[2]').text
        hubei_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[3]/div[1]/div[3]').text
        hubei_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[3]/div[1]/div[4]').text

        cursor.execute('update HUBEI set confirm = %s',hubei_confirm)
        cursor.execute('update HUBEI set cure = %s', hubei_cure)
        cursor.execute('update HUBEI set death = %s', hubei_death)

        print("湖北   确诊:"+hubei_confirm,"治愈:"+hubei_cure,"死亡:"+hubei_death)
    # 广东数据:
        guangdong_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[4]/div[1]/div[2]').text
        guangdong_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[4]/div[1]/div[3]').text
        guangdong_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[4]/div[1]/div[4]').text

        cursor.execute('update GUANGDONG set confirm = %s',guangdong_confirm)
        cursor.execute('update GUANGDONG set cure = %s', guangdong_cure)
        cursor.execute('update GUANGDONG set death = %s', guangdong_death)

        print("广东   确诊:" + guangdong_confirm, "治愈:" + guangdong_cure, "死亡:" + guangdong_death)

    # 上海数据
        shanghai_confirm = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[7]/div[5]/div[1]/div[2]').text
        shanghai_cure = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[7]/div[5]/div[1]/div[3]').text
        shanghai_death = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[7]/div[5]/div[1]/div[4]').text

        cursor.execute('update SHANGHAI set confirm = %s', shanghai_confirm)
        cursor.execute('update SHANGHAI set cure = %s', shanghai_cure)
        cursor.execute('update SHANGHAI set death = %s', shanghai_death)

        print("上海   确诊:" + shanghai_confirm, "治愈:" + shanghai_cure, "死亡:" + shanghai_death)

# 实例化GetEpidemicData类
data = GetEpidemicData()
data.get_domestic_epidemic_data()
data.get_provincial_epidemic_data()


cursor.close()
connection.close()

print("DataCollectSuccessfully")
