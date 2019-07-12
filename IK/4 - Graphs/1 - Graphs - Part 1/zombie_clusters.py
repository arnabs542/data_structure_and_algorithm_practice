'''
Zombie Clusters
Problem Statement:
There are zombies in Seattle. Liv and Ravi are trying to track them down to find out who is creating new zombies in an effort
 to prevent an apocalypse. Other than the patient-zero zombies (who became so by mixing MaxRager and tainted Utopium), new
 people only become zombies after being scratched by an existing zombie. Zombiism is transitive. This means that if zombie
 0 knows zombie 1 and zombie 1 knows zombie 2, then zombie 0 is connected to zombie 2 by way of knowing zombie 1. A zombie
 cluster is a group of zombies who are directly or indirectly linked through the other zombies they know, such as the one
 who scratched them or supplies who them with brains.
We have a 2D array having n rows and n columns where each cell, zombies[A][B], denotes whether zombie A knows zombie B.
 The diagram showing connectedness will be made up of a number of binary strings, characters 0 or 1. Each of the characters
 in the string represents whether the zombie associated with a row element is connected to the zombie at that character's
 index. For instance, a zombie 0 with a connectedness string '110' is connected to zombies 0 (itself) and zombie 1, but
 not to zombie 2. The complete matrix of zombie connectedness is:
110
110
001
Zombies 0 and 1 are connected. Zombie 2 is not.
Your task is to determine the number of connected groups of zombies, or clusters, in a given matrix.
NOTE: Method signatures may vary depending on the requirements of your chosen language.
Input/Output Format For The Function:
Input Format:
The function contains a single argument, a String array zombies.
Output Format:
Return an integer, the number of zombie clusters.
Input/Output Format For The Custom Input:
Input Format:
The first line contains integer n, the number of Strings. The next n lines contain a String each.
If arr = {“110”,”110”,”001”} then the input should be:
3
110
110
001
Output Format:
Output the number of zombie clusters in a single line.
For the above input, the output would be
2
Constraints:
1 <= n <= 1000 where n denotes length of zombies array.
Each zombies[i] is a binary string (Characters are either 0 or 1)
 of length n for 0 <= i < n.
Sample Test Cases:
Sample Test Case 1:
Sample Input 1:
4
1100
1110
0110
0001
Sample Output 1:
2
Explanation 1:
https://i.imgur.com/tKnENxg.png

We have n = 4 zombies numbered z0 through z3. There are 2 pairs of zombies who directly know each another: (z0, z1) and
 (z1, z2). Because of zombiism's transitive property, the set of zombies {z0, z1, z2} is considered to be a single zombie
 cluster. The remaining zombie, z3, doesn't know any other zombies and is considered to be his own, separate zombie cluster
 ({z3}). This gives us a total of 2 zombie clusters.
Sample Test Case 2:
Sample Input 2:
5
10000
01000
00100
00010
00001
Sample Output 2:
5
Explanation 2:
https://i.imgur.com/d0pt6hP.png

Each zombie forms its own zombie cluster: {z0}, {z1}, {z2}, {z3}, and {z4}. This means we have 5 zombie clusters.
'''

import math
import os
import random
import re
import sys

sys.setrecursionlimit(1000007)

# Complete the zombieCluster function below.
def zombieCluster(zombies):
    pass



if __name__ == "__main__":
    fptr = sys.stdout
    n = int(input())
    zombies = []
    for _ in range(n):
        zombies_item = input()
        zombies.append(zombies_item)
    res = zombieCluster(zombies)
    fptr.write(str(res) + '\n')
    fptr.close()

'''
We have provided a solution and the solutions contains necessary comments to understand the approach used:
1) solution.java
Description:
We have a 2D array having n rows and n columns where each cell, zombies[A][B], denotes whether zombie A knows zombie B.

We will use depth first search (dfs) traversal to solve this problem.
This type of 2D array is known as an adjacency matrix
 in graph theory, where each cell having value 1 denotes an edge between 2 vertices.
So, now we start iterating over zombies
 from 0 to n - 1 and for each of the zombies which hasn’t been visited yet, we perform a dfs traversal.
Each zombie that
 occurs in some dfs traversal gets marked as visited. So that we don’t perform dfs from that zombie as it already belongs
 to one of the clusters.
Finally, we count how many zombies weren’t visited and for who we had to perform the dfs.
This
 is the number of zombie clusters.
NOTE: Refer this link for more information on depth first search (dfs).
https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/  (recursive)
https://www.geeksforgeeks.org/iterative-depth-first-traversal/
 (iterative)
Example:
Consider the following input:
3
1 1 0
1 1 0
0 0 1
Here, we see that zombie 0 is connected to zombie 1 and zombie 1 is connected to zombie 0. zombie 2 is not connected to
 any other zombie. So we start iterating over the zombies and if the zombie isn’t visited yet, we start dfs from that zombie.
 So when we start iterating, we see that the first zombie isn’t visited yet. We start dfs from that zombie. So in this dfs,
 we will visit both zombie 0 and zombie 1. So this forms the first zombie cluster. Now we will start dfs from zombie 2.
 This forms the second zombie cluster. So the total number of zombie clusters are 2, which we return as the answer.
Time Complexity (assuming that input arguments are already given and excluding time used in declaration of output):
O(n^2) considering the number of zombies are n.
For each unvisited zombie we perform depth first search starting from that zombie. We check whether this zombie is connected
 to any of the other zombies. This take O(n) time. We do the same for all n vertices, so total time complexity is O(n^2).

Time Complexity:
O(n^2) considering the number of zombies are n.
As time complexity assuming that input arguments are already given and excluding time used in declaration of output is O(n^2),
 to read input it will take O(n^2) and to store output it will take O(1) hence total complexity will be O(n^2) + O(n^2)
 + O(1) → O(n^2).
Auxiliary Space Used:
O(n) considering the number of zombies are n.
We create an array of size n to keep a check of whether a zombie is visited or not. Apart from this, dfs is a recursive
 function and it uses at most O(n) stack space as the maximum number of zombies in a cluster is n. So overall auxiliary
 space used is O(n).
Space Complexity:
O(n^2) considering the number of zombies are n.
Input complexity is O(n^2), auxiliary space used is O(n), and output space complexity is O(1), hence total complexity will
 be O(n^2).
'''
'''
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
    // --------------------------------START-------------------------------
    static int zombieCluster(List<String> zombies){
        int ans = 0, n = zombies.size();
        //an array to check if the following zombie has been visited in dfs
        boolean visited[] = new boolean[n];
        //we perform dfs for any zombie who has not been visited yet
        for(int i = 0;i < n; i++){
            /*if the zombie hasn't be visited, it will form a new cluster
            so we increase the count of number of zombie clusters.*/
            if(!visited[i]){
                ans++;
                dfs(i, n, zombies, visited);
            }
        }
        return ans;
    }
    //simple depth first search function
    static void dfs(int x, int n, List<String> zombies, boolean[] visited){
        //mark current zombie as visited
        visited[x] = true;
        //for all the zombies connected to the current zombie, we perform dfs.
        for(int i = 0; i<n; i++){
            if(zombies.get(x).charAt(i) == '1' && !visited[i]){
                dfs(i, n, zombies, visited);
            }
        }
        return;
    }
    // --------------------------------END-------------------------------
}

class solution {
    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int zombiesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> zombies = IntStream.range(0, zombiesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        int result = Result.zombieCluster(zombies);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        bufferedReader.close();
    }
}
'''

