import math
import os
import random
import re
import sys
'''
Implement Merge Sort
Problem Statement:
You are given an array of integers. You have to sort the array using merge sort algorithm.

Input/Output Format For The Function:
Input Format:
The function contains a single argument, an integer array arr.

Output Format:
Return the sorted integer array.

Input/Output Format For The Custom Input:
Input Format:

First line contains integer n, the number of integers. The next n lines contains an integer each.

If arr = [1,7,5,3] then input should be:
4
1
7
5
3

Output Format:
Output the sorted array of integers, with each integer in a new line.

For input arr = [1,7,5,3], output will be
1
3
5
7

Constraints:
1 <= n <= 10^5
-10^9 <= arr[i] <= 10^9 where 0<=i<=n-1

Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
4
0
1
3
2

Sample Output 1:
0
1
2
3

Explanation 1:
Here 3>2>1>0, so after applying merge sort algorithm, the resultant array becomes [0,1,2,3].

Sample Test Case 2:
Sample Input 2:
3
1000000000
199999999
0

Sample Output 2:
0
199999999
1000000000

Explanation 2:
Here, 1000000000>199999999>0, so after applying merge sort algorithm, the resultant array becomes
[0,199999999,1000000000].
'''
#
# Complete the 'merge_sort' function below.
#
# The function accepts an integer array as parameter.
#

def merge_sort(arr):
    # Write your code here
    pass

