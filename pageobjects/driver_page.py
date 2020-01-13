from time import sleep

from poium import Page, PageElement, PageWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import os
class DriverIndexPage(Page):

    ###################新增操作###################

    #点击新增设备类型
    # driver_add = PageElement(css='.next-button > span:nth-child(1)')
    driver_add = PageElement(css='#device-type-container > div.top-option-area > div.btn-area > button > span')
    # 输入设备类型名称
    driver_name_input=PageElement(xpath='//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[1]/div/div/input')

    #下拉弹出设备选择框
    driver_types=PageElement(xpath='//*[@id="device-type-container"]/div[3]/div/div[2]/form/div[2]/div/div/div/input')
    #选择父设备类型
    driver_type_parents=PageElement(css='li.el-select-dropdown__item:nth-child(1) > span:nth-child(1)')
    # 选择子设备类型(firefox可以)
    driver_type_childs = PageElement(css='li.el-select-dropdown__item:nth-child(2) > span:nth-child(1)')

    #确认按钮
    driver_ok=PageElement(css='.save-button')

    # 获取登录成功文本值
    driver_add_success=PageElement(css='.el-message__content')
    #设备类型为空提示值
    driver_type_null=PageElement(css='.el-form-item__error')
    # 设备名称为空提示值
    driver_name_null = PageElement(css='.el-form-item__error')
    #设备名称已存在
    driver_name_exits=PageElement(css='.el-message__content')

    #添加成功
    def driver_action_success(self,name):
        self.driver_add.click()
        self.driver_name_input.send_keys(name)
        PageWait(self.driver_types,10)
        # self.driver_types.click()
        self.driver_types.send_keys(Keys.ENTER)
        ActionChains(self.driver).move_to_element(self.driver_type_parents).click(self.driver_type_parents).perform()
        ActionChains(self.driver).move_to_element(self.driver_ok).click(self.driver_ok).perform()
        # self.driver_ok.click()

    #只填name(设备类型null)
    def driver_action_type_null(self,name):
        self.driver_add.click()
        self.driver_name_input.send_keys(name)
        self.driver_ok.click()

    #只选设备类型(设备名称null)
    def driver_action_name_null(self):
        self.driver_add.click()
        # PageWait(self.driver_types)
        # self.driver_types.click()
        self.driver_types.send_keys(Keys.ENTER)  #无头浏览器无法点击，可用
        ActionChains(self.driver).move_to_element(self.driver_type_parents).click(self.driver_type_parents).perform()
        ActionChains(self.driver).move_to_element(self.driver_ok).click(self.driver_ok).perform()
        # self.driver_ok.click()



    #添加成功（断言）
    def add_success_hint(self):
        return self.driver_add_success.text

    #设备名称为空提示值(断言)
    def name_null_hint(self):
        return self.driver_name_null.text

    # 设备类型为空提示值(断言)
    def type_null_hint(self):
        return self.driver_type_null.text

    #设备名称已存在（断言）
    def name_exits_hint(self):
        return self.driver_name_exits.text


############修改操作#################

    #修改按钮 ,#输入框和选择框同新增
    fix_button=PageElement(xpath='//div[@class="option-area"]/*[name()="svg"][1]')
    #修改成功信息文本框
    fix_success=PageElement(css='.el-message__content')

    #名称修改确认
    fix_name_affirm =PageElement(css='td.el-table_1_column_1 > div:nth-child(1)')
    # 类型修改确认
    fix_type_affirm = PageElement(css='td.el-table_1_column_2 > div:nth-child(1)')



    # 修改设备名称
    def driver_fix_name(self, name):

        ActionChains(self.driver).click(self.fix_button).perform()
        # self.driver_name_input.clear()
        ##firefox-clear不了，双击清除(firefox也不行，chrom简单的可以)
        # ActionChains(self.driver).double_click(self.driver_name_input).perform()
        ##用keys操作(firefox，chrome通用)
        self.driver_name_input.send_keys(Keys.CONTROL,'a')
        self.driver_name_input.send_keys(Keys.CONTROL,'x')
        self.driver_name_input.send_keys(name)
        self.driver_ok.click()

    #修改设备类型
    def driver_fix_type(self):

        ActionChains(self.driver).click(self.fix_button).perform()
        PageWait(self.driver_types)
        # self.driver_types.click()
        self.driver_types.send_keys(Keys.ENTER)
        ActionChains(self.driver).move_to_element(self.driver_type_childs).click(self.driver_type_childs).perform()
        ActionChains(self.driver).move_to_element(self.driver_ok).click(self.driver_ok).perform()


    #修改成功信息文本框（断言）
    def driver_fix_success(self):
        return self.fix_success.text

    # 名称修改确认(断言)
    def driver_name_affirm(self):
        return self.fix_name_affirm.text

    # 类型修改确认(断言)
    def driver_type_affirm(self):
        return self.fix_type_affirm.text


########################删除操作===============

    #删除按钮 ,#输入框和选择框同新增
    del_button=PageElement(xpath='//div[@class="option-area"]/*[name()="svg"][2]')

    #取消删除按钮
    cancel_del=PageElement(css='button.el-button--default:nth-child(1) > span:nth-child(1)')
    #确认删除按钮
    affirm_del=PageElement(css='button.el-button:nth-child(2) > span:nth-child(1)')

    #取消文本提示
    cancel_text = PageElement(css='.el-message__content')
    #删除成功文本提示
    affirm_text = PageElement(css='.el-message__content')


    #取消删除操作
    def driver_cancel_del(self):
        ActionChains(self.driver).click(self.del_button).perform()
        self.cancel_del.click()

    # 确认删除操作，删除成功
    def driver_affirm_del(self):
        ActionChains(self.driver).click(self.del_button).perform()
        self.affirm_del.click()

    # 取消文本提示(断言)
    def cancel_del_fint(self):
        return self.cancel_text.text

    # 删除成功文本提示(断言)
    def affirm_text_fint(self):
        return self.affirm_text.text


########模型、图片上传############

    ##资源管理按钮
    resource_button=PageElement(css='tr.el-table__row:nth-child(1) > td:nth-child(3) > div:nth-child(1) > div:nth-child(1) > span:nth-child(3)')
    ##上传模型按钮
    up_model=PageElement(css='.el-upload--text > button:nth-child(1) > span:nth-child(1) > i:nth-child(1)')
    ##切换图标按钮
    ex_photo=PageElement(css='#tab-image')
    ##上传图片
    up_photo=PageElement(css='.el-upload--picture > button:nth-child(1) > span:nth-child(1) > i:nth-child(1)')

    ##文本提示信息
    msg_text=PageElement(css='.el-message__content')



    ####上传错误模型（实际为图片)
    def up_model_error(self):
        self.resource_button.click()
        self.up_model.click()
        ##上传模型（谷歌）
        # os.system(r"G:\selenium_up\modelup_chrome.exe")
        ##上传模型(火狐)
        os.system(r"G:\selenium_up\modelup.exe")



    ###上传图标（成功）
    def up_photo_success(self):
        self.resource_button.click()
        self.ex_photo.click()
        self.up_photo.click()

        ##上传图片（谷歌）
        # os.system(r"G:\selenium_up\modelup_chrome.exe")
        ##上传模型(火狐)
        os.system(r"G:\selenium_up\modelup.exe")


    # 上传模型(断言)
    def up_hint(self):
       return self.msg_text.text


