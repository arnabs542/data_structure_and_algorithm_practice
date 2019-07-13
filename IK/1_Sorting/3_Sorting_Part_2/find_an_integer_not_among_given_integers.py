import os
import sys

'''
(This is a popular interview problem, from Programming Pearls)

Given an input file with four billion integers, provide an algorithm to generate an integer which is not contained in
the file. Assume you have 1 GiB memory. Follow up with what you would do if you have only 10 MiB of memory.

Till we finish developing this problem, you can look at:
http://stackoverflow.com/questions/7153659/find-an-integer-not-among-four-billion-given-ones?rq=1
'''

#
# Complete the find_an_integer_not_among_given_integers function below.
#
def find_an_integer_not_among_given_integers(nos):
    #
    # Write your code here.
    #
    pass

if __name__ == "__main__":
    fptr = sys.stdout

    nos_count = int(input())

    nos = []

    for _ in range(nos_count):
        nos_item = int(input())
        nos.append(nos_item)

    res = find_an_integer_not_among_given_integers(nos)

    fptr.write(str(res) + '\n')

    fptr.close()
