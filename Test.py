from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://m.111.com.cn/yyw/activities/broadcast/#/home')
driver.implicitly_wait(5)

death = driver.find_elements(By.XPATH,'//*[@class="widget-tab-box"]')

for i in death:
    print(i.text)