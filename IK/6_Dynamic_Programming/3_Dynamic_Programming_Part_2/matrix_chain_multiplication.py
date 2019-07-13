'''
Matrix Chain Multiplication
Problem Statement:
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually
 to perform the multiplications, but merely to decide in which order to perform the multiplications.
We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words, no matter
 how we parenthesize the product, the result will be the same. For example, if we had four matrices A, B, C, and D, we would
 have:
(ABC)D = (AB)(CD) = A(BCD) = ....
However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute
 the product, or the efficiency. For example, suppose A is a 10 × 30 matrix, B is a 30 × 5 matrix, and C is a 5 × 60 matrix.
 Then,
(AB)C = (10×30×5) + (10×5×60) = 1500 + 3000 = 4500 operations
A(BC) = (30×5×60) + (10×30×60) = 9000 + 18000 = 27000 operations.
Clearly, the first parenthesization requires less number of operations.
Given an array mtxSizes[], which represents the chain of matrices such that the ith matrix Ai is of dimension mtxSizes[i-1]
 x mtxSizes[i], we need to write a function that should return the minimum number of multiplications needed to multiply
 the chain. Length of chain of matrices is n, and thus size of mtxSizes is (n+1).
Input/Output Format For The Function:
Input Format:
You will be given an integer array mtxSizes.
Output Format:
Return an integer minOps, denoting the minimum number of operations needed.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain a number, denoting the size of mtxSizes, which is (n+1).
In next (n+1) lines, ith line should contain ith entry of mtxSizes, i=(1,...,n+1).
If n = 4 and mtxSizes = [10, 30, 5, 60], then input should be:
4
10
30
5
60
Output Format:
There will be one line, containing an integer minOps, denoting the result returned by solution function.
For input n = 4 and mtxSizes = [10, 30, 5, 60], output will be:
4500
Constraints:
3 <= len(mtxSizes) <= 100
0 <= mtxSizes[i] <= 100
For any matrix, either both the dimensions will be zero, or both the dimensions
 will be non zero.
Sample Test Case:
Sample Input:
4
10
30
5
60
Sample Output:
4500
Explanation:
As explained in problem statement section.
'''
import sys
import os

# Complete the function below.
def  minMultiplicationCost(mtxSizes):
    pass


f = sys.stdout
_mtxSizes_cnt = 0
_mtxSizes_cnt = int(input())
_mtxSizes_i = 0
_mtxSizes = []
while _mtxSizes_i < _mtxSizes_cnt:
    _mtxSizes_item = int(input());
    _mtxSizes.append(_mtxSizes_item)
    _mtxSizes_i += 1
res = minMultiplicationCost(_mtxSizes);
f.write(str(res) + "\n")
f.close()


'''
Recursive solution
A function f(start, end) is defined to denote the minimum operations needed for solving the mtxSizes in the range start…end

Thus the base case would be
f(i, i+1) = 0
This is because it is denoting a single matrix.
Lets put a parenthesis at index. We can recur for the cost for start…index and index…end.
cost[index] = mtxSizes[start]*mtxSizes[index]*mtxSizes[end] + f(start, index) + f(index, end)
Recurrence relationship for this problem would be
f(start, end) = min(cost[index])
where start<index<end
Optimal solution
We can memoize the recurrence relationship mentioned above or build an iterative version for the same problem. We can see
 there are overlapping subproblems.
We can maintain a 2D table of size nxn. Thus every table cell denotes f(i,j).
Space Complexity: O(length(mtxSizes)^2)
Time Complexity: O(length(mtxSizes)^3)
'''
'''
import java.util.TreeSet;

public class OptimalSolution {
    // ==================start==================
    
    /*
     * Code author: Akshay Miterani
     * Space Complexity: O(len(mtxSizes)^2)
     * Time Complexity: O(len(mtxSizes)^3)
     */
    static int minMultiplicationCost(List<Integer> mtxSizes) {
        int n = mtxSizes.size();
        // Make the dp table
        int table[][] = new int[n][n];
        // Initialize all values with max value
        IntStream.range(0, n).forEach(i -> {
            Arrays.fill(table[i], Integer.MAX_VALUE);
        });
        return minCostFor(0, n - 1, mtxSizes, table);
    }
    
    private static int minCostFor(int start, int end, List<Integer> mtxSizes, int table[][]) {
        // If the value is stored in table, return the value
        if (table[start][end] != Integer.MAX_VALUE) {
            return table[start][end];
        }
        
        // If start and end have met, we have hit the base condition
        if (start + 1 == end) {
            return 0;
        }
        
        int min = Integer.MAX_VALUE;
        // Place parenthesis at every index and find out the minimum recursively
        for (int index = start + 1; index <= end - 1; index++) {
            // Cost of placing parenthesis at index
            int cost = mtxSizes.get(start) * mtxSizes.get(end) * mtxSizes.get(index)
            + minCostFor(start, index, mtxSizes, table) + minCostFor(index, end, mtxSizes, table);
            
            // Take the minimum of cost at every index
            min = Math.min(min, cost);
        }
        
        // Store and return the value
        table[start][end] = min;
        return table[start][end];
    }
    
    // ==================end==================}
'''

