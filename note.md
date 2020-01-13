##selenium问题：

* 1、忽略警告(Phantomjs浏览器)：
      需要在python里导入 import warnings。
       然后在下面加一行代码warnings.simplefilter(“ignore”, ResourceWarning)
https://blog.csdn.net/xiezhiming1234/article/details/82532815



* 2、解决selenium中无法点击Element：ElementClickInterceptedException

        selenium.common.exceptions.ElementClickInterceptedException: Message: 
        Element <a class=""> is not clickable at point 
        (318.3000030517578,661.7999877929688) because another element <div
        class=""> obscures it

        方法：
        element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
        driver.execute_script("arguments[0].click();", element)
 
        element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
        webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()


   https://blog.csdn.net/WanYu_Lss/article/details/84137519



* 3、warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
意思就是Selenuim已经放弃PhantomJS，了，建议使用火狐或者谷歌无界面浏览器。

 https://www.cnblogs.com/shaosks/p/9134257.html

* 谷歌 #设置浏览器无头模式


    chrome_options = Options()
     #Chrome-headless 模式， Google 针对 Chrome 浏览器 59版 新增加的一种模式，可以让你不打开UI界面的情况下使用 Chrome 浏览器，所以运行效果与 Chrome 保持完美一致。
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    self.driver = webdriver.Chrome(chrome_options=chrome_options)
     self.driver.set_page_load_timeout(10)
    self.driver.maximize_window()

注：不能打开浏览器

* FireFox设置无头

        option = webdriver.FirefoxOptions()
                # options.set_headless(True)
                option.add_argument("--headless")  # 设置火狐为headless无界面模式
                option.add_argument("--disable-gpu")
                driver = webdriver.Firefox(options=option)



* 4、  selenium svg标签定位元素

https://www.cnblogs.com/dengvv/p/10831473.html


# selenium_question

1.chrome 添加不可以选子设备，firefox可以（chrome修改都可以）

2.修改名称firefox不可以清空，Chrome可以
 见备注（公众号的双击和js demo操作）
 
        自己总结：
        ##用keys操作(firefox，chrome通用)
        self.driver_name_input.send_keys(Keys.CONTROL,'a')
        self.driver_name_input.send_keys(Keys.CONTROL,'x')

3.chrome不可以上传exe

    注意：上传控件名称不同（chrome和firefox的不同）
    

4.报错（使用无头浏览器报错）

selenium.common.exceptions.WebDriverException: Message: unknown error: Element <input type="text" readonly="readonly" autocomplete="off" placeholder="请选择所属类型" class="el-input__inner" style="border: 2px solid red;"> is not clickable at point (470, 216). Other element would receive the click: <i class="el-select__caret el-input__icon el-icon-arrow-up"></i>


https://blog.csdn.net/lyl_7310/article/details/78532628

使用：Key.Enter （键盘）



5.上传文件方式

https://www.cnblogs.com/xiaxiaoxu/p/9198019.html

https://www.bbsmax.com/A/6pdD9rmXzw/