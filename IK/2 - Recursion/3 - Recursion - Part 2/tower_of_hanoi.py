'''
Tower Of Hanoi
Problem Statement:
Tower of Hanoi is a mathematical puzzle where we have three pegs and n disks. The objective of the puzzle is to move
the entire stack to another peg, obeying the following simple rules:
Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk
can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.

Here, we are given n denoting the number of disks in the first peg, we need to return all the steps taken to move all
disks from the first peg to the third peg.
There can be multiple possibilities to complete the given objective. Every valid possibility to achieve objective will
be a valid answer.
Input/Output Format For The Function:
Input Format:
There is only one argument in the input, an integer named n denoting the number of disks in the first peg.
Output Format:
Return a 2d integer array denoting steps taken to move disks from the first peg to the third peg. Each row will have
two integers denoting from peg and to peg, for example, if the ith row is [2, 3], then it means in this step, we
moved top disk on peg 2 to peg 3.

For input n = 4, the output will be a 2d array result = [ [1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2],
[1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3] ]
Input/Output Format For The Custom Input:
Input Format:
There should be one line for input, containing a single integer n, denoting the number of disks in the first peg.

If n = 4 then input should be:
4
Output Format:
There will be a 2d array of integers, where ith row of result 2d array will denote ith step taken to reach the
objective. Each row will have two integers denoting from peg and to peg, for example, if the ith row is "2 3" then it
means, in this step, we moved top disk on peg 2 to peg 3.
For input n = 4, the output will be as follows:
1 2
1 3
2 3
1 2
3 1
3 2
1 2
1 3
2 3
2 1
3 1
2 3
1 2
1 3
2 3

Constraints:
1 <= n <= 20

Sample Test Case:
Input:
n = 4

Output:
[ [1, 2], [1, 3], [2, 3], [1, 2], [3, 1], [3, 2], [1, 2], [1, 3], [2, 3], [2, 1], [3, 1], [2, 3], [1, 2], [1, 3], [2, 3] ]

Explaination:
Following steps:
[1, 2] = Shift top disk of the first peg to top of the second peg.
Picture after this step will be:
First peg: 2 3 4
Second peg: 1
Third peg: Empty

[1, 3] = Shift top disk of the first peg to top of the third peg.
Picture after this step will be:
First peg: 3 4
Second peg: 1
Third peg: 2

Similarly after following remaining steps will find that the final configuration will be
First peg: Empty
Second peg: Empty
Third peg: 1 2 3 4

which is our objective.
'''

#
# Complete the 'tower_of_hanoi' function below.
#
# The function accepts INTEGER as parameter.
# Return 2D INTEGER ARRAY.
#
#!/bin/python3

import math
import os
import random
import re
import sys
sys.setrecursionlimit(1000100)


def tower_of_hanoi(n):
    pass


