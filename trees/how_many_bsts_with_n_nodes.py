'''
How Many Binary Search Trees With n Nodes?

Problem Statement:
Write a function that will return the number of binary search trees that can be constructed, with n nodes.
There may be other iterative solutions, but for the purpose of this exercise, please use recursive solution.

Input Format:
There is only one argument denoting integer n.

Output Format:
Return number of binary search trees that can be constructed, with n nodes.

Constraints:
1 <= n <= 16

Sample Test Cases:
Sample Input 1:
1

Sample Output 1:
1

Explanation 1:
1) root (node val = 1)

Sample Input 2:
2

Sample Output 2:
2

Explanation 2:
1) root (node val = 2), root->left (node val = 1)
2) root (node val = 1), root->right (node val = 2)

Sample Input 3:
3

Sample Output 3:
5

Explanation 3:
1) root (node val = 3), root->left (node val = 2), root->left->left (node val = 1)
2) root (node val = 3), root->left (node val = 1), root->left->right (node val = 2)
3) root (node val = 1), root->right (node val = 2), root->right->right (node val = 3)
4) root (node val = 1), root->right (node val = 3), root->right->left (node val = 2)
5) root (node val = 2), root->left (node val = 1), root->right (node val = 3)

If you keep doing this, it will form a series called Catalan numbers. One can simply lookup the formula for Catalan
numbers and write code for it. But that's not how we want to do this. We want to do this by understanding the
underlying recursion. The recursion is based on tree-topology only, as you can see by examples above, contents of the
nodes of the tree do not matter.
'''

def num_ways(n):
    if n in [1, 2]:
        return n
    allLeft = num_ways(n-1)
    allRight = num_ways(n-1)
    both = num_ways(n-2)+num_ways(n-2)
    return allLeft+allRight+both

# print(num_ways(1))
# print(num_ways(2))
# print(num_ways(3))
print(num_ways(4))
# print(num_ways(5))
# print(num_ways(6))
# print(num_ways(7))
# print(num_ways(8))
# print(num_ways(9))
# print(num_ways(10))
# print(num_ways(11))
# print(num_ways(12))
# print(num_ways(13))
