'''
Shortest Distance From the Guard
Problem Statement:
You are given a 2D character grid of size n * m. Each element of the grid is either a GUARD, an OPEN space or a WALL. Every
 GUARD can move up, down, left and right in the open space. They cannot move on the wall.
Find, for every cell, the distance from the nearest guard cell. Consider -1 as this distance for WALL cells and unreachable
 cells.
Input/Output Format For The Function:
Input Format:
You will be given a string array rowStr of size n, where each string rowStr[i] is of length m. rowStr represents the grid.
 Each character in the grid will be G, O or W.
G - Guard
O - Open space
W - Wall
Output Format:
Return 2D integer array resArr, of size n * m, where resArr[i][j] representing the distance from a cell in the ith row and
 jth column to its nearest guard.
Put -1 in case of wall cells and unreachable cells.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting no. of rows in input grid, which is also a size of array rowStr.

The second line of input should contain an integer m, denoting no. of columns in input grid.
In next n lines, the ith line should contain a string rowStr[i], denoting value at index i of rowStr.
If n = 5, m = 5 and rowStr = [“OOOOG”, “OWWOO”, “OOOWO”, “GWWWO”, “OOOOG”], then the input should be:
5
5
OOOOG
OWWOO
OOOWO
GWWWO
OOOOG
Output Format:
Output 2D array of integers resArr will be of same size of given 2D array i.e. n * m.
There will be n lines of output, where the ith line contains m space separated integers. So, jth integer in ith line is
 value resArr[i][j], denoting value at index (i, j) of resArr.
For input n = 5, m = 5 and rowStr = [“OOOOG”, “OWWOO”, “OOOWO”, “GWWWO”, “OOOOG”], output will be:
3 3 2 1 0
2 -1 -1 2 1
1 2 3 -1 2
0 -1 -1 -1 1
1 2 2 1 0
Constraints:
1 <= n, m <= 10^3
Sample Test Case:
Sample Test Case 1:
Sample Input 1:
5
5
OOOOG
OWWOO
OOOWO
GWWWO
OOOOG
Sample Output 1:
3 3 2 1 0
2 -1 -1 2 1
1 2 3 -1 2
0 -1 -1 -1 1
1 2 2 1 0
Explanation 1:
All the walls are -1. All other cells have the minimum distance to a Guard.
Sample Test Case 2:
Sample Input 2:
1
5
GWOWG
Sample Output 2:
0 -1 -1 -1 0
Explanation 2:
Open space in the middle is unreachable for the guards hence they have value -1.
'''
import math
import os
import random
import re
import sys

sys.setrecursionlimit(101000)


#
# Complete the find_shortest_distance_from_a_guard function below.
#
def find_shortest_distance_from_a_guard(grid):
    pass



if __name__ == '__main__':
    fptr = sys.stdout
    n = int(input().strip())
    m = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append([c for c in input().rstrip()])
    result = find_shortest_distance_from_a_guard(grid)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()


