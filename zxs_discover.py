import unittest

suite = unittest.defaultTestLoader.discover("./")  # 遍历当前目录及子包中所有test_*.py中所有unittest用例
unittest.TextTestRunner(verbosity=2).run(suite)