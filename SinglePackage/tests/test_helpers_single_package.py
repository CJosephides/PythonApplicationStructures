from unittest import TestCase, main
from single_package.helpers_single_package import Helper


class HelpersTests(TestCase):

    def setUp(self):
        self.helper = Helper()

    def test_Helper(self):
        self.assertIsInstance(self.helper, Helper)
