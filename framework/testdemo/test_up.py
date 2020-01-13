
from time import sleep

from selenium import webdriver

from selenium.webdriver import ActionChains
import os

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://192.168.1.192:9000/index.html')
driver.find_element_by_xpath('/html/body/div/div/form/div[2]/div/div[1]/input').send_keys('admin')
driver.find_element_by_xpath('html/body/div/div/form/div[3]/div/div/input').send_keys('123456')
driver.find_element_by_xpath('/html/body/div/div/form/div[4]/div/button').click()
sleep(1)


##模型上传

##点击资源管理
driver.find_element_by_css_selector('tr.el-table__row:nth-child(1) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)').click()
'''
##点击上传模型，打开windows上传窗口
driver.find_element_by_css_selector('.el-upload--text > button:nth-child(1) > span:nth-child(1) > i:nth-child(1)').click()

'''

# #调用upfile.exe上传程序
# os.system("D:\\upfile.exe")

# os.system(r"G:\selenium_up\modelup.exe")

# os.system(r"G:\selenium_up\modelup.exe")


# 上传模型/图片
# .el-message__content
# 所选文件必须包含obj文件
#上传成功！




#图标管理
driver.find_element_by_css_selector('#tab-image').click()
#上传图标
driver.find_element_by_css_selector('.el-upload--picture > button:nth-child(1) > span:nth-child(1) > i:nth-child(1)').click()

#火狐上传（上传框名称不一样：上传文件）
# os.system(r"G:\selenium_up\modelup.exe")
#谷歌上传（上传框名称不一样：打开）
os.system(r"G:\selenium_up\modelup_chrome.exe")


sleep(3)
#
# driver.quit()