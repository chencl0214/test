import os
import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class CheckSearch(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'automationName': 'UIAutomator2',
            # 实机
            #'deviceName' : 'A5RNW18119014503',
            # 虚拟机
            'deviceName': '192.168.96.102:5555',
            # 'app': PATH(
            #    '../../../sample-code/apps/ContactManager/.apk'
            # ),
            'appPackage': 'com.zillionsource.luiapp',
            'appActivity': '.MainActivity',
            'unicodeKeyboard': True,  # 使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
            'resetKeyboard': True  # 隐藏虚拟键盘，防止遮挡元素
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()
    def test_a_CheckShipmentsSearch(self):
        sleep(10)
        el = self.driver.find_element_by_accessibility_id('loginName')
        el.send_keys('LarryChen')
        el = self.driver.find_element_by_accessibility_id('password')
        el.send_keys('111111')

        el = self.driver.find_element_by_xpath("//android.widget.ImageView")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.TextView['Login']")
        el.click()
        sleep(10)
        try:
            print('\n')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Home']")
            print('登录成功')
        except:
            self.assertIsNone(not None, '登录失败')
        el = self.driver.find_element_by_xpath("//android.widget.TextView[1]")
        el.click()
        sleep(2)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='*DevTest*']")
        el.click()
        sleep(2)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[2]")
        el.click()
        sleep(2)
        el = self.driver.find_element_by_xpath("//android.widget.EditText")
        el.click()
        el.send_keys('lar')
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Shipments']")
        el.click()
        sleep(2)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Search:Shipments']")
        el.click()
        sleep(5)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Larytest_do_not_del']")
        el.click()
        sleep(10)
        try:
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Larytest_do_not_del']")
            print('正确找到该运单')
        except:
            self.assertIsNone(not None, '找错运单或没找到')
    def test_b_CheckDevicesSearch(self):
        sel = self.driver
        sleep(10)
        el = sel.find_element_by_accessibility_id("loginName")
        el.send_keys('LarryChen')
        el = sel.find_element_by_accessibility_id('password')
        el.send_keys('111111')

        el = sel.find_element_by_xpath("//android.widget.ImageView")
        el.click()
        el = sel.find_element_by_xpath("//android.widget.TextView['Login']")
        el.click()
        sleep(10)
        try:
            print('\n')
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
        el = sel.find_element_by_xpath("//android.widget.TextView[2]")
        el.click()
        sleep(2)
        el = sel.find_element_by_xpath("//android.widget.EditText")
        el.click()
        el.send_keys('537')
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Devices']")
        el.click()
        sleep(2)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Search:Devices']")
        el.click()
        sleep(5)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='ZS100-010204537']")
        el.click()
        sleep(10)
        try:
            sel.find_element_by_xpath("//android.widget.TextView[@text='ZS100-010204537']")
            print('正确找到该设备')
        except:
            self.assertIsNone(not None, '找错设备或没找到')








if __name__ == '__main__':
    testunit = unittest.TestLoader().loadTestsFromTestCase(CheckSearch)
    unittest.TextTestRunner(verbosity=2).run(testunit)
    #unittest.main()
