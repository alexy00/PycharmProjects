import unittest
from My_Account.tests.test_login_frame import ContactTests
from Gloves.tests.test_gloves_frame import GlovesTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(ContactTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(GlovesTests)

regressionTest = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(regressionTest)



# py.test Testsuits\test_suite_frame.py