if __name__ == '__main__':
    n = int(input().strip())

    fptr = sys.stdout

    result = tower_of_hanoi(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

'''
We have provided a solution and the solutions contain necessary comments to understand the approach used:
1) recursive_solution.java
Description:
Let's take an example of 2 disks.

Let peg 1 = 'A', peg 2 = 'B', peg 3 = 'C'.
Step 1: Shift the first disk from 'A' to 'B'.
Step 2: Shift the second disk from 'A' to 'C'.
Step 3: Shift the first disk from 'B' to 'C'.

The pattern here is :
Shift 'n-1' disks from 'A' to 'B'.
Shift the last disk from 'A' to 'C'.
Shift 'n-1' disks from 'B' to 'C'.

Image illustration for 3 disks:

For 2 disks, 3 steps required.
For 3 disks, 7 steps required.
Similarly, for n disks, steps required will be 2^n-1.

Source of images: https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

Time Complexity:
O(2^n) where n denotes the given number of disks in the first peg.

Recurrence relation is:
T(n) = 2 * T(n - 1) + O(1)

Which is O(2^n).

Auxiliary Space Used:
O(2^n) where n denotes the given number of disks in the first peg.

As there are O(2^n) steps in the output. And space used by function call stack will be O(n), because of the 
recursive calls. So, O(2^n) + O(n) = O(2^n).

Space Complexity:
O(2^n) where n denotes the given number of disks in the first peg.

Input is O(1).
Auxiliary space is O(2^n).
So, O(1) + O(2^n) → O(2^n).

2) iterative_solution.java
Description:
[Iterative solution is not that imp for interviews. It is based on observation.]

This approach is the iterative approach. To achieve our objective of shifting disks from the first peg to the third 
peg, we will follow steps:
Calculate the total number of moves required i.e. "pow(2, n) - 1" where n is the number of disks.
If the number of disks (i.e. n) is even then interchange destination peg and auxiliary peg.
for i = 1 to the total number of moves:
if i%3 == 1:
legal movement of the top disk between source peg and destination peg

if i%3 == 2:
legal movement top disk between source peg and the auxiliary peg

if i%3 == 0:
legal movement top disk between the auxiliary peg and destination peg
Let us understand with a simple example with 3 disks:
So, the total number of moves required = 7
        S              A D

When i = 1, (i % 3 == 1) legal movement between ‘S’ and ‘D’

When i = 2,  (i % 3 == 2) legal movement between ‘S’ and ‘A’

When i = 3, (i % 3 == 0) legal movement between ‘A’ and ‘D’.

When i = 4, (i % 4 == 1) legal movement between ‘S’ and ‘D’.

When i = 5, (i % 5 == 2) legal movement between ‘S’ and ‘A’.

When i = 6, (i % 6 == 0) legal movement between ‘A’ and ‘D’.

When i = 7, (i % 7 == 1) legal movement between ‘S’ and ‘D’.

So, after all these, destination peg contains all the in order of size.

Now, Only one question is unanswered, Why we interchanging destination peg and auxiliary peg if the number of disks 
is even.
For this, let's take an example of the number of disks n = 2 and apply our above-discussed approach without 
interchanging destination and auxiliary peg.
Total number of moves required will be 2^2-1 = 3

Initially:
S = 1 2
A = Empty
D = Empty

When i = 1, (i % 3 == 1) legal movement between ‘S’ and ‘D’
S = 2
A = Empty
D = 1

When i = 2, (i % 3 == 1) legal movement between ‘S’ and ‘A’
S = Empty
A = 2
D = 1

When i = 3, (i % 3 == 0) legal movement between ‘A’ and ‘D’
S = Empty
A = 1 2
D = Empty

Here, we can see that after applying our discussed approach of 3 moves without interchanging auxiliary and destination 
peg, we end up moving disks from peg S to A instead of S to D. We can see this similar pattern if the number of disks 
is even. Hence to complete our objective of moving disks from peg S to D in the minimum number of moves, we simply 
interchange A (auxiliary peg) and D (Destination peg) if the number of disks is even.
After observing above iterations, we can think that after a disk other than the smallest disk is moved, the next disk 
to be moved must be the smallest disk because it is the top disk resting on the spare peg and there are no other 
choices to move a disk.
Source of images:
https://www.geeksforgeeks.org/iterative-tower-of-hanoi/

Time Complexity:
O(2^n) where n denotes the given number of disks in the first peg.

Recurrence relation is:
T(n) = 2 * T(n - 1) + O(1)

Which is O(2^n).
Auxiliary Space Used:
O(2^n) where n denotes the given number of disks in the first peg.

As there are O(2^n) steps in the output. And we are maintaining three stacks representing three pegs, the maximum 
number of disks will be n in any stack hence it will take O(n) to store three stacks. So, O(2^n) + O(n) = O(2^n).
Space Complexity:
O(2^n) where n denotes the given number of disks in the first peg.

Input is O(1).
Auxiliary space is O(2^n).
So, O(1) + O(2^n) → O(2^n).
'''
'''
ITERATIVE JAVA SOLUTION
import java.io.*;
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
    //----------------------------START--------------------------------
    /*
    * Complete the 'tower_of_hanoi' function below.
    *
    * The function accepts INTEGER as parameter.
    * Return 2D INTEGER ARRAY.
    */
    public static List<List<Integer>> tower_of_hanoi(int n) {
        // Stacks representing pegs
        Stack<Integer> src = new Stack<Integer>(), dest=new Stack<Integer>(), 
            aux=new Stack<Integer>();
        List<List<Integer>> answer = new ArrayList<>();

        int i, total_num_of_moves;
        int from_peg=1, aux_peg=2, to_peg=3; 
       
        // If number of disks is even, then interchange 
        // destination pole and auxiliary pole 
        if (n % 2 == 0) {
            int temp = to_peg; 
            to_peg = aux_peg; 
            aux_peg  = temp; 
        } 
        // Total number of moves will be 2^n - 1.
        total_num_of_moves = (int) (Math.pow(2, n) - 1); 
       
        // Larger disks will be pushed first 
        for (i = n; i >= 1; i--) {
            src.push(i);
        }
       
        for (i = 1; i <= total_num_of_moves; i++) {
            if (i % 3 == 1) {
                // In every first step, move disk from src peg to dest peg
                move_disks_between_two_pegs(src, dest, from_peg, to_peg, answer);
            }
       
            else if (i % 3 == 2) {
                // In every second step, move disk from src peg to aux peg
                move_disks_between_two_pegs(src, aux, from_peg, aux_peg, answer);
            }
       
            else if (i % 3 == 0) {
                // In every third step, move disk from aux peg to dest peg
                move_disks_between_two_pegs(aux, dest, aux_peg, to_peg, answer);
            }
        }
        // Return final answer containing steps to follow to reach our objective of moving
        // all disks from src peg to dest peg.
        return answer;
    }
    // Function to implement legal movement between two pegs 
    public static void move_disks_between_two_pegs(Stack src, Stack dest, int from_peg,
        int to_peg, List<List<Integer>> answer) {

        int peg_1_top_disk = !src.isEmpty() ? (int) src.pop() : Integer.MIN_VALUE; 
        int peg_2_top_disk = !dest.isEmpty() ? (int) dest.pop() : Integer.MIN_VALUE; 
  
        // When peg 1 is empty 
        if (peg_1_top_disk == Integer.MIN_VALUE) {
            src.push(peg_2_top_disk);
            add_step_in_result(to_peg, from_peg, answer); 
        } 
        // When peg 2 is empty 
        else if (peg_2_top_disk == Integer.MIN_VALUE) {
            dest.push(peg_1_top_disk);
            add_step_in_result(from_peg, to_peg, answer); 
        } 
        // When top disk of peg 1 > top disk of peg 2 
        else if (peg_1_top_disk > peg_2_top_disk) {
            src.push(peg_1_top_disk);
            src.push(peg_2_top_disk);
            add_step_in_result(to_peg, from_peg, answer); 
        } 
        // When top disk of peg 1 < top disk of peg 2 
        else {
            dest.push(peg_2_top_disk);
            dest.push(peg_1_top_disk);
            add_step_in_result(from_peg, to_peg, answer); 
        }
    }
      
    // Function to add the step of disks to our final answer list
    public static void add_step_in_result(int from_peg, int to_peg,
        List<List<Integer>> answer) {

        List<Integer> temp = new ArrayList<Integer>();
        temp.add(from_peg);
        temp.add(to_peg);
        answer.add(temp);
    }
    //-----------------------------END---------------------------------
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
        List<List<Integer>> result = Result.tower_of_hanoi(n);

        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            });

        bufferedWriter.close();
        bufferedReader.close();
    }

}
'''
'''
RECURSIVE JAVA SOLTION
import java.io.*;
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
    //----------------------------START--------------------------------
    /*
    * Complete the 'tower_of_hanoi' function below.
    *
    * The function accepts INTEGER as parameter.
    * Return 2D INTEGER ARRAY.
    */
    public static List<List<Integer>> tower_of_hanoi(int n) {
        // Write your code here 
        List<List<Integer>> answer = new ArrayList<>();
        tower_of_hanoi_util(n, 1, 3, 2, answer);
        return answer;
    }

    public static void tower_of_hanoi_util(int n, int from_peg,
        int to_peg, int aux_peg, List<List<Integer>> answer) {

        // If reached at condition when n equal to one.
        if (n == 1) {
            // As it is last disk we shift it from from_peg to to_peg
            List<Integer> temp = new ArrayList<Integer>();
            temp.add(from_peg);
            temp.add(to_peg);
            answer.add(temp);
            return;
        }
        // Call the function to shift top n - 1 disks from from_peg to
        // aux_peg using to_peg.
        tower_of_hanoi_util(n-1, from_peg, aux_peg, to_peg, answer);

        // Store the step of moving of 1 top disk from from_peg to to_peg
        List<Integer> temp = new ArrayList<Integer>();
        temp.add(from_peg);
        temp.add(to_peg);
        answer.add(temp);

        // Shifting back remanining n-1 disks from aux_peg to to_peg using from_peg
        tower_of_hanoi_util(n-1, aux_peg, to_peg, from_peg, answer);
    }
    //-----------------------------END---------------------------------
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
        List<List<Integer>> result = Result.tower_of_hanoi(n);

        result.stream()
            .map(
                r -> r.stream()
                    .map(Object::toString)
                    .collect(joining(" "))
            )
            .map(r -> r + "\n")
            .collect(toList())
            .forEach(e -> {
                try {
                    bufferedWriter.write(e);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            });

        bufferedWriter.close();
        bufferedReader.close();
    }

}
'''
