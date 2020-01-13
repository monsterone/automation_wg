import os
import sys
import configparser as cparser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import framework.config_file as config
from framework.logger import Logger

logger=Logger(__name__).logger


#启动浏览器驱动
def browser():

    # =================webdriver===========================
    if config.browsers == 'Firefox':
        driver = webdriver.Firefox()
        logger.info("starting firefox browser")
    elif config.browsers == 'Chrome':
        driver = webdriver.Chrome()
        logger.info("starting Chrome browser")
    elif config.browsers == 'IE':
        driver = webdriver.Ie()
        logger.info("starting IE browser")
    elif config.browsers == 'Phantomjs':
        driver = webdriver.PhantomJS()
        logger.info("starting Phantomjs broeser")
    elif config.browsers == 'headless':
        # driver = webdriver.Chrome()
        # 设置浏览器无头模式
        option = webdriver.ChromeOptions()
        chrome_options = Options()
        option.add_argument('--headless')
        option.add_argument('--disable-gpu')
        # driver = webdriver.Chrome(chrome_options=option)
        driver = webdriver.Chrome(options=option)

    elif config.browsers == 'geckodriver':
        option = webdriver.FirefoxOptions()
        # options.set_headless(True)
        option.add_argument("--headless")  # 设置火狐为headless无界面模式
        option.add_argument("--disable-gpu")
        driver = webdriver.Firefox(options=option)
    else:
        driver = webdriver.Chrome()

    return driver


#调试运行
if __name__ == '__main__':
    browser()