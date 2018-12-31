from unittest import TestCase, main
from single_package.single import Single


class SingleTests(TestCase):

    def setUp(self):
        self.single = Single()

    def test_Single(self):
        self.assertIsInstance(self.single, Single)


if __name__ == "__main__":
    main()
