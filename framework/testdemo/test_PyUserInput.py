from pymouse import PyMouse
from pykeyboard import PyKeyboard


pym = PyMouse()
pyk = PyKeyboard()

#点击功能键F5
# pyk.tap_key(pyk.function_keys[5])
#点击小键盘5,6次
# pyk.tap_key(pyk.numpad_keys[5],6)
#点击回车键
pyk.tap_key(pyk.enter_key)
#联合按键模拟
#同时按alt+tab键盘
# pyk.press_key(pyk.alt_key)#按住alt键
# pyk.tap_key(pyk.tab_key)#点击tab键
# pyk.release_key(pyk.alt_key)#松开alt键


