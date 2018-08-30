import unittest

# Find the nth number of the fibonacci series

# Naive recursive solution

def nth_fibonacci(n):
    if n < 1:
        raise AssertionError
    if n in [1, 2]:
        return 1
    else:
        return nth_fibonacci(n-1) + nth_fibonacci(n-2)



class FibonacciTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(nth_fibonacci(1), 1)
        print("Passed ")

    def test_two(self):
        self.assertEqual(nth_fibonacci(2), 1)
        print("Passed")

    def test_ten(self):
        self.assertEqual(nth_fibonacci(1), 1)
        print("Passed")

test_nth_fibonacci = FibonacciTest()
test_nth_fibonacci.test_one()
test_nth_fibonacci.test_two()
test_nth_fibonacci.test_ten()

