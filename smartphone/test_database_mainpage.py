from unittest import TestCase
from database_mainpage import *


class Testlog(TestCase):
    def setUp(self):
        self.a=log()

    def test_log1(self):
        self.assertTrue(self)

    def test_log2(self):
        self.assertFalse(self)

    def test_log3(self):
        self.assertRaises(self)

    def test_log4(self):
        self.fail(self)

    def test_log5(self):
        self.assertTrue(self)


