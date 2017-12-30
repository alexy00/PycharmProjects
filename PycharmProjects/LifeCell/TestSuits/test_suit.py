import unittest

from Shop.All_In_One.test_payments import AllInOnePage

from Shop.test_links import ProductLinks

# initialize the test suite

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ProductLinks))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AllInOnePage))

# initialize a runner, pass it to your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