if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = merge_sort(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


'''
=== EDITORIAL ===
We have provided a solution which contains necessary comments to understand the approach used:
1) recursive_solution.java

Description:
We are given an input array of integers. Now we will implement merge sort algorithm to sort the integers in this array. 
Merge sort algorithm is a divide and conquer algorithm. Here, we partition the given array into subarrays, sort each of 
the subarrays separately and then merge these sorted subarrays to get the final resultant sorted array.
For more details, refer to the code given in recursive_solution.java.

Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*logn) where n denotes the length of array arr.
Here we keep on splitting the array into halves until we reach an array of size 1. For each of these subarrays, we sort 
them separately and merge them. Hence, after sorting and merging all the subarrays, the time complexity turns out to 
be O(n*logn).

Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) + Theta(n)
The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in case II of Master 
Method and solution of the recurrence is Theta(n*logn).
Time complexity of MergeSort is Theta(n*logn) in all 3 cases (worst, average and best) as merge sort always divides 
the array into two halves and take linear time to merge two halves.

Time Complexity:
O(n*logn) where n denotes the length of array arr.

As time complexity assuming that input arguments are already given and excluding time used in declaration of output 
is O(n*logn), to read input it will take O(n) and to store output it will take O(n) hence total complexity will be 
O(n*logn) + O(n) + O(n) → O(n*logn).

Auxiliary Space Used:
O(n) + O(logn)where n denotes the length of array arr.

Here, Merge Sort space complexity will always be O(n) with arrays. If you draw the space tree out, it will seem as 
though the space complexity is O(n*logn). However, as the code is a Depth First code, you will always only be expanding 
along one branch of the tree, therefore, the total space usage required will always be bounded by O(3n) = O(n). Apart 
from this, at each step, the size of the array gets halved, the depth of the tree would be at most O(logn). So 
considering functional stack space used for recursive calls the overall auxiliary space turns out to be O(n) + O(logn).

Space Complexity:
O(n) + O(logn) where n denotes the length of array arr.

The input array is of size n, so the input space complexity is O(n), and auxiliary space used is O(n) + O(logn) and 
output uses O(n), hence total complexity will be O(n) + O(logn) + O(n) + O(n) → O(n) + O(logn).
2) iterative_solution.java

Description:
We are given an input array of integers. Now the iterative approach of merge sort algorithm to sort given array. We 
start by dividing the array into blocks of size 1,2,4,8... and so on. For each of these blocks, we divide the array 
into corresponding subarrays of the size equal to block size and then sort them. Finally, we merge the sorted arrays 
and obtain the final sorted array. For more details, refer to the code given in iterative_solution.java.

Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*logn) where n denotes the length of array arr.

Here we iterate over block sizes starting from 1 and then move on in multiples of 2, that is, 2, 4, 8... and so on. 
For each of these block sizes, we take 2 consecutive subarrays of that size over the entire array. So for a block size 
of 1, there will be 2 subarrays of size 1 and we then sort them separately and merge them. We do this over the entire 
array n. So for each block size, we require O(n) time to sort the subarrays and merge them. Hence, after sorting and
 merging all the subarrays, for all the block sizes, 1,2,4,8,...,log2(n) the time complexity turns out to be O(n*logn).

Time Complexity:
O(n*logn) where n denotes the length of array arr.

As time complexity assuming that input arguments are already given and excluding time used in declaration of output is 
O(n*logn), to read input it will take O(n) and to store output it will take O(n) hence total complexity will be 
O(n*logn) + O(n) + O(n) → O(n*logn).

Auxiliary Space Used:
O(n*logn) where n denotes the length of array arr.

Here, for each and every subarray, we create a new array and copy the corresponding elements from the original array 
into this new array. So, total space complexity required is O(n*logn).
Space Complexity:
O(n*logn) where n denotes the length of array arr.
=== EDITORIAL ===
We have provided a solution which contains necessary comments to understand the approach used:
1) recursive_solution.java

Description:
We are given an input array of integers. Now we will implement merge sort algorithm to sort the integers in this array. 
Merge sort algorithm is a divide and conquer algorithm. Here, we partition the given array into subarrays, sort each of 
the subarrays separately and then merge these sorted subarrays to get the final resultant sorted array.
For more details, refer to the code given in recursive_solution.java.

Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*logn) where n denotes the length of array arr.
Here we keep on splitting the array into halves until we reach an array of size 1. For each of these subarrays, we sort 
them separately and merge them. Hence, after sorting and merging all the subarrays, the time complexity turns out to 
be O(n*logn).

Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) + Theta(n)
The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in case II of Master 
Method and solution of the recurrence is Theta(n*logn).
Time complexity of MergeSort is Theta(n*logn) in all 3 cases (worst, average and best) as merge sort always divides 
the array into two halves and take linear time to merge two halves.

Time Complexity:
O(n*logn) where n denotes the length of array arr.

As time complexity assuming that input arguments are already given and excluding time used in declaration of output 
is O(n*logn), to read input it will take O(n) and to store output it will take O(n) hence total complexity will be 
O(n*logn) + O(n) + O(n) → O(n*logn).

Auxiliary Space Used:
O(n) + O(logn)where n denotes the length of array arr.

Here, Merge Sort space complexity will always be O(n) with arrays. If you draw the space tree out, it will seem as 
though the space complexity is O(n*logn). However, as the code is a Depth First code, you will always only be expanding 
along one branch of the tree, therefore, the total space usage required will always be bounded by O(3n) = O(n). Apart 
from this, at each step, the size of the array gets halved, the depth of the tree would be at most O(logn). So 
considering functional stack space used for recursive calls the overall auxiliary space turns out to be O(n) + O(logn).

Space Complexity:
O(n) + O(logn) where n denotes the length of array arr.

The input array is of size n, so the input space complexity is O(n), and auxiliary space used is O(n) + O(logn) and 
output uses O(n), hence total complexity will be O(n) + O(logn) + O(n) + O(n) → O(n) + O(logn).
2) iterative_solution.java

Description:
We are given an input array of integers. Now the iterative approach of merge sort algorithm to sort given array. We 
start by dividing the array into blocks of size 1,2,4,8... and so on. For each of these blocks, we divide the array 
into corresponding subarrays of the size equal to block size and then sort them. Finally, we merge the sorted arrays 
and obtain the final sorted array. For more details, refer to the code given in iterative_solution.java.

Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n*logn) where n denotes the length of array arr.

Here we iterate over block sizes starting from 1 and then move on in multiples of 2, that is, 2, 4, 8... and so on. 
For each of these block sizes, we take 2 consecutive subarrays of that size over the entire array. So for a block size 
of 1, there will be 2 subarrays of size 1 and we then sort them separately and merge them. We do this over the entire 
array n. So for each block size, we require O(n) time to sort the subarrays and merge them. Hence, after sorting and
 merging all the subarrays, for all the block sizes, 1,2,4,8,...,log2(n) the time complexity turns out to be O(n*logn).

Time Complexity:
O(n*logn) where n denotes the length of array arr.

As time complexity assuming that input arguments are already given and excluding time used in declaration of output is 
O(n*logn), to read input it will take O(n) and to store output it will take O(n) hence total complexity will be 
O(n*logn) + O(n) + O(n) → O(n*logn).

Auxiliary Space Used:
O(n*logn) where n denotes the length of array arr.

Here, for each and every subarray, we create a new array and copy the corresponding elements from the original array 
into this new array. So, total space complexity required is O(n*logn).
Space Complexity:
O(n*logn) where n denotes the length of array arr.

The input array is of size n, so the input space complexity is O(n), and auxiliary space used is O(n*logn) and output 
uses O(n), hence total complexity will be O(n*logn) + O(n) + O(n) → O(n*logn).

Additional Material
QuickSort vs MergeSort:
Quicksort is an in-place sorting algorithm, that is, it does not require any extra space to perform sorting of an 
array. On the other hand, merge sort requires O(n*logn) auxiliary space. However, the worst-case time complexity of 
quicksort is O(n^2) because the time complexity depends on the selection of pivot. On the other hand, for mergesort, 
the worst-case time complexity is always O(n*logn).

Merge Sort vs Quick sort for arrays and arraylist:

https://www.geeksforgeeks.org/why-quick-sort-preferred-for-arrays-and-merge-sort-for-linked-lists/




The input array is of size n, so the input space complexity is O(n), and auxiliary space used is O(n*logn) and output 
uses O(n), hence total complexity will be O(n*logn) + O(n) + O(n) → O(n*logn).

Additional Material
QuickSort vs MergeSort:
Quicksort is an in-place sorting algorithm, that is, it does not require any extra space to perform sorting of an 
array. On the other hand, merge sort requires O(n*logn) auxiliary space. However, the worst-case time complexity of 
quicksort is O(n^2) because the time complexity depends on the selection of pivot. On the other hand, for mergesort, 
the worst-case time complexity is always O(n*logn).

Merge Sort vs Quick sort for arrays and arraylist:
https://www.geeksforgeeks.org/why-quick-sort-preferred-for-arrays-and-merge-sort-for-linked-lists/

'''

'''
// ITERATIVE SOLUTION
import java.io.*;
import java.lang.reflect.Member;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;
 
class Result {

    /*-------------------START----------------------*/
    public static List<Integer> merge_sort(List<Integer> arr) {
        int n = arr.size();
        int left = 0, right = n-1;
        split(arr, left, right);
        return arr;
    }

    public static void split(List<Integer> arr, int l, int h) {
        // divide the array into blocks of size [1,2,4,8,..]
        for (int blocks = 1; blocks <= h - l; blocks = 2 * blocks) {
            // for blocks = 1, i = 0, 2, 4, 6, 8 and so on
            // for each block we split the array into sub arrays and merge them
            /* note that each of these subarrays will always be sorted as we are
             building the array from smaller subarrays to larger subarrays*/
            for (int i = l; i < h; i += 2 * blocks) {
                int left = i;
                int mid = Math.min(i + blocks - 1, h);
                int right = Math.min(i + 2 * blocks - 1, h);
                merge(arr, left, mid, right);
            }
        }
    }

    /*function to merge 2 sorted arrays*/
    public static void merge(List<Integer> arr, int left, int mid, int right) {
        int[] l = new int[mid - left + 1];
        //copies the integers to array l from arr
        for(int i = 0; i< mid - left + 1; i++) {
            l[i] = arr.get(left + i);
        }
        int[] r = new int[right - mid];
        //copies the integers to array r from arr
        for(int i = 0; i< right - mid; i++) {
            r[i] = arr.get(mid + i + 1);
        }
        int i = 0, j = 0, k = left;
        //merges arrays l and r back to arr
        while(i<l.length && j<r.length) {
            if(l[i]<r[j]) {
                arr.set(k,l[i]);
                i++; 
            }
            else {
                arr.set(k,r[j]); 
                j++;
            }
            k++;
        }
        //merges remaining elements of arrays l and r
        while(i<l.length) {
            arr.set(k++,l[i++]);
        }
        while(j<r.length) {
            arr.set(k++,r[j++]);
        }
    }
    /*-------------------END----------------------*/

}

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        }).map(String::trim).map(Integer::parseInt).collect(toList());

        List<Integer> result = Result.merge_sort(arr);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedWriter.close();
        bufferedReader.close();
    }
}
'''

'''
// Recursive Solution
import java.io.*;
import java.lang.reflect.Member;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;
 
class Result {

    /*-------------------START----------------------*/
    public static List<Integer> merge_sort(List<Integer> arr) {
        int n = arr.size();
        int left = 0, right = n-1;
        split(arr, left, right);
        return arr;
    }
    
    /*function to partition the array into subarrays and then merge them*/
    public static void split(List<Integer> arr, int left, int right) {
        if(left<right) { 
            int mid = (left+right)/2;
            //sort first and second halves of the array
            split(arr, left, mid);
            split(arr, mid+1, right);
            //merge the sorted halves
            merge(arr, left, mid, right);
        }
    }

    /*function to merge 2 sorted arrays*/
    public static void merge(List<Integer> arr, int left, int mid, int right) {
        int[] l = new int[mid - left + 1];
        //copies the integers to array l from arr
        for(int i = 0; i< mid - left + 1; i++) {
            l[i] = arr.get(left + i);
        }
        int[] r = new int[right - mid];
        //copies the integers to array r from arr
        for(int i = 0; i< right - mid; i++) {
            r[i] = arr.get(mid + i + 1);
        }
        int i = 0, j = 0, k = left;
        //merges arrays l and r back to arr
        while(i<l.length && j<r.length) {
            if(l[i]<r[j]) {
                arr.set(k,l[i]);
                i++; 
            }
            else {
                arr.set(k,r[j]); 
                j++;
            }
            k++;
        }
        //merges remaining elements of arrays l and r
        while(i<l.length) {
            arr.set(k++,l[i++]);
        }
        while(j<r.length) {
            arr.set(k++,r[j++]);
        }
    }
    /*-------------------END----------------------*/

}

class Solution {
    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine().replaceAll("\\s+$", "");
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        }).map(String::trim).map(Integer::parseInt).collect(toList());

        List<Integer> result = Result.merge_sort(arr);

        bufferedWriter.write(
            result.stream()
                .map(Object::toString)
                .collect(joining("\n"))
            + "\n"
        );

        bufferedWriter.close();
        bufferedReader.close();
    }
}
'''
