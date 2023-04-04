import csv

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
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[36]/strong').click()


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
    print("\r")
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
    # 中国台湾数据：
        taiwan_confirm = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[2]").text
        taiwan_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[3]').text
        taiwan_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[1]/div[1]/div[4]').text


        cursor.execute('update TAIWAN set confirm = %s',taiwan_confirm)
        cursor.execute('update TAIWAN set cure = %s',taiwan_cure)
        cursor.execute('update TAIWAN set death = %s',taiwan_death)

        print("中国台湾  确诊:"+taiwan_confirm, "治愈:"+taiwan_cure, "死亡:"+taiwan_death)

    # 中国香港数据：
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

    # 吉林数据
        jilin_confirm = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[7]/div[6]/div[1]/div[2]').text
        jilin_cure = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[7]/div[6]/div[1]/div[3]').text
        jilin_death = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[7]/div[6]/div[1]/div[4]').text

        cursor.execute('update JILIN set confirm = %s',jilin_confirm)
        cursor.execute('update JILIN set cure = %s', jilin_cure)
        cursor.execute('update JILIN set death = %s', jilin_death)

        print("吉林   确诊:" + jilin_confirm, "治愈:" + jilin_cure, "死亡:" + jilin_death)

    # 北京数据:
        beijing_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[7]/div[1]/div[2]').text
        beijing_cure =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[7]/div[1]/div[3]').text
        beijing_death =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[7]/div[1]/div[4]').text

        cursor.execute('update BEIJING set confirm = %s',beijing_confirm)
        cursor.execute('update BEIJING set cure = %s', beijing_cure)
        cursor.execute('update BEIJING set death = %s', beijing_death)

        print("北京   确诊:" + beijing_confirm, "治愈:" + beijing_cure, "死亡:" + beijing_death)

    # 四川数据:
        sichuan_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[8]/div[1]/div[2]').text
        sichuan_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[8]/div[1]/div[3]').text
        sichuan_death =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[8]/div[1]/div[4]').text

        cursor.execute('update SICHUAN set confirm = %s',sichuan_confirm)
        cursor.execute('update SICHUAN set cure = %s', sichuan_cure)
        cursor.execute('update SICHUAN set death = %s', sichuan_death)

        print("四川   确诊:" + sichuan_confirm, "治愈:" + sichuan_cure, "死亡:" + sichuan_death)

    # 重庆数据:
        chongqing_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[9]/div[1]/div[2]').text
        chongqing_cure =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[9]/div[1]/div[3]').text
        chongqing_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[9]/div[1]/div[4]').text

        cursor.execute('update CHONGQING set confirm = %s',chongqing_confirm)
        cursor.execute('update CHONGQING set cure = %s',chongqing_cure)
        cursor.execute('update CHONGQING set death = %s',chongqing_death)

        print("重庆   确诊:" + chongqing_confirm, "治愈:" + chongqing_cure, "死亡:" + chongqing_death)

    # 海南数据:
        hainan_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[10]/div[1]/div[2]').text
        hainan_cure =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[10]/div[1]/div[3]').text
        hainan_death =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[10]/div[1]/div[4]').text

        cursor.execute('update HAINAN set confirm = %s',hainan_confirm)
        cursor.execute('update HAINAN set cure = %s', hainan_cure)
        cursor.execute('update HAINAN set death = %s', hainan_death)

        print("海南   确诊:" + hainan_confirm, "治愈:" + hainan_cure, "死亡:" + hainan_death)

    # 河南数据:
        henan_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[11]/div[1]/div[2]').text
        henan_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[11]/div[1]/div[3]').text
        henan_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[11]/div[1]/div[4]').text

        cursor.execute('update HENAN set confirm = %s',henan_confirm)
        cursor.execute('update HENAN set cure = %s', henan_cure)
        cursor.execute('update HENAN set death = %s', henan_death)

        print("河南   确诊:" + henan_confirm, "治愈:" + henan_cure, "死亡:" + henan_death)

    # 福建数据:
        fujian_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[12]/div[1]/div[2]').text
        fujian_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[12]/div[1]/div[3]').text
        fujian_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[12]/div[1]/div[4]').text

        cursor.execute('update FUJIAN set confirm = %s',fujian_confirm)
        cursor.execute('update FUJIAN set cure = %s',fujian_cure)
        cursor.execute('update FUJIAN set death = %s', fujian_death)

        print("福建   确诊:" + fujian_confirm, "治愈:" + fujian_cure, "死亡:" + fujian_death)

    # 内蒙古数据:
        neimenggu_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[13]/div[1]/div[2]').text
        neimenggu_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[13]/div[1]/div[3]').text
        neimenggu_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[13]/div[1]/div[4]').text

        cursor.execute('update NEIMENGGU set confirm = %s',neimenggu_confirm)
        cursor.execute('update NEIMENGGU set cure = %s',neimenggu_cure)
        cursor.execute('update NEIMENGGU set death = %s', neimenggu_death)

        print("内蒙古 确诊:" + neimenggu_confirm, "治愈:" + neimenggu_cure, "死亡:" + neimenggu_death)

    # 浙江数据:
        zhejiang_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[14]/div[1]/div[2]').text
        zhejiang_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[14]/div[1]/div[3]').text
        zhejiang_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[14]/div[1]/div[4]').text

        cursor.execute('update ZHEJIANG set confirm = %s',zhejiang_confirm)
        cursor.execute('update ZHEJIANG set cure = %s', zhejiang_cure)
        cursor.execute('update ZHEJIANG set death = %s', zhejiang_death)

        print("浙江   确诊:" + zhejiang_confirm, "治愈:" + zhejiang_cure, "死亡:" + zhejiang_death)

    # 云南数据:
        yunnan_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[15]/div[1]/div[2]').text
        yunnan_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[15]/div[1]/div[3]').text
        yunnan_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[15]/div[1]/div[4]').text

        cursor.execute('update YUNNAN set confirm = %s',yunnan_confirm)
        cursor.execute('update YUNNAN set cure = %s', yunnan_cure)
        cursor.execute('update YUNNAN set death = %s',yunnan_death)

        print("云南   确诊:" + yunnan_confirm, "治愈:" + yunnan_cure, "死亡:" + yunnan_death)

    # 陕西数据:
        shanxi_west_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[16]/div[1]/div[2]').text
        shanxi_west_cure =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[16]/div[1]/div[3]').text
        shanxi_west_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[16]/div[1]/div[4]').text

        cursor.execute('update SHANXI_WEST set confirm = %s',shanxi_west_confirm)
        cursor.execute('update SHANXI_WEST set cure = %s', shanxi_west_cure)
        cursor.execute('update SHANXI_WEST set death = %s', shanxi_west_death)

        print("陕西   确诊:" + shanxi_west_confirm, "治愈:" + shanxi_west_cure, "死亡:" + shanxi_west_death)

    # 黑龙江数据:
        heilongjiang_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[17]/div[1]/div[2]').text
        heilongjiang_cure =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[17]/div[1]/div[3]').text
        heilongjiang_death =  driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[17]/div[1]/div[4]').text

        cursor.execute('update HEILONGJIANG set confirm = %s ',heilongjiang_confirm)
        cursor.execute('update HEILONGJIANG set cure = %s ', heilongjiang_cure)
        cursor.execute('update HEILONGJIANG set death = %s ',heilongjiang_death)

        print("黑龙江 确诊:" + heilongjiang_confirm, "治愈:" + heilongjiang_cure, "死亡:" + heilongjiang_death)

    # 山西数据:
        shanxi_north_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[18]/div[1]/div[2]').text
        shanxi_north_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[18]/div[1]/div[3]').text
        shanxi_north_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[18]/div[1]/div[4]').text

        cursor.execute('update SHANXI_NORTH set confirm = %s',shanxi_north_confirm)
        cursor.execute('update SHANXI_NORTH set cure = %s', shanxi_north_cure)
        cursor.execute('update SHANXI_NORTH set death = %s', shanxi_north_death)

        print("山西   确诊:" + shanxi_north_confirm, "治愈:" + shanxi_north_cure, "死亡:" + shanxi_north_death)

    # 山东数据:
        shandong_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[19]/div[1]/div[2]').text
        shandong_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[19]/div[1]/div[3]').text
        shandong_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[19]/div[1]/div[4]').text

        cursor.execute('update SHANDONG set confirm = %s',shandong_confirm)
        cursor.execute('update SHANDONG set cure = %s',shandong_cure)
        cursor.execute('update SHANDONG set death = %s', shandong_death)

        print("山东   确诊:" + shandong_confirm, "治愈:" + shandong_cure, "死亡:" + shandong_death)

    # 江苏数据:
        jiangsu_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[20]/div[1]/div[2]').text
        jiangsu_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[20]/div[1]/div[3]').text
        jiangsu_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[20]/div[1]/div[4]').text

        cursor.execute('update JIANGSU set confirm = %s',jiangsu_confirm)
        cursor.execute('update JIANGSU set cure = %s', jiangsu_cure)
        cursor.execute('update JIANGSU set death = %s', jiangsu_death)

        print("江苏   确诊:" + jiangsu_confirm, "治愈:" + jiangsu_cure, "死亡:" + jiangsu_death)

    # 辽宁数据:
        liaoning_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[21]/div[1]/div[2]').text
        liaoning_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[21]/div[1]/div[3]').text
        liaoning_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[21]/div[1]/div[4]').text

        cursor.execute('update LIAONING set confirm = %s',liaoning_confirm)
        cursor.execute('update LIAONING set cure = %s',liaoning_cure)
        cursor.execute('update LIAONING set death = %s',liaoning_death)

        print("江苏   确诊:" + liaoning_confirm, "治愈:" + liaoning_cure, "死亡:" + liaoning_death)

    # 湖南数据:
        hunan_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[22]/div[1]/div[2]').text
        hunan_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[22]/div[1]/div[3]').text
        hunan_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[22]/div[1]/div[4]').text

        cursor.execute('update HUNAN set confirm = %s',hunan_confirm)
        cursor.execute('update HUNAN set cure = %s', hunan_cure)
        cursor.execute('update HUNAN set death = %s',hunan_death)

        print("湖南   确诊:" + hunan_confirm, "治愈:" + hunan_cure, "死亡:" + hunan_death)

    # 天津数据:
        tianjin_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[23]/div[1]/div[2]').text
        tianjin_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[23]/div[1]/div[3]').text
        tianjin_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[23]/div[1]/div[4]').text

        cursor.execute('update TIANJIN set confirm = %s',tianjin_confirm)
        cursor.execute('update TIANJIN set cure = %s', tianjin_cure)
        cursor.execute('update TIANJIN set death = %s', tianjin_death)

        print("天津   确诊:" + tianjin_confirm, "治愈:" + tianjin_cure, "死亡:" + tianjin_death)

    # 河北数据:
        hebei_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[24]/div[1]/div[2]').text
        hebei_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[24]/div[1]/div[3]').text
        hebei_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[24]/div[1]/div[4]').text

        cursor.execute('update HEBEI set confirm = %s',hebei_confirm)
        cursor.execute('update HEBEI set cure = %s', hebei_cure)
        cursor.execute('update HEBEI set death = %s', hebei_death)

        print("河北   确诊:" + hebei_confirm, "治愈:" + hebei_cure, "死亡:" + hebei_death)

    # 新疆数据:
        xinjiang_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[25]/div[1]/div[2]').text
        xinjiang_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[25]/div[1]/div[3]').text
        xinjiang_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[25]/div[1]/div[4]').text

        cursor.execute('update XINJIANG set confirm = %s',xinjiang_confirm)
        cursor.execute('update XINJIANG set cure = %s', xinjiang_cure)
        cursor.execute('update XINJIANG set death = %s', xinjiang_death)

        print("新疆   确诊:" + xinjiang_confirm, "治愈:" + xinjiang_cure, "死亡:" + xinjiang_death)

    # 广西数据:
        guangxi_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[26]/div[1]/div[2]').text
        guangxi_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[26]/div[1]/div[3]').text
        guangxi_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[26]/div[1]/div[4]').text

        cursor.execute('update GUANGXI set confirm = %s',guangxi_confirm)
        cursor.execute('update GUANGXI set cure = %s',guangxi_cure)
        cursor.execute('update GUANGXI set death = %s',guangxi_death)

        print("广西   确诊:" + guangxi_confirm, "治愈:" + guangxi_cure, "死亡:" + guangxi_death)

    # 江西数据:
        jiangxi_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[27]/div[1]/div[2]').text
        jiangxi_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[27]/div[1]/div[3]').text
        jiangxi_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[27]/div[1]/div[4]').text

        cursor.execute('update JIANGXI set confirm = %s',jiangxi_confirm)
        cursor.execute('update JIANGXI set cure = %s', jiangxi_cure)
        cursor.execute('update JIANGXI set death = %s', jiangxi_death)

        print("江西   确诊:" + jiangxi_confirm, "治愈:" + jiangxi_cure, "死亡:" + jiangxi_death)

    # 中国澳门数据:
        aomen_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[28]/div[1]/div[2]').text
        aomen_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[28]/div[1]/div[3]').text
        aomen_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[28]/div[1]/div[4]').text

        cursor.execute('update AOMEN set confirm = %s',aomen_confirm)
        cursor.execute('update AOMEN set cure = %s', aomen_cure)
        cursor.execute('update AOMEN set death = %s', aomen_death)

        print("中国澳门   确诊:" + aomen_confirm, "治愈:" + aomen_cure, "死亡:" + aomen_death)

    # 贵州数据:
        guizhou_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[29]/div[1]/div[2]').text
        guizhou_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[29]/div[1]/div[3]').text
        guizhou_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[29]/div[1]/div[4]').text

        cursor.execute('update GUIZHOU set confirm = %s',guizhou_confirm)
        cursor.execute('update GUIZHOU set cure = %s', guizhou_cure)
        cursor.execute('update GUIZHOU set death = %s', guizhou_death)

        print("贵州   确诊:" + guizhou_confirm, "治愈:" + guizhou_cure, "死亡:" + guizhou_death)

    # 安徽数据:
        anhui_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[30]/div[1]/div[2]').text
        anhui_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[30]/div[1]/div[3]').text
        anhui_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[30]/div[1]/div[4]').text

        cursor.execute('update ANHUI set confirm = %s',anhui_confirm)
        cursor.execute('update ANHUI set cure = %s', anhui_cure)
        cursor.execute('update ANHUI set death = %s', anhui_death)

        print("安徽   确诊:" + anhui_confirm, "治愈:" + anhui_cure, "死亡:" + anhui_death)

    # 甘肃数据:
        gansu_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[31]/div[1]/div[2]').text
        gansu_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[31]/div[1]/div[3]').text
        gansu_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[31]/div[1]/div[4]').text

        cursor.execute('update GANSU set confirm = %s',gansu_confirm)
        cursor.execute('update GANSU set cure = %s', gansu_cure)
        cursor.execute('update GANSU set death = %s', gansu_death)

        print("甘肃   确诊:" + gansu_confirm, "治愈:" + gansu_cure, "死亡:" + gansu_death)

    # 西藏数据:
        xizang_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[32]/div[1]/div[2]').text
        xizang_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[32]/div[1]/div[3]').text
        xizang_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[32]/div[1]/div[4]').text

        cursor.execute('update XIZANG set confirm = %s',xizang_confirm)
        cursor.execute('update XIZANG set cure = %s', xizang_cure)
        cursor.execute('update XIZANG set death = %s', xizang_death)

        print("西藏   确诊:" + xizang_confirm, "治愈:" + xizang_cure, "死亡:" + xizang_death)

    # 青海数据:
        qinghai_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[33]/div[1]/div[2]').text
        qinghai_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[33]/div[1]/div[3]').text
        qinghai_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[33]/div[1]/div[4]').text

        cursor.execute('update QINGHAI set confirm = %s',qinghai_confirm)
        cursor.execute('update QINGHAI set cure = %s', qinghai_cure)
        cursor.execute('update QINGHAI set death = %s', qinghai_death)

        print("青海   确诊:" + qinghai_confirm, "治愈:" + qinghai_cure, "死亡:" + qinghai_death)

    # 宁夏数据:
        ningxia_confirm = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[34]/div[1]/div[2]').text
        ningxia_cure = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[34]/div[1]/div[3]').text
        ningxia_death = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[7]/div[34]/div[1]/div[4]').text

        cursor.execute('update NINGXIA set confirm = %s',ningxia_confirm)
        cursor.execute('update NINGXIA set cure = %s', ningxia_cure)
        cursor.execute('update NINGXIA set death = %s', ningxia_death)

        print("宁夏   确诊:" + ningxia_confirm, "治愈:" + ningxia_cure, "死亡:" + ningxia_death)

        # 将爬取的数据写入csv文件内:
        file = open('data.csv', 'w', encoding='utf-8', newline="")
        csv_write = csv.writer(file)
        # 写入csv表头
        csv_write.writerow(['地区', '确诊', '治愈', '死亡'])
        # 写入csv具体数据
        csv_write.writerow(['台湾省', taiwan_confirm, taiwan_cure, taiwan_death])
        csv_write.writerow(['香港特别行政区', hongkong_confirm, hongkong_cure, hongkong_death])
        csv_write.writerow(['湖北省', hubei_confirm, hubei_cure, hubei_death])
        csv_write.writerow(['广东省', guangdong_confirm, guangdong_cure, guangdong_death])
        csv_write.writerow(['上海市', shanghai_confirm, shanghai_cure, shanghai_death])
        csv_write.writerow(['吉林省', jilin_confirm, jilin_cure, jilin_death])
        csv_write.writerow(['北京市', beijing_confirm, beijing_cure, beijing_death])
        csv_write.writerow(['四川省', sichuan_confirm, sichuan_cure, sichuan_death])
        csv_write.writerow(['重庆省', chongqing_confirm, chongqing_cure, chongqing_death])
        csv_write.writerow(['海南省', hainan_confirm, hainan_cure, hainan_death])
        csv_write.writerow(['河南省', henan_confirm, henan_cure, henan_death])
        csv_write.writerow(['福建省', fujian_confirm, fujian_cure, fujian_death])
        csv_write.writerow(['内蒙古自治区', neimenggu_confirm, neimenggu_cure, neimenggu_death])
        csv_write.writerow(['浙江省', zhejiang_confirm, zhejiang_cure, zhejiang_death])
        csv_write.writerow(['云南省', yunnan_confirm, yunnan_cure, yunnan_death])
        csv_write.writerow(['陕西省', shanxi_west_confirm, shanxi_west_cure, shanxi_west_death])
        csv_write.writerow(['黑龙江省', heilongjiang_confirm, heilongjiang_cure, heilongjiang_death])
        csv_write.writerow(['山西省', shanxi_north_confirm, shanxi_north_cure, shanxi_north_death])
        csv_write.writerow(['山东省', shandong_confirm, shandong_cure, shandong_death])
        csv_write.writerow(['江苏省', jiangsu_confirm, jiangsu_cure, jiangsu_death])
        csv_write.writerow(['辽宁省', liaoning_confirm, liaoning_cure, liaoning_death])
        csv_write.writerow(['湖南省', hunan_confirm, hunan_cure, hunan_death])
        csv_write.writerow(['天津市', tianjin_confirm, tianjin_cure, tianjin_death])
        csv_write.writerow(['河北省', hebei_confirm, hebei_cure, hebei_death])
        csv_write.writerow(['新疆维吾尔自治区', xinjiang_confirm, xinjiang_cure, xinjiang_death])
        csv_write.writerow(['广西壮族自治区', guangxi_confirm, guangxi_cure, guangxi_death])
        csv_write.writerow(['江西省', jiangxi_confirm, jiangxi_cure, jiangxi_death])
        csv_write.writerow(['澳门特别行政区', aomen_confirm, aomen_cure, aomen_death])
        csv_write.writerow(['贵州省', guizhou_confirm, guizhou_cure, guizhou_death])
        csv_write.writerow(['安徽省', anhui_confirm, anhui_cure, anhui_death])
        csv_write.writerow(['甘肃省', gansu_confirm, gansu_cure, gansu_death])
        csv_write.writerow(['西藏自治区', xizang_confirm, xizang_cure, xizang_death])
        csv_write.writerow(['青海省', qinghai_confirm, qinghai_cure, qinghai_death])
        csv_write.writerow(['宁夏回族自治区', ningxia_confirm, ningxia_cure, ningxia_death])
        csv_write.writerow(['重庆市', chongqing_confirm, chongqing_cure, chongqing_death])
        file.close()

print("Start to collect data------")
# # 实例化GetEpidemicData类
data = GetEpidemicData()
data.get_domestic_epidemic_data()
data.get_provincial_epidemic_data()
print("End to collect data------")
time.sleep(1)

print("\r")
print("DataCollectSuccessfully")
print("\r")

cursor.close()
connection.close()
print("DBDisconnectSuccessfully")