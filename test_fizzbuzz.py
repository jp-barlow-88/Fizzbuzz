import fizz_buzz
import unittest


class Test(unittest.TestCase):

    def test_nums(self):
        self.assertEqual(fizz_buzz.fizz(1), 1)
        self.assertEqual(fizz_buzz.fizz(4), 4)

    def test_whizz(self):
        self.assertEqual(fizz_buzz.fizz(2), 'Whizz')

    def test_fizzwhizz(self):
        self.assertEqual(fizz_buzz.fizz(3), 'FizzWhizz')

    def test_buzzwhizz(self):
        self.assertEqual(fizz_buzz.fizz(5), 'BuzzWhizz')

    def test_fizz(self):
        self.assertEqual(fizz_buzz.fizz(6), 'Fizz')
        self.assertEqual(fizz_buzz.fizz(9), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizz_buzz.fizz(10), 'Buzz')
        self.assertEqual(fizz_buzz.fizz(20), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizz_buzz.fizz(15), 'FizzBuzz')
        self.assertEqual(fizz_buzz.fizz(30), 'FizzBuzz')
        self.assertEqual(fizz_buzz.fizz(75), 'FizzBuzz')


if __name__ == '__main__':
    unittest.main()
