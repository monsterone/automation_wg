from time import sleep

from selenium import webdriver

from selenium.webdriver import ActionChains


# http://47.108.71.92



driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://47.108.71.92')
driver.find_element_by_xpath('/html/body/div/div/form/div[2]/div/div[1]/input').send_keys('admin')
driver.find_element_by_xpath('html/body/div/div/form/div[3]/div/div/input').send_keys('123456')
driver.find_element_by_xpath('/html/body/div/div/form/div[4]/div/button').click()
sleep(1)



element=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[1]/*[name()="svg"][1]')

ActionChains(driver).click(element).perform()

