
from poium import Page,PageElement

class LoginIndexPage(Page):
    username_input = PageElement(xpath='/html/body/div/div/form/div[2]/div/div[1]/input')
    password_input = PageElement(xpath='/html/body/div/div/form/div[3]/div/div/input')
    login_button = PageElement(xpath='/html/body/div/div/form/div[4]/div/button')
    erro_hint_loc = PageElement(class_name='el-form-item__error')
    erro_hint_two = PageElement(xpath='/html/body/div[2]/p')

    # page.username_input.send_keys("")
    # page.password_input.send_keys("11")
    # page.login_button.click()
    #登录
    def login_action(self,username,password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    ##登录失败（断言）
    def type_loginFail_hint1(self):
        return self.erro_hint_loc.text

    ##登录失败（断言）
    def type_loginFail_hint2(self):
        return self.erro_hint_two.text