'''
Area under histogram
Problem Statement:
You will be given an array arr of height of bars, of size n. You have to answer q queries, where in each query, you will
 be given left index l and right index r. For each query, return largest rectangular area possible in a histogram formed
 using (right-left+1) bars with array of heights as [arr[left], arr[left+1], arr[left+2], ..., arr[right]]. Largest rectangle
 can be made of a number of contiguous bars. For simplicity, you can assume that all bars have same width and the width
 is 1 unit.
For example, consider the following histogram with 7 bars of heights [6, 2, 5, 4, 5, 1, 6]. The largest possible rectangle
 possible is 12 (see the below figure, the max area rectangle is highlighted in red).

 https://i.imgur.com/RNPHUrV.png

(source: https://goo.gl/fTcCTK)
Input/Output Format For The Function:
Input Format:
There are three arguments: arr, denoting input array of height of bars, l denoting left and r denoting right as explained
 in problem statement.
Output Format:
Return a number maxArea, denoting maximum rectangular area possible in a histogram formed as explained in problem statement.

Input/Output Format For The Custom Input:
Input Format:
The first line of the input should contain a single integer n, denoting the size of input array arr. In the next n lines,
 ith line should contain a number arr[i], denoting ith number of the input array arr, i=(1,2,...,n).
Next line should contain q, denoting no. of queries that need to be answered. In next 2*q lines, (2*i-1)th line should contain
 left value for ith query and (2*i)th line should contain right value for ith query, i=(1,2,...,q), i.e. 1st and 2nd line
 should contain left and right values for 1st query, 3rd and 4th line should contain left and right values for 2nd query,
 and so on...
If n = 5, arr = [2, 4, 6, 5, 8], q = 2, for 1st query: l = 0 and r = 4 and for 2nd query: l = 3 and r = 3, then input should be:
5
2
4
6
5
8
2
0
4
3
3
Output Format:
There will be q lines, where ith line contains a number maxArea[i], denoting result of ith query.
For input n = 5, arr = [2, 4, 6, 5, 8], q = 2, for 1st query: l = 0 and r = 4 and for 2nd query: l = 3 and r = 3, output will be:
16
5

Constraints:
1 <= n <= 2*10^5
1 <= q <= 10
1 <= arr[i] <= 10^9, i=(0,1,2,3,...,n-1)
0 <= l <= r < n for each query.

Sample Test Cases:
Sample Input 1:
arr = [6, 2, 5, 4, 5, 1, 6]
q = 1
For 1st query: l = 0 and r = 6.
Sample Output 1:
12
Explanation 1:
1st query: A rectangle of area 12 can be formed using 2nd to 4th bar (0-based indexing) and has maximum area possible in
 histogram out of all possible rectangles that can be formed using contiguous bar with given array of heights [arr[0],…,arr[6]]
 = [6, 2, 5, 4, 5, 1, 6] as l=0 and r=6.

Sample Input 2:
arr = [2, 4, 6, 5, 8]
q = 2
For 1st query: l = 0 and r = 4.
For 2nd query: l = 3 and r = 3.
Sample Output 2:
16
5
Explanation 2:
1st query: A rectangle of area 16 can be formed using 1st to 4th bar (0-based indexing) and has maximum area possible in
 histogram out of all possible rectangles that can be formed using contiguous bar with given array of heights [arr[0], …,
 arr[4]] = [2, 4, 6, 5, 8] as l=0 and r=4.
2nd query: A rectangle of area 5 can be formed using 3rd to 3rd bar (0-based indexing) and has maximum area possible in
 histogram out of all possible rectangles that can be formed using contiguous bar with given array of heights [arr[3]] =
 [5] as l=3 and r=3.
Suggestions:
Suggested time in interview: 30 minutes.
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework i.e.
 For the first attempt of a given homework problem, the focus should be to understand what the problem is asking, what approach
 you are using, coding it, as well as identifying any gaps that you can discuss during a TA session.
Take your time, but limit yourself to 2 one hour sessions for most problems.
'''
import os
import sys


# Complete the findMaxPossibleArea function below.
def findMaxPossibleArea(heights, l, r):
    pass


if __name__ == "__main__":
    fptr = sys.stdout
    heights_count = int(input())
    heights = []
    for _ in range(heights_count):
        heights_item = int(input())
        heights.append(heights_item)
    q = int(input())
    for _ in range(q):
        l = int(input())
        r = int(input())
        res = findMaxPossibleArea(heights, l, r)
        fptr.write(str(res) + '\n')
    fptr.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
A naive approach would be to check area of all possible rectangles that can be made using bars in given histogram and find
 the max area rectangle.
