#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")
from common import HTMLTestRunner

import  unittest
casePath = "E:\\YY_sh\\case"

discover = unittest.defaultTestLoader.discover(casePath,"test*.py")

# runner = unittest.TextTestRunner()
# runner.run(discover)

reportPath = "E:\\YY_sh\\report\\"+"1.html"

fp = open(reportPath, "wb" )

runner = HTMLTestRunner.HTMLTestRunner(fp,verbosity=2 , title="测试报告",
                              description="报告描述")


runner.run(discover)
fp.close()


# print(discover)