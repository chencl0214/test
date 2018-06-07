#coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep
import HTMLTestRunner
import time
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Test(unittest.TestCase):
    # setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。

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

    def test1(self):
        print('1')

    def test2(self):
        print('2')
        #print('链接Appium')
    sleep(5)
        #self.verificationErrors = "Appium未启动"  # 设置的断言
    # tearDown 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出

    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()
        print('关闭程序')

    def Login(self):
        sleep(5)
        self.driver.find_element_by_accessibility_id("loginName").send_keys('LarryChen')
        self.driver.find_element_by_accessibility_id("password").send_keys('111111')
        self.driver.find_element_by_xpath("//android.widget.ImageView").click()
        self.driver.find_element_by_xpath("//android.widget.TextView['Login']").click()
        # 等待10秒
        sleep(10)
        #判断是否登录到首页
        #self.assertIsNotNone(self.driver.find_element_by_xpath("//android.widget.TextView[@text='Followed Devices']"),'无followed,登录失败,Fail')

        #def (self):
        print('\n')
        print('登录检查')
        #pass_1 = False
        try:
            print('检查是否存在首页的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Home']")
            print('登录成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '登录失败')


        # 点击Devices
    #def DevicePageCheck(self):
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Devices']").click()
        sleep(2)
        print('跳转到设备页面')
        try:
            print('检查是否存在设备页面的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='All Devices']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        # 点击All Devices
    #def AllDevicePageCheck(self):
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='All Devices']").click()
        sleep(2)
        # 点击Recent View
    #def RecentViewCheck(self):
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Recent View']").click()
        sleep(2)

        # 点击Shipment
    #def ShipmentPageCheck(self):
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Shipments']").click()
        sleep(2)
        print('跳转到运单页面')
        try:
            print('检查是否存在运单页面的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')

        # 点击Completed Shipments
    #def CompletedShipmentsCheck(self):
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Completed Shipments']").click()
        sleep(10)
        # 获取屏幕的高
        x = self.driver.get_window_size()['width']
        # 获取屏幕宽
        y = self.driver.get_window_size()['height']
        # 打印屏幕高和宽
        print(self.driver.get_window_size())

        # 向上滑
        self.driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)
        # count=0
        '''while True:
            # self.assertIsNot(self.driver.find_element_by_xpath("//android.widget.TextView[@text='No More Data,long press to follow']"))):
            #self.driver.swipe(1 / 2 * x, 1 / 2 * y, 1 / 2 * x, 1 / 7 * y, 200)
            sleep(3)
            # count=count+1
            # self.assertIsNot(self.driver.find_element_by_xpath("//android.widget.TextView[@text='No More Data,long press to follow']"))
            if self.driver.find_element_by_xpath(
                    "//android.widget.TextView[@text='No More Data,long press to follow']"):
                print(self.driver.find_element_by_xpath(
                    "//android.widget.TextView[@text='No More Data,long press to follow']"))
                break'''

        try:
            print('根据运单状态检查是否存在已完成运单页面的元素')
            self.driver.find_element_by_xpath(
                "//android.widget.TextView[@text='Completed'or @text='Cancelled'or @text='No More Data，long press to follow']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        # 点击Active Shipments
    #def ActiveShipmentsCheck(self):
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Active Shipments']").click()
        sleep(2)
        try:
            print('根据运单状态检查是否存在活动运单页面的元素')
            self.driver.find_element_by_xpath(
                "//android.widget.TextView[@text='Active'or @text='Overdue'or @text='No More Data，long press to follow']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        # 点击My
    #def MyCheck(self):
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='My']").click()
        sleep(2)
        print('跳转到我的页面')
        try:
            print('检查是否存在我的页面的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Version']")
            print('跳转成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '跳转失败')
        # 点击Logout
    #def LogoutCheck(self):
        sleep(5)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Logout']").click()
        sleep(1)
        self.driver.find_element_by_id("android:id/button1").click()
        sleep(1)
        print('登出')
        try:
            print('检查是否存在登录页面的元素')
            self.driver.find_element_by_xpath("//android.widget.TextView[@text='Login']")
            print('登出成功')
        except:
            print('找不到元素')
            self.assertIsNone(not None, '登出失败')

        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='']").click()

        # 扫码允许点击allow
        # self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    #suite.addTest(Test('setUp'))  # 需要测试的用例就addTest，不加的就不会运行
    suite.addTest(Test('test1'))
    suite.addTest(Test('test2'))
    '''suite.addTest(Test('DevicePageCheck'))
    suite.addTest(Test('AllDevicePageCheck'))
    suite.addTest(Test('RecentViewCheck'))
    suite.addTest(Test('ShipmentPageCheck'))
    suite.addTest(Test('CompletedShipmentsCheck'))
    suite.addTest(Test('ActiveShipmentsCheck'))
    suite.addTest(Test('MyCheck'))
    suite.addTest(Test('LogoutCheck'))'''

    # unittest.TextTestRunner(verbosity=1).run(suite)
    timestr = time.strftime('%Y-%m-%M-%H_%M_%S', time.localtime(time.time()))  # 本地日期时间作为测试报告的名字
    filename = 'C://Users/Administrator/Desktop/result/'+timestr+'.html' + timestr + '.html'  # 这个路径改成自己的目录路径
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()