To implement this approach, iterate over all bars j for each bar i, j>=i, find the smallest height bar 'hsmall' from (i,
 i+1, i+2, ..., j)th bars. Then area of largest rectangle made using (i, i+1, i+2 , ..., j)th bars would be currentArea
 = (hsmall * (j - i + 1)). Compare with max area 'maxArea' found till now and replace it if maxArea < currentArea.
Time Complexity:
O(n*n) where n is length of input array arr.
As we are iterating over all possible subarrays, it will take O(n*n).
This time complexity is for function findMaxPossibleArea.
Auxiliary Space Used:
O(1).
As we are not storing anything extra.
This auxiliary is for function findMaxPossibleArea.
Space Complexity:
O(n) where n is length of input array arr.
To store array it will take O(n) and as auxiliary space used is O(1).
So, O(n) + O(1) → O(n).
This space complexity is for function findMaxPossibleArea.
2) optimal_solution1.java
Description:
The optimal would be as follows:
As we are calling this function with given l and r.
For each element arr[i+l], find the first element smaller than it on its left (only consider upto index l) and that on its
 right (only consider upto index r) and build arrays leftSmaller and rightSmaller.
Thus, leftSmaller[i] = j, implies that j is greatest index smaller than i+l such that arr[i+l]>arr[j] and rightSmaller[i]
 = j, implies that j is smallest index greater than i+l such that arr[i+l]>arr[j].
Notice that all elements in subarray arr[leftSmaller[i]+1], arr[leftSmaller[i]+2],..., arr[rightSmaller[i]-1] are greater
 than or equal to arr[i+l]. So, the max area a rectangle can have such that it must contain ith bar is (arr[i+l]*((rightSmaller[i]-1)
 - (leftSmaller[i]+1) + 1).
Time Complexity:
O(n) where n is length of input array arr.
Arrays leftSmaller and rightSmaller can be generated in a single traversal of arr input array, one traversal of arr array
 for each using stack.
So, to create leftSmaller and rightSmaller array it will take O(n) and to find result it will take O(n).
So, O(n) + O(n) → O(n).
This time complexity is for function findMaxPossibleArea.
Auxiliary Space Used:
O(n) where n is length of input array arr.
To store leftSmaller and rightSmaller array in generating them stack used which will take O(n) space.
This auxiliary is for function findMaxPossibleArea.
Space Complexity:
O(n) where n is length of input array arr.
As to store input array it will take O(n) and auxiliary space used is O(n).
Hence, O(n) + O(n) → O(n).
This space complexity is for function findMaxPossibleArea.
3) optimal_solution2.java
Description:
This would be more optimal approach in comparison to approach of optimal_solution2.java.
In optimal_solution1, we traverse array 3 times to find answer but here we will traverse array once to find our answer.

For every bar ‘x’, we calculate the area with ‘x’ as the smallest bar in the rectangle. If we calculate such area for every
 bar ‘x’ and find the maximum of all areas, our task is done. How to calculate area with ‘x’ as smallest bar? We need to
 know index of the first smaller (smaller than ‘x’) bar on left of ‘x’ and index of first smaller bar on right of ‘x’. Let
 us call these indexes as ‘left index’ and ‘right index’ respectively.
We traverse all bars from left to right, maintain a stack of bars.
Every bar is pushed to stack once. A bar is popped from stack
when a bar of smaller height is seen. When a bar is popped, we calculate the area with the popped bar as smallest bar. How
 do we get left and right indexes of the popped bar – the current index tells us the ‘right index’ and index of previous
 item in stack is the ‘left index’. Following is the complete algorithm.
1) Create an empty stack.
2) Start from first bar, and do following for every bar ‘arr[i]’ where ‘i’ varies from l to r (As we are calling this function
 for each query with given l and r).
……a) If stack is empty or arr[i] is higher than the bar at top of stack, then push ‘i’ to stack.
……b) If this bar is smaller than the top of stack, then keep removing the top of stack while top of the stack is greater.
 Let the removed bar be arr[tp]. Calculate area of rectangle with arr[tp] as smallest bar. For arr[tp], the ‘left index’
 is previous (previous to tp) item in stack and ‘right index’ is ‘i’ (current index).
3) If the stack is not empty, then one by one remove all bars from stack and do step 2.b for every removed bar.
For better understanding, please look solution once.
Time Complexity:
O(n) where n is length of input array arr.
As we are traversing through array to calculate our answer and size of array is r-l+1 in worst case it can be n. So, time
 complexity will be O(n).
