from datetime import datetime, timedelta
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

def nth_fibonacci_DP_top_down(n, memo=None):
    if n < 1:
        raise AssertionError

    if n in [1, 2]:
        return 1

    if memo == None:
        memo = dict()

    if n in memo:
        return memo[n]

    key = nth_fibonacci_DP_top_down(n-1, memo) + nth_fibonacci_DP_top_down(n-2, memo)
    memo[n] = key
    return key

def nth_fibonacci_DP_bottom_up(n):
    
    num1 = 1
    num2 = 1
    
    for _ in range(n-2):
        nth_num = num1+num2
        num1 = num2
        num2 = nth_num

    return num2

class FibonacciTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(nth_fibonacci(1), 1)
        self.assertEqual(nth_fibonacci_DP_top_down(1), 1)
        self.assertEqual(nth_fibonacci_DP_bottom_up(1), 1)
        print("Passed ")

    def test_two(self):
        self.assertEqual(nth_fibonacci(2), 1)
        self.assertEqual(nth_fibonacci_DP_top_down(2), 1)
        self.assertEqual(nth_fibonacci_DP_bottom_up(2), 1)
        print("Passed")

    def test_ten(self):
        self.assertEqual(nth_fibonacci(10), 55)
        self.assertEqual(nth_fibonacci_DP_top_down(10), 55)
        self.assertEqual(nth_fibonacci_DP_bottom_up(10), 55)
        print("Passed")

    def test_fibonacci_times(self):
        start_time = datetime.now()
        nth_fibonacci(33)
        print("Brute force nth_fibonacci = " + str(datetime.now() - start_time))

        start_time = datetime.now()
        nth_fibonacci_DP_top_down(33)
        print("nth_fibonacci_DP_top_down = " + str(datetime.now() - start_time))

        start_time = datetime.now()
        nth_fibonacci_DP_bottom_up(33)
        print("nth_fibonacci_DP_bottom_up= " + str(datetime.now() - start_time))


test_nth_fibonacci = FibonacciTest()
test_nth_fibonacci.test_one()
test_nth_fibonacci.test_two()
test_nth_fibonacci.test_ten()
test_nth_fibonacci.test_fibonacci_times()
