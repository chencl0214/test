import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Devices(unittest.TestCase):
    def setUp(self):
        desired_caps = {
        'platformName' : 'Android',
        'platformVersion' : '7.0',
        'automationName' : 'UIAutomator2',
        #实机
        'deviceName' : 'A5RNW18119014503',
        #虚拟机
        #'deviceName' : '192.168.96.102:5555',
        # 'app': PATH(
        #    '../../../sample-code/apps/ContactManager/.apk'
        # ),
        'appPackage' : 'com.zillionsource.luiapp',
        'appActivity' : '.MainActivity',
        'unicodeKeyboard': True,  # 使用unicodeKeyboard的编码方式来发送字符串 ,可以实现输入中文
        'resetKeyboard': True  # 隐藏虚拟键盘，防止遮挡元素
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_a_Devices(self):
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
        #点击Devices
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Devices']")
        el.click()
        sleep(2)
        print('跳转到设备页面')
        try:
            print('\n')
            print('检查是否存在设备页面的元素')
            sel.find_element_by_xpath("//android.widget.TextView[@text='All Devices']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
    def test_b_AllDevices(self):
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
        # 点击Devices
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Devices']")
        el.click()
        sleep(2)
        print('跳转到设备页面')
        try:
            print('\n')
            print('检查是否存在设备页面的元素')
            sel.find_element_by_xpath("//android.widget.TextView[@text='All Devices']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        #点击All Devices
        sleep(5)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='All Devices']")
        el.click()
        sleep(2)





    def test_c_RecentView(self):
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
        sleep(5)
        # 点击Devices
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Devices']")
        el.click()
        sleep(2)
        print('跳转到设备页面')
        try:
            print('\n')
            print('检查是否存在设备页面的元素')
            sel.find_element_by_xpath("//android.widget.TextView[@text='All Devices']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        # 点击All Devices
        sleep(5)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='All Devices']")
        el.click()
        sleep(2)
        #点击Recent View
        sleep(5)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Recent View']")
        el.click()
        sleep(2)











if __name__ == '__main__':
    testunit = unittest.TestLoader().loadTestsFromTestCase(Devices)
    unittest.TextTestRunner(verbosity=2).run(testunit)
    #unittest.main()