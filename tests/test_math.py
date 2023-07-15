import unittest
from src.mymath import *

class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setup class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class')
    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    def test1_add(self):
        r = add(10, 20)
        self.assertEqual(r, 30, 'add testing')

    # @unittest.skip('no reason')
    def test_add(self):
        r = add(1, 2)
        self.assertEqual(3, r)

    def test_multiply(self):
        r = multiply(1, 2)
        self.assertEqual(3, r)

if __name__ == '__main__':
    unittest.main()