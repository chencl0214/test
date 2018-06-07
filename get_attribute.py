# coding:utf-8
from appium import webdriver

desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:62001',
                'platformVersion': '4.4.2',
                'appPackage': 'com.baidu.yuedu',
                'appActivity': 'com.baidu.yuedu.splash.SplashActivity',
                'noReset': 'true',
                'resetKeyboard': 'true',
                'unicodeKeyboard': 'true'
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 等主页面activity出现
driver.wait_activity(".base.ui.MainActivity", 10)

# 点取消升级
driver.find_element_by_id("com.baidu.yuedu:id/negativeUpgrade").click()

# 获取text
t1 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").text
print(t1)

# 获取tag_name
t2 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").tag_name
print(t2)

# content-desc为空，获取的是text
t3 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").get_attribute("name")
print(t3)

# content-desc
t4 = driver.find_element_by_id("com.baidu.yuedu:id/fragment_banner").get_attribute("name")
print (t4)

# id
t5 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").get_attribute("resourceId")
print(t5)

# class
t6 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").get_attribute("className")
print(t6)

# text
t7 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").get_attribute("text")
print(t7)

# checkable
t8 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").get_attribute("checkable")
print (t8)

# clickable
t9 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").get_attribute("clickable")
print (t9)

# size
t10 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").size
print (t10)

# location
t11 = driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").location
print (t11)