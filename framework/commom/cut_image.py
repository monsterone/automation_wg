




import os

#截图方法
class Image():

    def inser_img(driver,filename):

        #获取当前模块所在路径
        func_path=os.path.dirname(__file__)
        # print("func_path is %s" %func_path)

        #获取test_case目录
        # base_dir=os.path.dirname(func_path)
        base_dir=os.path.dirname(os.path.dirname(func_path))
       # print("base_dir is %s" %base_dir)

        #将路径转化为字符串
        base_dir=str(base_dir)

        #对路径的字符串进行替换
        base_dir=base_dir.replace('\\','/')
        # print(base_dir)


        #获取项目文件的根目录路径
        # base=base_dir.split('/Website')[0]
        # print(base)

        #指定截图存放路径
        filepath=base_dir+'/report/Screenshots/'+filename
        # print(filepath)
        driver.get_screenshot_as_file(filepath)
