'''
Merge Overlapping Intervals
Problem Statement:
Given an array of time intervals(in any order) inputArray, of size n, merge all overlapping intervals into one and return
 the resulting array outputArray, such that no two intervals in outputArray are overlapping. In other words, result array
 should contain only mutually exclusive intervals. Hence, in outputArray, no pair of intervals i and j exists, such that

outputArray[i][0] <= outputArray[j][0] <= outputArray[i][1].
(In this problem, you should consider all the intervals as closed intervals. i.e. endpoints of intervals are inclusive.)

Input/Output Format For The Function:
Input Format:
There is only one argument: inputArray, denoting input array of time intervals, where inputArray is 2D array of n*2 size,
 denoting inputArray[i][0] as start point of ith interval, and inputArray[i][1] as end point of ith interval.
Output Format:
Return an array of time intervals outputArray, denoting the required array of merged time intervals, where outputArray is
 2D array of len*2 size, denoting outputArray[i][0] as start point of ith interval, and outputArray[i][1] as end point of
 ith interval.
(Order of intervals in outputArray doesn't matter.)
Input/Output Format For The Custom Input:
Input Format:
First line should contain a number n, denoting number of intervals in inputArray. Next line should contain 2, unconditionally,
 as inputArray is 2D array of n*2. In next n lines, ith line should contain two space separated numbers starti and endi,
 denoting start point and end point of ith interval respectively.
If n = 4, inputArray = [[1, 3], [5, 7], [2, 4], [6, 8]], then input should be:
4
2
1 3
5 7
2 4
6 8
Output Format:
Let say len*2 is the size of resultant 2D array outputArray. Then, there will be len lines, where ith line contains two
 space separated integers starti and endi, denoting start point and end point of ith interval in outputArray respectively.

For input n = 4, inputArray = [[1, 3], [5, 7], [2, 4], [6, 8]], output will be:
1 4
5 8
Constraints:
1 <= n <= 10^5
-10^9 <= inputArray[i][0] <= inputArray[i][1] <= 10^9,   i=0, 1, ..., (n-1)
Sample Test Cases:
Sample Input 1:
4
2
1 3
5 7
2 4
6 8
Sample Output 1:
1 4
5 8
Explanation 1:
The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1,4}.
Similarly {5,7} and {6,8} should be merged and become {5,8}.
Sample Input 2:
7
2
100 154
13 47
1 5
2 9
7 11
51 51
47 50
Sample Output 2:
1 11
13 50
51 51
100 154
Explanation 2:
The intervals {1,5} and {2,9} overlap with each other, so they should be merged and become {1,9}.
Also, {1,9} and {7,11} overlap with each other, so they should be merged and become {1,11}
Similarly, The intervals {13,47} and {47,50} should be merged and become {13,50}.
Intervals {51,51} and {100,154} are kept as it is as they are not overlapping with any other intervals.
Suggestions:
Suggested time in interview: 20 minutes.
The “Suggested Time” is the time expected to complete this question during a real-life interview, not now in homework i.e.
 For the first attempt of a given homework problem, the focus should be to understand what the problem is asking, what approach
 you are using, coding it, as well as identifying any gaps that you can discuss during a TA session. Take your time, but
 limit yourself to 2 one hour sessions for most problems.
'''
import os
import sys

#
# Complete the getMergedIntervals function below.
#
def getMergedIntervals(inputArray):
    pass



if __name__ == "__main__":
    f = sys.stdout
    inputArray_rows = int(input())
    inputArray_columns = int(input())
    inputArray = []
    for _ in range(inputArray_rows):
        inputArray.append(list(map(int, input().rstrip().split())))
    res = getMergedIntervals(inputArray)
    f.write('\n'.join([' '.join(map(str, x)) for x in res]))
    f.write('\n')
    f.close()


