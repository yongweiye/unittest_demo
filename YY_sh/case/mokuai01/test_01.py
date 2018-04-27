#coding=utf-8

import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")
import  time
import  unittest
class Test1(unittest.TestCase):

    u''' 测试用例集合;描述 xxx'''
    @classmethod
    def setUpClass(cls):
        print("setUpClass 初始化操作 ,用例开始执行前操作")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass初始化操作 ,用例开始执行前操作")


    def setUp(self):
        print("setUp(self) ,用例开始执行前操作")


    def test_01(self):
        time.sleep(1)
        print("test_01(self): running......")

    def test_02(self):
        time.sleep(1)
        print("test_02(self):running......")
    def tearDown(self):
        print("tearDown(self):running...... ")



if __name__ == '__main__':
    unittest.main()