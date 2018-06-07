#coding=utf-8
import unittest
#加载模块
import time
import HTMLTestRunner

import Home
import ChangeClient
import CheckSearch
import Devices
import Shipments
import My
import Follow


print('\n')
print('生成报告...')
testunit = unittest.TestSuite()
#将测试用例加入到测试容器中
#testunit.addTest(unittest.makeSuite(pyfile.classname))
#检查登录到首页
testunit.addTest(unittest.makeSuite(Home.Home))
#检查切换客户
testunit.addTest(unittest.makeSuite(ChangeClient.ChangeClient))
#检查搜索
testunit.addTest(unittest.makeSuite(CheckSearch.CheckSearch))
#检查设备页面
testunit.addTest(unittest.makeSuite(Devices.Devices))
#检查运单页面
testunit.addTest(unittest.makeSuite(Shipments.Shipments))
#检查我的页面
testunit.addTest(unittest.makeSuite(My.My))
#检查关注
testunit.addTest(unittest.makeSuite(Follow.Follow))


#runner=unittest.TextTestRunner()
#runner.run(testunit)
#unittest.TextTestRunner(verbosity=2).run(testunit)
#导入当前时间，使用time模块的相关函数
now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
filename = 'C://Users/Administrator/Desktop/result/'+now+'.html'#这个路径改成自己的目录路径
#将测试结果写入到result.html中
fp=open(now+"result.html",'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description='Result:')
#rnnner=unittest.TextTestRunner(verbosity=2)
runner.run(testunit)
fp.close()
#####