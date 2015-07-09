# Run with 'python fizzbuzz_test.py' or 'python -m unittest discover -p '*_test.py'

import unittest
from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):
    """Any method which starts with `test_` will be considered as a test case."""

    def test_fizz(self):
        """It correctly returns the Fizz for number divisible by 3."""

        res = fizzbuzz(3)
        self.assertEqual(res, """Fizz""")    

    def test_buzz(self):
        """It correctly returns the Buzz for number divisible by 5."""

        res = fizzbuzz(5)
        self.assertEqual(res, """Buzz""")

    def test_fizzbuzz(self):
        """It correctly returns the Fizzbuzz for number divisible by 3 and 5."""

        res = fizzbuzz(15)
        self.assertEqual(res, """Fizzbuzz""")


if __name__ == '__main__':
    unittest.main()