'''
Detect cycle in Directed Graph
Problem Statement:
You are given Directed Graph G. You need to find out whether at least one cycle exist in the graph or not.
Input Format:
Three arguments for function, N, M and 2D Array of size M*2 where N denotes number of vertices and M denotes number of directed
 edges and 2D array of size M*2 represent M directed edges.
For array of size M*2, each row will represent directed edge, where value in column 1 and column 2 will be index (0-based)
 of starting vertex and ending vertex respectively of that directed edge.
Output Format:
Return boolean true if at least one cycle exist in graph else boolean false.
Constraints:
2 <= N <= 100000
1 <= M <= 100000
Indexing of vertices starting from 0.
No multiple edges i.e. if an edge is present which is directed from vertex u to vertex v, then no other edge will present
 which is directed from vertex u to vertex v.
Graph can have multiple components.
Sample Test Case:
Sample Input:
N = 5, M = 7, edges = [[0,1],[0,3],[1,3],[1,2],[2,3],[4,0],[2,4]]
Sample Output:
true
Explanation:
Graph formed from 5 vertices and given 7 directed edges have 1 cycle (0 --> 1 --> 2 --> 4 --> 0) So, Output will be true.
'''
import math
import os
import random
import re
import sys

sys.setrecursionlimit(100007)

# Complete the 'hasCycle' function below.
#
# The function accepts INTEGER N, INTEGER M and 2D_INTEGER_ARRAY edges as parameter.
# The function is expected to return a BOOLEAN.
#

def hasCycle(N, M, edges):
    pass



if __name__ == "__main__":
    N = int(input().strip())
    M = int(input().strip())

    edges = []

    for _ in range(M):
        edges.append(list(map(int, input().rstrip().split())))

    fptr = sys.stdout

    result = hasCycle(N, M, edges)

    fptr.write(str(int(result)) + '\n')

    fptr.close()


'''
We have provided solution which contain necessary comments to understand the approach used:
1) optimal_solution.java
Time Complexity:
O(N + M) where N is number of vertices and M is number of edges.
For this solution, we used DFS (Depth First Traversal). DFS is used to traverse graph and detect cycle in graph. Traversing
 graph using DFS will produces a tree. We need to find out if any cycle is present in the graph or not? So, condition for
 cycle to be present in graph will be if any edge is from node to one of its ancestor in the tree produced by DFS, this
 type of edge is called back edge.
We are iterating over all the unvisited nodes because if
1. Graph is disconnected means graph have more than one component
2. From the vertex we are starting DFS considering that node as root and not able to reach all other vertices due to no
 valid path.
So, We are checking for back edges in all the components of graph.
How to detect a back edge ..?
We can keep track of vertices which are currently present in the recursion stack of DFS function that is hasCycleUtil().
 If we are able to reach a vertex which is already present in recursion stack then we can declare that there is cycle in
 the graph and that edge which is connecting the current vertex to the ancestor vertex (vertex in recursion stack) is a
 back edge.
We have used visited set to maintain visited vertices and is_in_stack set to maintain vertices present in recursion stack.

Auxiliary Space Used:
O(N + M).
As we are using two hashsets, One to maintain elements of stack and other to maintain visited vertices and also we are maintaining
 adjacency list for edges.  
Space Complexity:
O(N + M).
Input is O(M) because we are storing m edges and each edge occupies O(1) space and auxiliary space used is O(N + M). So,
 O(M) + O(N + M) -> O(N + M).
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

    /*
     * Complete the 'hasCycle' function below.
     *
     * The function accepts INTEGER N, INTEGER M and 2D_INTEGER_ARRAY edges as parameter.
     */


    // ============================ Start ============================
    

    public static boolean hasCycle(int N, int M, List<List<Integer>> edges) {
        ArrayList<Integer> adjacency[] = new ArrayList[N];
        // To store adjacency matrix of graph

        for (int var = 0; var < N; var++) {
            adjacency[var] = new ArrayList<Integer>();
        }

        for (int var = 0; var < M; var++) {
            int u = edges.get(var).get(0), v = edges.get(var).get(1);
            adjacency[u].add(v);
        }
        boolean visited[] = new boolean[N];
        boolean is_in_stack[] = new boolean[N];
        for (int var = 0; var < N; var++) {
            if(hasCycleUtil(var, adjacency, visited, is_in_stack)) {
                return true;
            }
        }
        return false;
    }


    public static boolean hasCycleUtil(int cur_vertex, ArrayList<Integer> adj[],
       	boolean visited[], boolean is_in_stack[]) {
        
        // If back edge present then return true
        if (is_in_stack[cur_vertex])
            return true;

        // If cur_vertex is already visited then return false, 
        // no need to apply logic as it has been already applied
        if (visited[cur_vertex])
            return false;

        // Mark the current node as visited and
        // part of recursion stack
        visited[cur_vertex]=true;
        is_in_stack[cur_vertex]=true;

        // Recur for all the vertices adjacent to this vertex
        for (int v: adj[cur_vertex])
            if (hasCycleUtil(v, adj, visited, is_in_stack))
                return true;

        // remove the vertex from recursion stack
        is_in_stack[cur_vertex]=false;

        return false;

	}
}


// ============================ End =============================


class Solution {
    public static void main(String args[]) {
        /*
        This function is used to increase the size of recurison stack. 
        It makes the size of stack 2^26 ~= 10^8
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

        int N = Integer.parseInt(bufferedReader.readLine().trim());// N = Number of vertices
        int M = Integer.parseInt(bufferedReader.readLine().trim());// M = Number of directed edges

        List<List<Integer>> edges = new ArrayList<>();// To store directed edges

        IntStream.range(0, M).forEach(i -> {
            try {
                edges.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });
        bufferedReader.close();

        boolean result = Result.hasCycle(N,M, edges);

        bufferedWriter.write(result);
        bufferedWriter.newLine();
        bufferedWriter.close();
    }
}
'''

