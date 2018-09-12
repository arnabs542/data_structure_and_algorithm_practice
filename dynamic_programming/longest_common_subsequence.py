# Given two strings find the longest common subsequence between the two.
# A subsequence does not have to be consecutive.
# Example longest_common_subsequence("abcdaf", "acbcf") would return 4
# The subsequence would be "abcf" common among both input strings.

def longest_common_subsequence(string_one, string_two):
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

longest_common_subsequence("abcdaf", "acbcf")
longest_common_subsequence("abcdefgizzzzaj", "abcdefghiabcdefgh")

