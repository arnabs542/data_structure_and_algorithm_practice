'''
Find Order Of Characters From Alien Dictionary
Problem Statement:
Given a sorted dictionary of an alien language, you have to find the order of characters in that language.
(This is a popular interview problem.)
Generally, dictionary does not contain duplicate values, but for the sake of this problem, assume that dictionary might
 have duplicate values. (Sometimes interviewer tricks the question, to see, how you will handle it.)
Input/Output Format For The Function:
Input Format:
There is only one argument, array of strings words, which denotes sorted dictionary of an alien language.
Output Format:
Return a string ordered, denoting order of characters in the alien language.
Length of the output string will be the number of different characters present in input dictionary.
For more clarity see the sample test cases.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting size of input array words. In next n lines, ith line should
 contain a string words[i], denoting a value at index i of words.
If n = 5 and words = ["baa", "abcd", "abca", "cab", "cad"], then input should be:
5
baa
abcd
abca
cab
cad
Output Format:
There will be only one line of output, containing a string ordered, denoting the result returned by solution function.
For input n = 5 and words = ["baa", "abcd", "abca", "cab", "cad"], output will be:
bdac
Constraints:
1 <= total number of characters in dictionary (not words) <= 10^5
Character in any word will be lower case alphabet letter.

Input will be such that it is possible to determine the order uniquely.
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
words = ["baa", "abcd", "abca", "cab", "cad"]
Sample Output 1:
"bdac"
Sample Test Case 2:
Sample Input 2:
words = ["caa", "aaa", "aab"]
Sample Output 2:
"cab"
Notes:
Maximum time allowed in interview: 20 Minutes.
Here input is given such that it is possible to determine order uniquely. But in interview you should clarify these things
 with interviewer. Like if we are given words = ["z" "bc"] then we can only conclude that 'z' will come before 'b', but
 nothing about the order of 'c'!
'''

import sys
import os

def find_order(words):
    pass

if __name__ == "__main__":
    f = sys.stdout

    words_cnt = 0
    words_cnt = int(input())
    words_i = 0
    words = []
    while words_i < words_cnt:
        try:
            words_item = str(input())
        except:
            words_item = None
        words.append(words_item)
        words_i += 1


    res = find_order(words);
    f.write(res + "\n")


    f.close()


'''
Simple but non-optimal solution is: 
Collect all unique characters. Generate all permutations of those characters. Validate each permutation against the given
 dictionary.
Now let's think about optimal solution:
If you're familiar with topological sort and what it means, however, you'll see that this is a simple application of topological
 sort.
Quick recap - Topological sort is ordering the vertices in a directed graph such that vertex A appears before vertex B for
 all directed edges A->B. One way to look at it is that you're given a graph of dependencies and you want to order the vertices
 such that no dependencies are broken when going from left to right.
So, what is the graph in this question anyway?
Since we are given the words sorted lexicographically, we know which character precedes what other characters.
How do we determine these relationships between characters in practice?
We know a few things about the dictionary ordering.
In a dictionary, between two adjacent words, one of the following is true:
1. there is at least one character different. Eg. "abcd" and "abde" in English.
2. one word is shorter than other. Eg. "abc" and "abcd" in English.
In case 1, we know from the dictionary's property that the character at mismatch index in the left word appears before its
 counter part in right word in the alphabet.
In case 2, there is no meaningful information with respect to the alphabet
It is also necessarily true between two adjacent words, that the characters after the first mismatch do not convey any relationship
 between the characters
We can compare two adjacent words and try to find a mismatch. First mismatch denotes that, letter in first word will come
 before letter in second word in that alien language. Let's take one example to understand this:
words =
[
"c",
"aaaa",
"aaaa",
"aabc"
] 
Then we compare: 
1) "c" and "aaaa", here first mismatch is between 'c' and 'a' hence we are sure that 'c' will come before 'a'.
2) "aaaa" and "aaaa", here there is no mismatch so we can not conclude anything!  
3) "aaaa" and "aabc", here first mismatch is between 'a' and 'b' hence we are sure that 'a' will come before 'b'. Also note
 that we should only consider first mismatch. So from second mismatch concluding that 'a' will come before 'c' is wrong!
 
Now total information we have collected is:
1) 'c' comes before 'a'
2) 'a' comes before 'b'
Combining them we can figure out the order of characters is 'cab' in the given alien language. 
Here we can use directed graph to combine the information collected by comparing words. Add an directed edge between first
 mismatched characters! Our directed graph will be directed acyclic graph! Now on DAG we can use topological sort to get
 the order of characters! 
Now have a look at the solution provided by us.  
Time complexity:
In the solution one word will be compared maximum two times. With 1) previous word and 2) next word. So comparing words
 and finding edges will take O(2 * total number of characters) = O(total number of characters). 
Also an edge is added when a mismatch is found. Maximum number of mismatch will be <= number of words. So in our directed
 graph |V| is O(number of different characters) and |E| is O(number of words). We know that topological sort takes O(V +
 E) time, so that is O(number of different characters + number of words).
So our overall time complexity will be O(total number of characters + number of different characters + number of words)
 = O(total number of characters).
Space complexity:
Input is O(total number of characters) and graph we will build will be O(number of different characters + number of words).
 So space complexity is also O(total number of characters). 
'''
'''
# ------------------------------------------ START ------------------------------------------

from collections import defaultdict


def find_order(words):
        all_chars = set()
        for word in words:
            for c in word:
                all_chars.add(c)

        deps = defaultdict(set)  # dependency -> dependants
        # get word and its following word one by one
        for w1, w2 in zip(words, words[1:]):
            # do the same character by character
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    deps[c1].add(c2)
                    break

        order = []
        visited = {}

        # use visited (1), visiting(-1) and unvisited (not in dictionary) states to keep track
        # dfs returns False if there is a cycle
        def _dfs(node):
            status = visited.get(node)
            # have visited this node
            if status == 1:
                return True
            # there is a cycle as this node is currently being visited
            if status == -1:
                return False

            # set to visiting
            visited[node] = -1

            for n in deps[node]:
                if not _dfs(n):
                    return False

            # complete visiting and add to order
            visited[node] = 1
            order.append(node)
            return True

        # run through dfs and check for cycles
        for c in all_chars:
            if not _dfs(c):
                return ''

        # since order is used as a stack it will be need to be reversed to get the right order
        return ''.join(reversed(order))

# ------------------------------------------ STOP ------------------------------------------


# MAIN/TEST CASES
w = ["baa", "abcd", "abca", "cab", "cad"]
print(find_order(w))
'''
