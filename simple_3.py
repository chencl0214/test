import os
import unittest
from appium import webdriver
from time import sleep
import HTMLTestRunner
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {
        #'platformName' : 'Android',
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























if __name__=="__main__":
    unittest.main()