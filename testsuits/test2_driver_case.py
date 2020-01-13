import random
from time import sleep

from framework.module import myunit
from pageobjects.driver_page import DriverIndexPage
from pageobjects.login_page import LoginIndexPage
# from pageobjects.index_page import FirstIndexPage
from selenium import webdriver
import unittest
from framework.commom.cut_image import Image
class DriverTest(myunit.MyTest):

    def login_case(self):
        page = LoginIndexPage(self.driver)
        page.get(self.base_url)
        page.login_action('admin', '123456')


    ##########新增设备类型############

    def test01_driver_add_name_null(self):
        '''设备名为空，设备类型父设备'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.driver_action_name_null()
        sleep(1)
        self.assertEqual(page.name_null_hint(), '请输入设备类型名称')
        Image.inser_img(self.driver,'driver_add_name_null.png')


    def test02_driver_add_type_null(self):
        '''设备类型为空'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.driver_action_type_null('add10')
        sleep(1)
        self.assertEqual(page.type_null_hint(), '请选择所属类型')
        Image.inser_img(self.driver, 'driver_add_type_null.png')

    def test03_driver_add_success(self):
        '''添加成功'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.driver_action_success('monster')
        sleep(1)
        self.assertEqual(page.add_success_hint(), '添加成功')
        Image.inser_img(self.driver, 'driver_add_success.png')


    def test04_driver_add_exits(self):
        '''添加设备名称已存在'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.driver_action_success('monster')
        sleep(1)
        self.assertEqual(page.name_exits_hint(), '当前设备类型名称已存在')
        Image.inser_img(self.driver, 'driver_name_exits.png')

    # #################修改################

    def test05_driver_fix_name(self):
        '''修改设备名称'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.driver_fix_name('怪兽')
        sleep(1)
        self.assertEqual(page.driver_fix_success(),'修改成功')
        self.assertEqual(page.driver_name_affirm(),'怪兽')
        Image.inser_img(self.driver, 'driver_fix_name.png')


    def test06_driver_fix_type(self):
        '''修改设备类型，改为子设备'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.driver_fix_type()
        sleep(1)
        self.assertEqual(page.driver_fix_success(),'修改成功')
        self.assertEqual(page.driver_type_affirm(),'子设备类型')
        Image.inser_img(self.driver, 'driver_fix_type.png')


    ###############上传模型、图片#########
    @unittest.skip('8')
    def test07_upmodel_error(self):
        '''上传错误模型'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.up_model_error()
        sleep(3)
        self.assertEqual(page.up_hint(),'所选文件必须包含obj文件')
        Image.inser_img(self.driver, 'upmodel_error.png')

    @unittest.skip('8')
    def test08_upphoto_success(self):
        '''上传图片成功'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.up_photo_success()
        sleep(3)
        self.assertEqual(page.up_hint(),'上传成功!')
        Image.inser_img(self.driver, 'upphoto_success.png')


    ###########################删除######################

    def test09_1driver_del_cannel(self):
        '''取消删除'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.driver_cancel_del()
        sleep(1)
        self.assertEqual(page.cancel_del_fint(),'已取消删除')
        # self.assertEqual(page.driver_name_affirm(),'怪兽')
        Image.inser_img(self.driver, 'driver_del_cannel.png')


    def test09_2driver_del_affirm(self):
        '''删除成功'''
        self.login_case()
        page = DriverIndexPage(self.driver)
        page.driver_affirm_del()
        sleep(1)
        self.assertEqual(page.affirm_text_fint(),'删除成功!')
        Image.inser_img(self.driver, 'driver_del_affirm.png')


if __name__ == '__main__':
    unittest.main()
