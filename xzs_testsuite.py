import unittest
from test_user_login import TestUserLogin
from test_user_reg import TestUserReg # 从上面两个例子里导入测试类

suite = unittest.TestSuite()
suite.addTest(TestUserLogin('test_user_login_normal')) # 添加单个用例
suite.addTests([TestUserReg('test_user_reg_normal'),TestUserReg('test_user_reg_exist')]) # 添加多个用例

# 运行测试集
unittest.TextTestRunner(verbosity=2).run(suite)  # verbosity显示级别，运行顺序为添加到suite中的顺序