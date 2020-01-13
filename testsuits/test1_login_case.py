import random
from time import sleep

from framework.module import myunit
from pageobjects.login_page import LoginIndexPage
from pageobjects.index_page import FirstIndexPage
from selenium import webdriver
import unittest
from framework.commom.cut_image import Image
class LoginTest(myunit.MyTest):

    def test_login_user_pawd_null(self):
        '''用户名、密码为空登录'''
        page = LoginIndexPage(self.driver)
        page.get(self.base_url)
        # page.username_input.send_keys("")
        # page.password_input.send_keys("11")
        # page.login_button.click()
        page.login_action("", "11")
        sleep(2)
        self.assertEqual(page.type_loginFail_hint1(), '请输入用户名')
        Image.inser_img(self.driver,'login_user_pawd_null.png')

    def test_login_pawd_null(self):
        '''密码为空登录'''
        page = LoginIndexPage(self.driver)
        page.get(self.base_url)
        page.login_action('admin','')
        sleep(2)
        self.assertEqual(page.type_loginFail_hint1(), '请输入密码')
        Image.inser_img(self.driver, 'login_pawd_null.png')
    def test_login_user_pawd_error(self):
        '''用户名、密码为错误'''
        page = LoginIndexPage(self.driver)
        page.get(self.base_url)
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "test" + character
        page.login_action(username,'@#$%')
        sleep(2)
        # self.assertIn(page.type_loginFail_hint2(), '账号或密码不正确')
        self.assertIn(page.type_loginFail_hint2(), '账号或密码不匹配')
        # self.assertEqual(po.login_error_hint(), '请先进行验证')
        Image.inser_img(self.driver, 'login_user_pawd_error.png')
    def test_login_success(self):
        '''用户名、密码正确，登录成功'''
        page = LoginIndexPage(self.driver)
        page.get(self.base_url)
        user = "admin"
        page.login_action(user,'123456')
        sleep(2)
        po2 = FirstIndexPage(self.driver)
        self.assertEqual(po2.user_logon.text, '')
        Image.inser_img(self.driver, 'login_success.png')
if __name__ == '__main__':
    unittest.main()
