import unittest
from test_user_login import TestUserLogin

suite = unittest.TestLoader().loadTestsFromTestCase(TestUserLogin) # 加载该测试类所有用例并生成测试集

unittest.TextTestRunner(verbosity=2).run(suite)