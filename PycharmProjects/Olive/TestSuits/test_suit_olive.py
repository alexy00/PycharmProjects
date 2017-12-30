import unittest
from Product_Line.test_product_links import Product
from Contact.test_contact import ContactUS


# get all tests from TestClass1 and TestClass2 ^^^

tc1 = unittest.TestLoader().loadTestsFromTestCase(Product)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ContactUS)

# create a test suite combining TestClass1 and TestClass2
smoke_test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)