from datetime import datetime, timedelta
import unittest
# Given two strings find the longest common subsequence between the two.
# A subsequence does not have to be consecutive.
# Example longest_common_subsequence("abcdaf", "acbcf") would return 4
# The subsequence would be "abcf" common among both input strings.

def longest_common_subsequence_old(string_one, string_two):
    # build an empty 2D array of size [string_one] * [string_two]
    two_d_array = [[0] * len(string_two) for i in range(len(string_one))]

    longest = 0
    for row in range(len(string_one)):
        for col in range(len(string_two)):
            if string_one[row] == string_two[col]:
                current_longest = 0
                if row-1 >= 0 and col-1 >= 0:
                    current_longest = two_d_array[row-1][col-1]
                two_d_array[row][col] = current_longest + 1
                if current_longest + 1 > longest:
                    longest = current_longest + 1
            else:
                try:
                    cur_row_max = two_d_array[row-1][col]
                except IndexError:
                    cur_row_max = 0
                try:
                    cur_col_max = two_d_array[row][col-1]
                except IndexError:
                    cur_col_max = 0
                two_d_array[row][col] = max(cur_row_max, cur_col_max)
    print(longest)

def longest_common_subsequence(string_one, string_two):
    # build an empty 2D array of size [string_one] * [string_two]
    two_d_array = [[0] * (len(string_two)+1) for i in range(len(string_one) + 1)]

    longest = float('-inf')
    for row in range(len(string_one)):
        for col in range(len(string_two)):
            if string_one[row] == string_two[col]:
                two_d_array[row][col] = two_d_array[row-1][col-1] + 1
                if two_d_array[row][col] > longest:
                    longest = two_d_array[row][col]
            else:
                two_d_array[row][col] = max(two_d_array[row-1][col], two_d_array[row][col-1])
    return longest


class LCS_Test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(longest_common_subsequence("abcdaf", "acbcf"), 4)
        print("Passed ")
        self.assertEqual(longest_common_subsequence("abcdefgizzzzaj", "abcdefghiabcdefgh"), 9)
        print("Passed ")
        self.assertEqual(longest_common_subsequence("ABCDGH", "AEDFHR"), 3)
        print("Passed ")
        self.assertEqual(longest_common_subsequence("AGGTAB", "GXTXAYB"), 4)
        print("Passed ")
        self.assertEqual(longest_common_subsequence("acbaed", "abcadf"), 4)
        print("Passed ")
        self.assertEqual(longest_common_subsequence("classical", "musical"), 5)
        print("Passed ")
        self.assertEqual(longest_common_subsequence("12341", "341213"), 3)
        print("Passed ")

    def test_timed(self):
        start_time = datetime.now()
        longest_common_subsequence("abcdefgizzzzaj", "abcdefghiabcdefgh")
        print("LCS time = " + str(datetime.now() - start_time))

tests = LCS_Test()
tests.test_one()
tests.test_timed()