This time complexity is for function findMaxPossibleArea.
Auxiliary Space Used:
O(n) where n is length of input array arr.
To maintain stack of size r-l+1 in worst case it can be n which is length of input array arr. So, auxiliary space used will
 be O(n).
This auxiliary is for function findMaxPossibleArea.
Space Complexity:
O(n) where n is length of input array arr.
As to store input array it will take O(n) and auxiliary space used is O(n).
Hence, O(n) + O(n) → O(n).
This space complexity is for function findMaxPossibleArea.
'''
'''
BRUTE FORCE
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Find the largest rectangular area possible in a given histogram, where 
 * the largest rectangle can be made of a number of contiguous bars. 
 * For simplicity, assume that all bars have same width and the width is 1 unit. 
 * You will be given an array arr of height of bars of size n.
 */

import java.io.*;
import java.util.*;

class Result {

    // ============================ Start ============================
    static long findMaxPossibleArea(long[] arr, int l, int r) {
        long maxArea = 0;
        long currentMaxPossibleHeight, currentMaxArea;
        //Iterating over all rectangles which starts from ith bar
        for (int i = l; i <= r; i++) {
            currentMaxPossibleHeight = Long.MAX_VALUE;
            // Finding area of rectangle which starts from ith bar and ends at jth bar
            for (int j = i; j <= r; j++) {
                // Height of rectangle which starts from ith bar and ends at jth bar 
                // can be minimum of all the heights (arr[k], i<=k<=j) between i and j.
                currentMaxPossibleHeight = Math.min(currentMaxPossibleHeight, arr[j]);
                currentMaxArea = currentMaxPossibleHeight * (j - i + 1);
                maxArea = Math.max(currentMaxArea, maxArea);
            }
        }
        return maxArea;
    }
    // ============================= End ==============================
}

class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        int heightsCount = Integer.parseInt(bufferedReader.readLine().trim());

        long[] heights = new long[heightsCount];

        for (int heightsItr = 0; heightsItr < heightsCount; heightsItr++) {
            heights[heightsItr] = Long.parseLong(bufferedReader.readLine().trim());
        }

        int q = Integer.parseInt(bufferedReader.readLine().trim());
        for (int i = 0; i < q; i++) {
            int l = Integer.parseInt(bufferedReader.readLine().trim());

            int r = Integer.parseInt(bufferedReader.readLine().trim());

            long res = Result.findMaxPossibleArea(heights, l, r);
            bufferedWriter.write(res+"\n");
        }
        bufferedWriter.close();
    }
}
/**
 * Time complexity: O(n*n)
 * Space complexity: O(n)
 */
'''
'''
OPTIMAL SOLUTION 1
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Find the largest rectangular area possible in a given histogram, where 
 * the largest rectangle can be made of a number of contiguous bars. 
 * For simplicity, assume that all bars have same width and the width is 1 unit. 
 * You will be given an array arr of height of bars of size n.
 */

import java.io.*;
import java.util.*;

class Result {

    // ============================ Start ============================
    static long findMaxPossibleArea(long[] arr, int l, int r) {
        int n = r - l + 1;
        long maxArea = 0;
        
        // rightSmaller[i] = j, implies that j is smallest index greater than i 
        // such that arr[l+i]>arr[r+j] where 0<=i<(r-l+1) and 0<=j<(r-l+1)

        // To fill rightSmaller array
        int[] rightSmaller = new int[n];
        Stack<Integer> stack = new Stack<Integer>();
        
        for (int i = l; i <= r; i++) {
            if (stack.isEmpty()) {
                stack.push(i);
            } else {
                while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                    int popped = stack.pop();
                    rightSmaller[popped - l] = i - l;
                }
                stack.push(i);
            }
        }
        while (!stack.isEmpty()) {
            int popped = stack.pop();
            rightSmaller[popped - l] = n;
        }

        // leftSmaller[i] = j, implies that j is smallest index greater than i 
        // such that arr[l+i]>arr[r+j] where 0<=i<(r-l+1) and 0<=j<(r-l+1)

        // To fill leftSmaller array
        int[] leftSmaller = new int[n];
        
        for (int i = r; i >= l; i--) {
            if (stack.isEmpty()) {
                stack.push(i);
            } else {
                while (!stack.isEmpty() && arr[stack.peek()] > arr[i]) {
                    int popped = stack.pop();
                    leftSmaller[popped - l] = i - l;
                }
                stack.push(i);
            }
        }
        while (!stack.isEmpty()) {
            int popped = stack.pop();
            leftSmaller[popped - l] = -1;
        }
        // Notice that all elements in subarray arr[leftSmaller[i]+1], arr[leftSmaller[i]+2],...,
        // arr[rightSmaller[i]-1] are greater than or equal to arr[i]
        // So, the max area a rectangle can have such that it must contain ith bar is
        // (arr[i]*((rightSmaller[i]-1) - (leftSmaller[i]+1) + 1)

