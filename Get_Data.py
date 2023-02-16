import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get("https://m.111.com.cn/yyw/activities/broadcast/#/home")
time.sleep(2)
'''
获取全国疫情总览数据
'''
def get_epidemic_data():
#全国确诊
    total_number = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/ul[2]/li[1]/div[2]/div[1]/div[2]').text
#境外输入
    aboard_number = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/ul[2]/li[1]/div[2]/div[2]/div[2]').text
#治愈人数
    cure_number = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/ul[2]/li[1]/div[2]/div[3]/div[2]').text
#死亡人数
    death_number = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[2]/ul[2]/li[1]/div[2]/div[4]/div[2]').text
#输出数据
    print("全国确诊"+total_number,"境外输入"+aboard_number,"治愈人数"+cure_number,"死亡人数"+death_number)

''' testsd'''
get_epidemic_data()

