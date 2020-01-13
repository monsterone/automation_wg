from time import sleep

from selenium import webdriver

from selenium.webdriver import ActionChains


# http://47.108.71.92



driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://192.168.1.192:9000/index.html')
driver.find_element_by_xpath('/html/body/div/div/form/div[2]/div/div[1]/input').send_keys('admin')
driver.find_element_by_xpath('html/body/div/div/form/div[3]/div/div/input').send_keys('123456')
driver.find_element_by_xpath('/html/body/div/div/form/div[4]/div/button').click()
sleep(1)

#点击新增设备类型
driver.find_element_by_css_selector('#device-type-container > div.top-option-area > div.btn-area > button > span').click()

###################正常登录成功=====================
'''
#输入设备类型名称
driver.find_element_by_xpath('//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys("hello")

#选择父、子设备
driver.find_element_by_xpath('//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[2]/div/div/div/input').click()

#父设备
# element=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
#子设备
# element=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')

#父设备新css######
element=driver.find_element_by_css_selector('li.el-select-dropdown__item:nth-child(1) > span:nth-child(1)')
#子设备新
# element=driver.find_element_by_css_selector('li.el-select-dropdown__item:nth-child(2) > span:nth-child(1)')

ActionChains(driver).move_to_element(element).click(element).perform()


#登录按钮
# driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[1]/div[3]/div/div[3]/span/button[1]').click()
# driver.find_element_by_css_selector('.save-button').click()
q1=driver.find_element_by_css_selector('.save-button')

ActionChains(driver).move_to_element(q1).click(q1).perform()
#获取登录成功文本值
# text1=driver.find_element_by_css_selector('.el-message__content').text
# print(text1)
'''
#############括号有值不填=====================
'''
##1.设备不选
#输入设备类型名称
driver.find_element_by_xpath('//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[1]/div/div/input').send_keys("kkkk")

#登录按钮
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[1]/div[3]/div/div[3]/span/button[1]').click()

#提示值
text2 = driver.find_element_by_css_selector('.el-form-item__error').text
print(text2)   #请选择所属类型



##2.设备名不填

#选择父、子设备
driver.find_element_by_xpath('//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[2]/div/div/div/input').click()

#父设备
element=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
#子设备
# element=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')

ActionChains(driver).move_to_element(element).click(element).perform()
#登录按钮
driver.find_element_by_css_selector('.save-button').click()

#提示值
text2 = driver.find_element_by_css_selector('.el-form-item__error').text
print(text2)   #请输入设备类型名称

'''

# element1=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[1]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[3]/div/div/svg[1]')
# element1=driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/section/div[1]/div[2]/div[2]/div/div[3]/table/tbody/tr/td[3]/div/div/*[name()="svg"][1]')
# ActionChains(driver).click(element1).perform()


# element2=driver.find_element_by_xpath('//div[@class="option-area"]/*[name()="svg"][1]')
# ActionChains(driver).click(element2).perform()
#
# driver.find_element_by_xpath('//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[1]/div/div/input').clear()
# sleep(2)

#删掉类型
# p1=driver.find_element_by_css_selector('.el-select__caret')
# ActionChains(driver).move_to_element(p1).click(p1).perform()











#选择父、子设备
# driver.find_element_by_xpath('//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[2]/div/div/div/input').click()
#父设备(修改不可用)
# element=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')
#子设备
# element=driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]/span')


# #父设备新
# # element=driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
# #子设备新
# element=driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')

#css
#父设备新######
# # element=driver.find_element_by_css_selector('li.el-select-dropdown__item:nth-child(1) > span:nth-child(1)')
# #子设备新
# element=driver.find_element_by_css_selector('li.el-select-dropdown__item:nth-child(2) > span:nth-child(1)')
#
# ActionChains(driver).move_to_element(element).click(element).perform()
#
# #登录按钮
# driver.find_element_by_css_selector('.save-button').click()

'''
#登录按钮
driver.find_element_by_css_selector('.save-button').click()

# driver.find_element_by_xpath('//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[1]/div/div/input').clear()
# sleep(2)
# # b1=driver.find_element_by_css_selector('td.el-table_1_column_1 > div:nth-child(1)').text
# b1=driver.find_element_by_css_selector('td.el-table_1_column_2 > div:nth-child(1)').text
# print(b1)

'''

