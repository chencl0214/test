import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class ChangeClient(unittest.TestCase):
    def setUp(self):
        desired_caps = {
        'platformName' : 'Android',
        'platformVersion' : '7.0',
        'automationName' : 'UIAutomator2',
        #实机
        'deviceName' : 'A5RNW18119014503',
        #虚拟机
        #'deviceName' : '192.168.96.102:5555',
        #'app': PATH(
        #    '../../../sample-code/apps/ContactManager/.apk'
        #),
        'appPackage' : 'com.zillionsource.luiapp',
        'appActivity' : '.MainActivity',
        'unicodeKeyboard': True,  # 使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
        'resetKeyboard': True  # 隐藏虚拟键盘，防止遮挡元素
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()
    def test_a_ChangeClient(self):
        sel = self.driver
        sleep(10)
        el = sel.find_element_by_accessibility_id('loginName')
        el.send_keys('LarryChen')
        el = sel.find_element_by_accessibility_id('password')
        el.send_keys('111111')

        el = sel.find_element_by_xpath("//android.widget.ImageView")
        el.click()
        el = sel.find_element_by_xpath("//android.widget.TextView['Login']")
        el.click()
        sleep(10)
        try:
            sel.find_element_by_xpath("//android.widget.TextView[@text='Home']")
            print('登录成功')
        except:
            self.assertIsNone(not None, '登录失败')
        el = sel.find_element_by_xpath("//android.widget.TextView[1]")
        el.click()
        sleep(2)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='*DevTest*']")
        el.click()
        sleep(2)
        try:
            print('\n')
            sel.find_element_by_xpath("//android.widget.TextView[@text='*DevTest*']")
            print('切换成功')
        except:
            self.assertIsNone(not None, '切换失败')



if __name__ == '__main__':
    testunit = unittest.TestLoader().loadTestsFromTestCase(ChangeClient)
    unittest.TextTestRunner(verbosity=2).run(testunit)
    #unittest.main()
