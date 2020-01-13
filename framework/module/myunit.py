import os
import unittest
import configparser as cparser
from selenium import webdriver
import framework.config_file as config
from framework.driver.web_driver import browser
from framework.driver import web_driver
import warnings

class MyTest(unittest.TestCase):


    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
        # driver = BrowserEngine(self)
        # self.base_url = "http://47.108.71.92"
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()

        # self.driver = webdriver.Chrome()
        # self.base_url = "http://47.108.71.92"

        self.driver = browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.base_url =config.url_c



    def tearDown(self):
        self.driver.quit()