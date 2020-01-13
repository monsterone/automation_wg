import configparser
import os.path
from selenium import webdriver

from framework.logger import Logger

logger = Logger(logger='BrowserEngine').getlog()


class BrowserEngine(object):

    dir = os.path.dirname(os.path.abspath('.'))  # 注意相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    """
	定义一个浏览器引擎，根据browser_type的值去，控制启动不同的浏览器，这里主要是IE,FireFoc,Chrome
	"""

    def __init__(self, driver):

        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self):

        config = configparser.ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = os.path.dirname(
            os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        # config.read(file_path,encoding='UTF-8') #如果代码有中文注释，用这个，不然报解码错误

        self.browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % self.browser)
        self.url = config.get("testServer", "URL")
        # print(url)
        logger.info("The test server url is: %s" % self.url)

        if self.browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info("starting firefox browser")
        elif self.browser == 'Chrome':
            driver = webdriver.Chrome()
            logger.info("starting Chrome browser")
        elif self.browser == 'IE':
            driver = webdriver.Ie()
            logger.info("starting IE browser")
        else:
            driver = webdriver.Chrome()

        driver.get(self.url)
        logger.info("Open url: %s" % self.url)
        driver.maximize_window()
        logger.info("Maxmze the current window.")
        driver.implicitly_wait(10)
        logger.info("set implictly wait 10 seconds")
        return driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()


if __name__ == '__main__':
    test = BrowserEngine(driver=webdriver.Firefox())
    test.open_browser()
