import unittest

from Contact.tests.test_contact import ContactPage
from Header.tests.test_header import Header
from Programs.tests.test_programs import ProgramsPage
from Sidebar.tests.test_sidebar import Sidebar

header = unittest.TestLoader().loadTestsFromTestCase(Header)
programs = unittest.TestLoader().loadTestsFromTestCase(ProgramsPage)
sidebar = unittest.TestLoader().loadTestsFromTestCase(Sidebar)
contact = unittest.TestLoader().loadTestsFromTestCase(ContactPage)


rocha_test = unittest.TestSuite([header,programs,sidebar,contact])

unittest.TextTestRunner(verbosity=2).run(rocha_test)


# py.test -s -v Testsuits\test_suit.py
