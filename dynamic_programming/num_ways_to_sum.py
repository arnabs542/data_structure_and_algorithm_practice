from datetime import datetime, timedelta
import unittest

def num_ways_to_sum(n, numbers):
    totals = 0
    for num in numbers:
        if n - num == 0:
            totals += 1
        elif n - num > 0:
            totals += num_ways_to_sum(n-num, numbers)
    return totals

def num_ways_to_sum_DP_top_down(n, numbers, memo=None):
    totals = 0

    if memo == None:
        memo = dict()

    if n in memo:
        return memo[n]

    for num in numbers:
        if n - num == 0:
            totals += 1
        elif n - num > 0:
            totals += num_ways_to_sum_DP_top_down(n-num, numbers, memo)
    memo[n] = totals
    return totals

class SumTest(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(num_ways_to_sum(5,[1,3,4]), 6)
        self.assertEqual(num_ways_to_sum_DP_top_down(5,[1,3,4]), 6)
        print("Passed")

    def test_sum_times(self):
        start_time = datetime.now()
        num_ways_to_sum(35,[1,3,4])
        print("Brute force number of ways to sum = " + str(datetime.now() - start_time))

        start_time = datetime.now()
        num_ways_to_sum_DP_top_down(35,[1,3,4])
        print("Brute force number of ways to sum w/DP top down = " + str(datetime.now() - start_time))

test_sums = SumTest()
test_sums.test_example_one()
test_sums.test_sum_times()
