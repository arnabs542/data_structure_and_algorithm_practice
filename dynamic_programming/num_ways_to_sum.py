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

def num_ways_to_sum_DP_bottom_up(n, numbers):
    memo = dict()

    for count in range(n+1):
        for num in numbers:
            if count - num in memo:
                if count in memo:
                    memo[count] += memo[count-num]
                else:
                    memo[count] = memo[count-num]
            elif count - num == 0:
                if count in memo:
                    memo[count] += 1
                else:
                    memo[count] = 1

    return memo[n]


class SumTest(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(num_ways_to_sum(5,[1,3,4]), 6)
        self.assertEqual(num_ways_to_sum_DP_top_down(5,[1,3,4]), 6)
        self.assertEqual(num_ways_to_sum_DP_bottom_up(5,[1,3,4]), 6)
        print("Passed")

    def test_example_two(self):
        self.assertEqual(num_ways_to_sum(10,[1,3,4]), 64)
        self.assertEqual(num_ways_to_sum_DP_top_down(10,[1,3,4]), 64)
        self.assertEqual(num_ways_to_sum_DP_bottom_up(10,[1,3,4]), 64)
        print("Passed")

    def test_example_three(self):
        self.assertEqual(num_ways_to_sum(20,[1,3,4]), 7921)
        self.assertEqual(num_ways_to_sum_DP_top_down(20,[1,3,4]), 7921)
        self.assertEqual(num_ways_to_sum_DP_bottom_up(20,[1,3,4]), 7921)
        print("Passed")

    def test_sum_times(self):
        start_time = datetime.now()
        num_ways_to_sum(33,[1,3,4])
        print("Brute force number of ways to sum = " + str(datetime.now() - start_time))

        start_time = datetime.now()
        num_ways_to_sum_DP_top_down(33,[1,3,4])
        print("Brute force number of ways to sum w/DP top down = " + str(datetime.now() - start_time))

        start_time = datetime.now()
        num_ways_to_sum_DP_bottom_up(33,[1,3,4])
        print("Brute force number of ways to sum w/DP bottom up = " + str(datetime.now() - start_time))

test_sums = SumTest()
test_sums.test_example_one()
test_sums.test_example_two()
test_sums.test_example_three()
test_sums.test_sum_times()

