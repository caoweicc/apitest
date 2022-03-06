import unittest
from test_user_login import TestUserLogin

suite1 = unittest.makeSuite(TestUserLogin, 'test_user_login_normal') # 使用测试类的单条用例制作测试集
suite2 = unittest.makeSuite(TestUserLogin) # 使用整个测试类制作测试集合(包含该测试类所有用例)

unittest.TextTestRunner(verbosity=2).run(suite1)