'''
We have provided a solution which contains necessary comments to understand the approach used:
optimal_solution.java
Description:
The idea is to consider the given board as a graph. Each cell has 4 neighbors, top, bottom, left and right. We cannot go
 to a wall neighbor.
If we have only one guard then the problem becomes a straight-forward problem for BFS. We will put that guard in the queue
 at the start and keep running breadth-first search and denote the distance to all the cells from that guard. Places which
 cannot be reached will be marked -1.
When there are more than one guards, we run a multi-source BFS. In multi-source breadth-first search, we add all the guards
 to the queue at the start with 0 distance. Then with every move to the neighbor, we add 1 to the original distance of the
 respective guard. We keep on storing the minimum distance of that cell from the guard when we reach a cell first time.

For better understanding of multi source concept:
https://www.geeksforgeeks.org/multi-source-shortest-path-in-unweighted-graph/
Time Complexity (assuming that input arguments are already given and excluding time used in the declaration of output):

O(n * m) where n denotes the number of rows of the grid and m denotes the number of columns of the grid.
As we are iterating complete grid twice. Once while checking possible guards and adding them in the queue. And second time
 while calculating distances with the help of queue as we are maintaining visited 2d array to avoid visiting already visited
 indices. Hence total complexity will be 2 * O(n * m) → O(n * m).
Time Complexity:
O(n * m) where n denotes the number of rows of the grid and m denotes the number of columns of the grid.
As time complexity assuming that input arguments are already given and excluding time used in the declaration of output
 is O(n * m), for reading input it will take O(n * m) as we are reading grid of size n * m, for declaration of output it
 will take O(n * m) as we are initializing a 2d array of integers of size n * m. Hence, total time complexity will be 3
 * O(n * m) → O(n * m).
Auxiliary Space Used:
O(n * m) where n denotes the number of rows of the grid and m denotes the number of columns of the grid.
As we are maintaining visited 2d array to avoid visiting already visited indices, space to store it will take O(n * m) and
 in worst case (when all are guards) queue will have n*m elements hence space for that will be O(n * m). Hence, the total
 auxiliary space used will be 2 * O(n * m) → O(n * m).
Space Complexity:
O(n * m) where n denotes the number of rows of the grid and m denotes the number of columns of the grid.
To store input, it will take O(n * m) as we are storing grid of size n * m, auxiliary space used is O(n * m), space for
 output will be O(n * m) hence 3 * O(n * m) → O(n * m).
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

    // -------------------- START ----------------------
    // Complete the find_shortest_distance_from_a_guard function below.
    static char GUARD = 'G';
    static char OPEN = 'O';
    static char WALL = 'W';
    
    static List<List<Integer>> find_shortest_distance_from_a_guard(List<List<Character>> grid) {
        int n = grid.size();
        int m = grid.get(0).size();
        List<List<Integer>> distance = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            distance.add(new ArrayList<Integer>());
            for (int j = 0; j < m; j++) {
                distance.get(i).add(-1);
            }
        }
        
        Queue<Node> queue = new LinkedList<>();
        // Initialize marker to keep track of visited cells
        boolean visited[][] = new boolean[n][m];
        // Adding all guards to the Queue
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid.get(i).get(j) == GUARD) {
                    // Cells with guards are at 0 distance from the Guard
                    queue.add(new Node(i, j, 0));
                }
            }
        }
        // Starting a multi-source BFS
        while (!queue.isEmpty()) {
            Node removedCell = queue.poll();
            // Continue if already visited
            if (visited[removedCell.x][removedCell.y]) {
                continue;
            }
            
            // Mark the new cell visited
            visited[removedCell.x][removedCell.y] = true;
            // Update the distance
            distance.get(removedCell.x).set(removedCell.y, removedCell.dist);
            // Iterate over other valid neighbours
            for (Node neighbour : validNeighboursOf(removedCell.x, removedCell.y, n, m, grid)) {
                neighbour.dist = removedCell.dist + 1;
                queue.add(neighbour);
            }
        }
        
        return distance;
    }
    
    // An entry in queue used in BFS
    static class Node {
        Node(int x, int y, int dist) {
            this.x = x;
            this.y = y;
            this.dist = dist;
        }
        
        int x, y;// Row and Column number
        int dist;// Distance of this vertex from source
    }
    /*
     * To calculate valid neighbours of node at index (x, y) from grid.
     */
    static ArrayList<Node> validNeighboursOf(int x, int y, int n, int m, 
        List<List<Character>> grid) {
        ArrayList<Node> listOfValidNeighbours = new ArrayList<>();
        
        // To the left
        if (isOnBoard(x - 1, y, n, m, grid)) {
            Node node = new Node(x - 1, y, 0);
            listOfValidNeighbours.add(node);
        }
        
        // To the right
        if (isOnBoard(x + 1, y, n, m, grid)) {
            Node node = new Node(x + 1, y, 0);
            listOfValidNeighbours.add(node);
        }
        
        // To the top
        if (isOnBoard(x, y - 1, n, m, grid)) {
            Node node = new Node(x, y - 1, 0);
            listOfValidNeighbours.add(node);
        }
        
        // To the bottom
        if (isOnBoard(x, y + 1, n, m, grid)) {
            Node node = new Node(x, y + 1, 0);
            listOfValidNeighbours.add(node);
        }
        
        return listOfValidNeighbours;
    }
    
    static boolean isOnBoard(int x, int y, int n, int m, List<List<Character>> grid) {
        // Cases for the cell not being on the board
        if (x < 0 || y < 0 || x >= n || y >= m || grid.get(x).get(y) != OPEN) {
            return false;
        } else {
            return true;
        }
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
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int gridRows = Integer.parseInt(bufferedReader.readLine().trim());
        int gridColumns = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Character>> grid = new ArrayList<>();

        IntStream.range(0, gridRows).forEach(i -> {
            try {
                grid.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(""))
                        .map(e -> e.charAt(0))
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<List<Integer>> result = Result.find_shortest_distance_from_a_guard(grid);

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
