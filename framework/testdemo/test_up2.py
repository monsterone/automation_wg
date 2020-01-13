
from selenium import webdriver
import win32gui
import win32con
import time
from framework.commom.windows_up import firefox_up,chrome_up

# from pymouse import PyMouse


# dr = webdriver.Firefox()
# dr.get('http://sahitest.com/demo/php/fileUpload.htm')
# # upload = dr.find_element_by_id('file')
# upload = dr.find_element_by_css_selector('#file').click()
# time.sleep(1)
#
# # win32gui
# dialog = win32gui.FindWindow('#32770',r'文件上传')  #对话框
# ComboBoxEx32 = win32gui.FindWindow(dialog,0,'ComBoxEx32',None)
# ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
# Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
# button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
# win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, r'C:\Users\pc\Desktop\目录A\1.Redgex测试\图片\AA.jpg')  # 往输入框输入绝对地址
# win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
#
# print(upload.get_attribute('value'))
# dr.quit()


# driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('http://192.168.1.192:9000/index.html')
driver.find_element_by_xpath('/html/body/div/div/form/div[2]/div/div[1]/input').send_keys('admin')
driver.find_element_by_xpath('html/body/div/div/form/div[3]/div/div/input').send_keys('123456')
driver.find_element_by_xpath('/html/body/div/div/form/div[4]/div/button').click()
time.sleep(1)


##模型上传

##点击资源管理
driver.find_element_by_css_selector('tr.el-table__row:nth-child(1) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)').click()

##点击上传模型，打开windows上传窗口
driver.find_element_by_css_selector('.el-upload--text > button:nth-child(1) > span:nth-child(1) > i:nth-child(1)').click()


#firefox上传
# firefox_up()

#chrome上传
# chrome_up()



#Sendkeys
SendKeys.SendKeys('G:\\selenium_up\\picture\\AA.jpg')  # 发送文件地址

SendKeys.SendKeys("{ENTER}") # 发送回车键