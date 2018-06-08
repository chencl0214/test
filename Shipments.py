import os
import unittest
from appium import webdriver
from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Shipments(unittest.TestCase):
    def setUp(self):
        desired_caps = {
        'platformName' : 'Android',
        'platformVersion' : '6.0',
        'automationName' : 'UIAutomator2',
        #实机
        #'deviceName' : 'A5RNW18119014503',
        #虚拟机
        'deviceName' : '192.168.96.102:5555',
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
    def test_a_Shipments(self):
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
        sleep(5)
        #点击Shipments
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Shipments']")
        el.click()
        sleep(2)
        print('\n')
        print('跳转到运单页面')
        try:
            print('\n')
            print('检查是否存在运单页面的元素')
            sel.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
    def test_b_CompletedShipments(self):
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
        # 点击Shipments
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Shipments']")
        el.click()
        sleep(2)
        print('\n')
        print('跳转到运单页面')
        try:
            print('\n')
            print('检查是否存在运单页面的元素')
            sel.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        #点击Completed Shipments
        sleep(5)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']")
        el.click()
        sleep(2)
        try:
            print('\n')
            print('根据运单状态检查是否存在已完成运单页面的元素')
            sel.find_element_by_xpath(
                "//android.widget.TextView[@text='Completed'or @text='Cancelled'or @text='No More Data，long press to follow']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
    def test_c_ActiveShipments(self):
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
        # 点击Shipments
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Shipments']")
        el.click()
        sleep(2)
        print('\n')
        print('跳转到运单页面')
        try:
            print('\n')
            print('检查是否存在运单页面的元素')
            sel.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        # 点击Completed Shipments
        sleep(5)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']")
        el.click()
        sleep(2)
        try:
            print('\n')
            print('根据运单状态检查是否存在已完成运单页面的元素')
            sel.find_element_by_xpath(
                "//android.widget.TextView[@text='Completed'or @text='Cancelled'or @text='No More Data，long press to follow']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        #点击Active Shipments
        sleep(5)
        el = sel.find_element_by_xpath("//android.widget.TextView[@text='Active Shipments']")
        el.click()
        sleep(2)
        try:
            print('\n')
            print('根据运单状态检查是否存在活动运单页面的元素')
            sel.find_element_by_xpath(
                "//android.widget.TextView[@text='Active'or @text='Overdue'or @text='No More Data，long press to follow']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')




if __name__ == '__main__':
    testunit = unittest.TestLoader().loadTestsFromTestCase(Shipments)
    unittest.TextTestRunner(verbosity=2).run(testunit)
    #unittest.main()