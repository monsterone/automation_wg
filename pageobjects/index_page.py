from poium import Page,PageElement

class FirstIndexPage(Page):
    username_input = PageElement(xpath='/html/body/div/div/form/div[2]/div/div[1]/input')
    password_input = PageElement(xpath='/html/body/div/div/form/div[3]/div/div/input')
    login_button = PageElement(xpath='/html/body/div/div/form/div[4]/div/button')
    erro_hint_loc = PageElement(class_name='el-form-item__error')
    erro_hint_two = PageElement(xpath='/html/body/div[2]/p')


    user_logon = PageElement(css='.username')