        // to calculate histogram area. here n = r - l + 1
        long currentMaxArea;
        for (int i = 0; i < n; i++) {
            currentMaxArea = arr[i + l] * (rightSmaller[i] - leftSmaller[i] - 1);
            maxArea = Math.max(currentMaxArea, maxArea);
        }
        return maxArea;
    }
    // ============================= End ==============================
}

class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        int heightsCount = Integer.parseInt(bufferedReader.readLine().trim());

        long[] heights = new long[heightsCount];

        for (int heightsItr = 0; heightsItr < heightsCount; heightsItr++) {
            heights[heightsItr] = Long.parseLong(bufferedReader.readLine().trim());
        }

        int q = Integer.parseInt(bufferedReader.readLine().trim());
        for (int i = 0; i < q; i++) {
            int l = Integer.parseInt(bufferedReader.readLine().trim());

            int r = Integer.parseInt(bufferedReader.readLine().trim());

            long res = Result.findMaxPossibleArea(heights, l, r);
            bufferedWriter.write(res+"\n");
        }
        bufferedWriter.close();
    }
}
/**
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
'''
'''
OPTIMAL SOLUTION 2
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Find the largest rectangular area possible in a given histogram, where 
 * the largest rectangle can be made of a number of contiguous bars. 
 * For simplicity, assume that all bars have same width and the width is 1 unit. 
 * You will be given an array arr of height of bars of size n.
 */

import java.io.*;
import java.util.*;

class Result {

    // ============================ Start ============================
    static long findMaxPossibleArea(long[] arr, int l, int r) {
        // Create an empty stack. The stack holds indexes of arr[] array which can be from l to r. 
        // The bars stored in stack are always in increasing order of their heights. 
        Stack<Integer> stack = new Stack<>();
        
        long max_area = 0; // Initialize max area 
        int tp;  // To store top of stack 
        long area_with_top; // To store area with top bar as the smallest bar 
       
        // Run through all bars of given histogram 
        int i = l; 
        while (i <= r) 
        { 
            // If this bar is higher than the bar on top stack, push it to stack 
            if (stack.empty() || arr[stack.peek()] <= arr[i]) 
                stack.push(i++); 
       
            // If this bar is lower than top of stack, then calculate area of rectangle  
            // with stack top as the smallest (or minimum height) bar. 'i' is  
            // 'right index' for the top and element before top in stack is 'left index' 
            else
            { 
                tp = stack.peek();  // store the top index 
                stack.pop();  // pop the top 
       
                // Calculate the area with arr[tp] stack as smallest bar 
                area_with_top = arr[tp] * 1l * (stack.empty() ? i-l : i - stack.peek() - 1); 
       
                // update max area, if needed 
                if (max_area < area_with_top) 
                    max_area = area_with_top; 
            } 
        } 
       
        // Now pop the remaining bars from stack and calculate area with every 
        // popped bar as the smallest bar 
        while (stack.empty() == false) 
        { 
            tp = stack.peek(); 
            stack.pop(); 
            area_with_top = arr[tp] * 1l * (stack.empty() ? i-l : i - stack.peek() - 1); 
       
            if (max_area < area_with_top) 
                max_area = area_with_top; 
        } 
       
        return max_area;
    }
    // ============================= End ==============================
}

class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recursion stack. It makes the size of stack
        2^26 ~= 10^8
        */
        new Thread(null, new Runnable() {
            public void run() {
                try{
                    solve();
                }
                catch(Exception e){
                    e.printStackTrace();
                }
            }
        }, "1", 1 << 26).start();
    }
    public static void solve() throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        int heightsCount = Integer.parseInt(bufferedReader.readLine().trim());

        long[] heights = new long[heightsCount];

        for (int heightsItr = 0; heightsItr < heightsCount; heightsItr++) {
            heights[heightsItr] = Long.parseLong(bufferedReader.readLine().trim());
        }

        int q = Integer.parseInt(bufferedReader.readLine().trim());
        for (int i = 0; i < q; i++) {
            int l = Integer.parseInt(bufferedReader.readLine().trim());

            int r = Integer.parseInt(bufferedReader.readLine().trim());

            long res = Result.findMaxPossibleArea(heights, l, r);
            bufferedWriter.write(res+"\n");
        }
        bufferedWriter.close();
    }
}
/**
 * Time complexity: O(n)
 * Space complexity: O(n)
 */
'''

