import os
from time import sleep
import unittest
from appium import webdriver
from time import sleep
import HTMLTestRunner
import time

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {
        'platformName' : 'Android',
        #'platformVersion' : '7.0',
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
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_login(self):
        el = self.driver.find_element_by_accessibility_id("loginName")
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
            print('检查是否存在首页的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Home']")
            print('登录成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '登录失败')

    def test_b_devices(self):
        print(111)
        sleep(5)
        el = self.driver.find_element_by_accessibility_id("loginName")
        el.send_keys('LarryChen')
        el = self.driver.find_element_by_accessibility_id('password')
        el.send_keys('111111')
        el = self.driver.find_element_by_xpath("//android.widget.ImageView")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.TextView['Login']")
        el.click()
        sleep(5)
        #点击devices
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Devices']")
        el.click()
        sleep(2)
        print('跳转到设备页面')
        try:
            print('\n')
            print('检查是否存在设备页面的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='All Devices']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        #点击all devices
        sleep(5)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='All Devices']")
        el.click()
        sleep(2)
        #点击Recent View
        sleep(5)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Recent View']")
        el.click()
        sleep(2)






    def test_c_shipments(self):
        sleep(10)
        el = self.driver.find_element_by_accessibility_id("loginName")
        el.send_keys('LarryChen')
        el = self.driver.find_element_by_accessibility_id('password')
        el.send_keys('111111')
        el = self.driver.find_element_by_xpath("//android.widget.ImageView")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.TextView['Login']")
        el.click()
        sleep(5)
        #点击shipment
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Shipments']")
        el.click()
        sleep(2)
        print('跳转到运单页面')
        try:
            print('\n')
            print('检查是否存在运单页面的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        #点击Completed Shipments
        sleep(5)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']")
        el.click()
        sleep(2)
        try:
            print('\n')
            print('根据运单状态检查是否存在已完成运单页面的元素')
            self.driver.find_element_by_xpath(
                "//android.widget.TextView[@text='Completed'or @text='Cancelled'or @text='No More Data，long press to follow']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        #点击Active Shipments
        sleep(5)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Active Shipments']")
        el.click()
        sleep(2)
        try:
            print('\n')
            print('根据运单状态检查是否存在活动运单页面的元素')
            self.driver.find_element_by_xpath(
                "//android.widget.TextView[@text='Active'or @text='Overdue'or @text='No More Data，long press to follow']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')

    def test_d_my(self):
        sleep(10)
        el = self.driver.find_element_by_accessibility_id("loginName")
        el.send_keys('LarryChen')
        el = self.driver.find_element_by_accessibility_id('password')
        el.send_keys('111111')
        el = self.driver.find_element_by_xpath("//android.widget.ImageView")
        el.click()
        el = self.driver.find_element_by_xpath("//android.widget.TextView['Login']")
        el.click()
        sleep(5)
        # 点击My
        sleep(5)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='My']")
        el.click()
        sleep(2)
        print('跳转到我的页面')
        try:
            print('\n')
            print('检查是否存在我的页面的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Version']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        #点击Logout
        sleep(5)
        el = self.driver.find_element_by_xpath("//android.widget.TextView[@text='Logout']")
        el.click()
        sleep(1)
        el = self.driver.find_element_by_id("android:id/button1")
        el.click()
        sleep(1)
        print('登出')
        try:
            print('\n')
            print('检查是否存在登录页面的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Login']")
            print('登出成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '登出失败')














if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    ''''# unittest.main()
    suite = unittest.TestSuite()
    # suite.addTest(Test('setUp'))  # 需要测试的用例就addTest，不加的就不会运行
    suite.addTest(SimpleAndroidTests('test_a_login'))
    suite.addTest(SimpleAndroidTests('test_b_devices'))
    suite.addTest(SimpleAndroidTests('test_c_shipments'))
    suite.addTest(SimpleAndroidTests('test_d_my'))


    # unittest.TextTestRunner(verbosity=1).run(suite)
    timestr = time.strftime('%Y-%m-%M-%H_%M_%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'C://Users/Administrator/Desktop/result/' + timestr + '.html' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()'''