'''
We have provided solutions which contain necessary comments to understand the approach used:
1) brute_force_solution.java
Description:
A naive approach would be that iterating over inputArray,
For 0<=i<=n-1, Check if inputArray[i] is a removed interval.
If it’s a removed interval continue.
If it's not a removed interval, compare inputArray[i] with all other intervals for
 overlapping. Let say it overlaps with interval inputArray[k], then remove inputArray[k] from array and merge it into the
 inputArray[i].
For removing an interval from array, one way is to make the interval invalid (i.e. start>end), so that later we can
check if it is removed or not. See implementation for better understanding.
Time Complexity:
O(n*n) where n is length of inputArray.
As we have to iterate entire input interval array for each interval, time complexity will be O(n*n).
Auxiliary Space Used:
O(1).
Here, all updation can be done in inputArray only. So, no extra space is used.
Space Complexity:
O(n) where n is length of inputArray.
For inputArray, it takes O(n) and auxiliary space used is O(1). So, O(n) + O(1) → O(n).
2) other_solution.java
Description:
An efficient approach would be as follows:
Sort the interval array in increasing order of start point. Once we have sorted intervals, we can combine all intervals
 in a linear traversal.
Following is the detailed step by step algorithm.
Sort the intervals based on increasing order of starting time.
Push the first interval on to a stack.
For each interval
 do the following
If the current interval does not overlap with the stack top, push it.
If the current interval overlaps
 with stack top and ending time of current interval is more than that of stack top, update stack top with the ending  time
 of current interval.
At the end stack contains the merged intervals.
Time Complexity:
O(n*log(n)) where n is length of inputArray.
As we have to sort the interval array, followed by linear traversal, time complexity will be
O(n*log(n)) + O(n) → O(n*log(n)).
Auxiliary Space Used:
O(n) where n is length of inputArray.
Here we have used Stack. So, extra space is used other than that of inputArray. So, auxiliary space used is O(n). (Here
 we are ignoring auxiliary space used by inbuilt sort function for sorting n elements of inputArray because it is language
 specific like in java, it will take O(1) but in python it will take O(n)).
Space Complexity:
O(n) where n is length of inputArray.
For inputArray, it takes O(n) and auxiliary space used is O(n). So, O(n) + O(n) → O(n).
3) optimal_solution.java
Description:
Auxiliary space used in above approach is O(n). It can be reduced.
The idea remains same as discussed in previous approach. Sort the interval array in increasing order of starting point.

Once you have sorted intervals, you can combine all intervals in a linear traversal.
Following is the detailed step by step algorithm:
Let last be the last interval of non overlapping intervals. last=0.
Iterating over inputArray, starting from second interval (1<=i<=n-1)
Check if inputArray[i] is overlapping with inputArray[last]
If overlapping, merge inputArray[i] and inputArray[last], For
 merging them, it is sufficient to update only endpoint of inputArray[last] as it is guaranteed that starting point of inputArray[last]
 <= starting point of inputArray[i][0] as array is sorted by starting point.
If non overlapping, we increment last and moving
 on, inputArray[i] is the new interval under test of overlapping with following intervals.
repeat step 1 for i=i+1.
Time Complexity:
O(n*log(n)) where n is length of inputArray.
As we have to sort the interval array, followed by linear traversal, time complexity will be
O(n*log(n)) + O(n) → O(n*log(n)).
Auxiliary Space Used:
O(1).
Here, all updation can be done in inputArray only. So, no extra space is used. (Here we are ignoring auxiliary space used
 by inbuilt sort function for sorting n elements of inputArray because it is language specific like in java, it will take
 O(1) but in python it will take O(n)).
Space Complexity:
O(n) where n is length of inputArray.
For inputArray, it takes O(n) and auxiliary space used is O(1). So, O(n) + O(1) → O(n).
'''
'''
BRUTE FORCE
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which
 * should have only mutually exclusive intervals.
 *
 * e.g. for this input: {{1,3}, {2,4}, {5,7}, {6,8} }.
 * The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}.
 * Similarly {5, 7} and {6, 8} should be merged and become {5, 8}.
 *
 * Write a function which produces the set of merged intervals for the given set of intervals.
 */

import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static int[][] getMergedIntervals(int[][] inputArray) {
        for (int i = 0; i < inputArray.length; i++) {
            // Check if it is an invalid interval
            if (isInvalidInterval(inputArray[i])) {
                continue;
            }

            for (int j = 0; j < inputArray.length; j++) {
                // Check if it is an invalid interval
                if (i == j || isInvalidInterval(inputArray[j])) {
                    continue;
                }
                // Check if interval[i] and interval[j] are overlapping
                if (is_overlapping(inputArray[i], inputArray[j])) {
                    inputArray[i][0] = Math.min(inputArray[i][0], inputArray[j][0]);
                    inputArray[i][1] = Math.max(inputArray[i][1], inputArray[j][1]);
                    invalidateInterval(inputArray[j]);
                    // Here, for removing an interval from inputArray, we will make it an invalid interval
                    // (i.e. interval.start > interval.end) as actually removing it from array will be an inefficient way.
                }
            }
        }
        int outputArraySize = 0;
        for (int i = 0; i < inputArray.length; i++) {
            // Check if it is an invalid interval.
            // Invalid intervals are the ones which are removed(merged into some other intervals).
            if (!isInvalidInterval(inputArray[i])) {
                outputArraySize++;
            }
        }

        int[][] outputArray = new int[outputArraySize][2];
        int ptr = 0;
        for (int i = 0; i < inputArray.length; i++) {
            if (!isInvalidInterval(inputArray[i])) {
                outputArray[ptr++] = inputArray[i];
            }
        }

        return outputArray;
    }

    private static boolean isInvalidInterval(int[] inputArray) {
        return (inputArray[0] > inputArray[1]);
    }

    private static void invalidateInterval(int[] interval) {
        interval[0] = 1;
        interval[1] = 0;
    }

    private static boolean is_overlapping(int[] interval1, int[] interval2) {
        return !isInvalidInterval(interval1) && !isInvalidInterval(interval2) &&
                !(interval1[1] < interval2[0] || interval2[1] < interval1[0]);
    }
    // -------------------- END ----------------------
}

class Solution{
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

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        int m = Integer.parseInt(bufferedReader.readLine().trim());

        int[][] inputArray = new int[n][m];

        for (int i = 0; i < n; i++) {
            String[] str = bufferedReader.readLine().split(" ");
            for(int j = 0; j < m; j++){
                inputArray[i][j] = Integer.parseInt(str[j].trim());
            }
        }

        int[][] res = Result.getMergedIntervals(inputArray);

        for (int i = 0; i < res.length; i++) {
            bufferedWriter.write(res[i][0]+" "+res[i][1]+"\n");
        }
        
        bufferedReader.close();
        bufferedWriter.close();
    }

}

/**
 * Time complexity: O(N*N)
 * Auxiliary Space complexity: O(N)
 */
'''
'''
OTHER SOLUTION
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which
 * should have only mutually exclusive intervals.
 *
 * e.g. for this input: {{1,3}, {2,4}, {5,7}, {6,8} }.
 * The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}.
 * Similarly {5, 7} and {6, 8} should be merged and become {5, 8}.
 *
 * Write a function which produces the set of merged intervals for the given set of intervals.
 */

import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------
    static int[][] getMergedIntervals(int[][] inputArray) {
        // Sorting the input interval array by their starting points in increasing order
        Arrays.sort(inputArray, (int object1[], int object2[]) -> { 
            if (object1[0] != object2[0]){
                return object1[0] - object2[0];
            }
            return object1[1] - object2[1]; }
        );

        Stack<int[]> stack = new Stack<>();
        int[] popped;
        for (int[] interval : inputArray) {
            if (!stack.isEmpty()) {
                // Checking if interval at top of stack is overlapping with current interval
                if (stack.peek()[1] >= interval[0]) {
                    // Checking if interval at top of stack has ending point less than that of current interval
                    if (stack.peek()[1] < interval[1]) {
                        // Updating ending point of interval at top of stack with that of current interval
                        popped = stack.pop();
                        popped[1] = interval[1];
                        stack.push(popped);
                    }
                } else {      
                    // if not overlapping
                    stack.push(interval);
                }
            } else {        
                // if stack was empty i.e. it was the first interval
                stack.push(interval);
            }
        }

        int[][] outputArray = new int[stack.size()][2];
        int ptr = outputArray.length - 1;
        // Popping out all found non overlapping intervals
        while (!stack.isEmpty()) {
            popped = stack.pop();
            outputArray[ptr] = popped;
            ptr--;
        }
        return outputArray;
    }
    // -------------------- END ----------------------
}
    
class Solution{
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

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        int m = Integer.parseInt(bufferedReader.readLine().trim());

        int[][] inputArray = new int[n][m];

        for (int i = 0; i < n; i++) {
            String[] str = bufferedReader.readLine().split(" ");
            for(int j = 0; j < m; j++){
                inputArray[i][j] = Integer.parseInt(str[j].trim());
            }
        }

        int[][] res = Result.getMergedIntervals(inputArray);

        for (int i = 0; i < res.length; i++) {
            bufferedWriter.write(res[i][0]+" "+res[i][1]+"\n");
        }
        
        bufferedReader.close();
        bufferedWriter.close();
    }

}

/**
 * Time complexity: O(N*log(N))
 * Auxiliary Space complexity: O(N)
 */
'''
'''
OPTIMAL SOLUTION
/**
 * *********************** PROBLEM DESCRIPTION ***************************
 * Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which
 * should have only mutually exclusive intervals.
 * 
 * e.g. for this input: {{1,3}, {2,4}, {5,7}, {6,8} }.
 * The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}.
 * Similarly {5, 7} and {6, 8} should be merged and become {5, 8}.
 * 
 * Write a function which produces the set of merged intervals for the given set of intervals.
 */

import java.io.*;
import java.util.*;

class Result {

    // -------------------- START ----------------------

    static int[][] getMergedIntervals(int[][] inputArray) {
        // Sorting the input interval array by their starting points in increasing order
        Arrays.sort(inputArray, (int object1[], int object2[]) -> { 
            if (object1[0] != object2[0]){
                return object1[0] - object2[0];
            }
            return object1[1] - object2[1]; }
        );
        int last = 0;
        for (int i = 1; i < inputArray.length; i++) {
            // Checking if inputArray[last] and inputArray[i] are overlapping or not
            if (inputArray[last][1] >= inputArray[i][0]) {
                // If overlapping, then merge inputArray[i] into inputArray[last]
                // For merging them, it is sufficient to update only endpoint of inputArray[last] as 
                // it is guaranteed that inputArray[last][0]<=inputArray[i][0] , last<i
                inputArray[last][1] = Math.max(inputArray[last][1], inputArray[i][1]);
            } else {
                // inputArray[last] and inputArray[i] are found non-overlapping.
                // Moving on, inputArray[i] is the new interval under test of overlapping with following intervals.
                last++;
                inputArray[last] = inputArray[i];
            }
        }

        // From index 0 to last of inputArray will contain all non overlapping intervals
        return Arrays.copyOfRange(inputArray, 0, last+1);
    }

    // -------------------- END ----------------------
}

class Solution{
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
        int n = Integer.parseInt(bufferedReader.readLine().trim());
        int m = Integer.parseInt(bufferedReader.readLine().trim());

        int[][] inputArray = new int[n][m];

        for (int i = 0; i < n; i++) {
            String[] str = bufferedReader.readLine().split(" ");
            for(int j = 0; j < m; j++){
                inputArray[i][j] = Integer.parseInt(str[j].trim());
            }
        }

        int[][] res = Result.getMergedIntervals(inputArray);

        for (int i = 0; i < res.length; i++) {
            bufferedWriter.write(res[i][0]+" "+res[i][1]+"\n");
        }

        bufferedReader.close();
        bufferedWriter.close();
    }

}

/**
 * Time complexity: O(N*log(N))
 * Auxiliary Space complexity: O(1)
 */
'''
