import os
import configparser as cparser
from framework.logger import Logger


# ===============读取email_config.ini文件设置============

logger=Logger(__name__).logger
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
# base_dir = base_dir.replace('\\','/') #多余本身/
file_path = base_dir + "/config/config.ini"
cf = cparser.ConfigParser()
cf.read(file_path, encoding='utf-8')
browsers = cf.get("browserType", "browserName")
logger.info("You had select %s browser." % browsers)
url_c = cf.get("testServer", "URL")
logger.info("The test server url is: %s" % url_c)