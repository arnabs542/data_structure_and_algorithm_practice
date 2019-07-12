'''
Snakes and Ladders Matrix
Problem Statement:
Given a snake and ladder rectangular board-game, find the minimum number of dice throws required to reach the final cell
 from the 1st cell.
Rules are as usual: If after a dice-throw, the player reaches a cell where the ladder starts, the player has to climb up
 that ladder and if the player reaches a cell that has the mouth of the snake, s/he has to go down to the tail of snake.

For example, in the board given below, it will take minimum 2 throws to reach from 1 to 20. That can be done with the following
 sequence of throws: (1,1). There may be more such sequences of the same length.
Input/Output Format For The Function:
Input Format:
You will be given an integer n, denoting the size of the board and an array of integer moves of length n, denoting if there
 is a ladder or a snake as follows:
moves[i] = -1, No ladder and no snake
moves[i] < i, Snake from i to moves[i]
moves[i] > i, Ladder from i to moves[i]
Note that moves array has one-based indexing.
Output Format:
Return an integer minMoves, denoting the minimum number of dice rolls required to reach the last cell.
Return -1 if there is no possible way.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting size of board.
The second line of input should also contain an integer n, denoting size of input array moves. In next n lines, ith line
 should contain an integer moves[i], denoting a value at index i of moves.
If n = 20 and moves = [-1, 19, -1, -1, -1, -1, -1, -1, 3, -1, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1], then input should
 be:
20
20
-1
19
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
-1
Output Format:
There will be one line of output, containing an integer minMoves, denoting the result returned by solution function.
If n = 20 and moves = [-1, 19, -1, -1, -1, -1, -1, -1, 3, -1, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1], output will be:
2
Constraints:
1 <= n <= 10^5
1 <=  moves[i] <= n
There is no snake at the last cell and no ladder at the first cell.
No snake starts at
 the top of a ladder or bottom of a snake. No ladder starts at the bottom of the snake or top of a ladder.
Sample Test Case:
Sample Input:
n = 20
moves = [-1, 19, -1, -1, -1, -1, -1, -1, 3, -1, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1]
Sample Output:
2
Explanation:
You start at cell 1. You roll 1 to go to cell 2 to take the stairs to cell 19. You roll 1 again to reach the last cell,
 20.
1 --> (2~19) --> 20
'''
import math
import os
import random
import re
import sys

# Complete the minNumberOfRolls function below.
def minNumberOfRolls(n, moves):
    pass



if __name__ == "__main__":
    fptr = sys.stdout

    n = int(input().strip())

    moves_count = int(input().strip())

    moves = []

    for _ in range(moves_count):
        moves_item = int(input().strip())
        moves.append(moves_item)

    res = minNumberOfRolls(n, moves)

    fptr.write(str(res) + '\n')

    fptr.close()

'''
Optimal solution
Consider the entire board as a graph. All cells are nodes and there is an edge of length 1 from where you stand to next
 6 cells on board, as there are 6 numbers on a dice. Whenever there is a snake or a ladder, then we go to their respective
 ends with no cost. For instance, when we are 24 and we roll 3 to reach 27, we would check if there is a ladder or a snake
 at 27. If there is, we go to the end of that snake or ladder. Otherwise, we stay at 27.
Hence, the entire problem is now reduced to graphs with given nodes and edges. We need to find the minimum distance to the
 the end node from the start node. We can run simple breadth first search(BFS) as the edges are of same weights.
Space Complexity: O(n)
Time Complexity: O(n)
'''
'''
import java.util.TreeSet;

public class OptimalSolution {
    // ==================start==================
    
    /*
     * Space Complexity: O(n)
     * Time Complexity: O(n)
     */
    static int minNumberOfRolls(int n, List<Integer> moves) {
        int[] move = new int[n];
        // Converting to 0 index based array
        for (int i = 0; i < n; i++) {
            move[i] = moves.get(i);
            if (move[i] != -1)
                move[i]--;
        }
        return minNumberOfRollsHelper(move, n);
    }
    
    // An entry in queue used in BFS
    static class Node {
        int index;// Vertex number
        int dist;// Distance of 0
    }
    
    static int minNumberOfRollsHelper(int move[], int n) {
        boolean visited[] = new boolean[n];
        
        // Add the 0th cell to the queue as we start from there
        Queue<Node> queue = new LinkedList<>();
        Node node = new Node();
        node.index = 0;
        node.dist = 0;
        queue.add(node);
        
        // Run BFS from Node 0
        while (!queue.isEmpty()) {
            Node removed = queue.poll();
            // Check if already visited
            if (!visited[removed.index]) {
                // Mark the removed cell visited and update the distance
                visited[removed.index] = true;
                if(removed.index==n-1){
                    return removed.dist;
                }
                // Add all the neighbors to the queue.
                for (int dice = 1; dice <= 6; dice++) {
                    if (removed.index + dice < n) {
                        Node newNode = new Node();
                        if (move[removed.index + dice] == -1) {
                            // If there is no snake or ladder
                            newNode.index = removed.index + dice;
                        } else {
                            // If there is a snake or a ladder
                            newNode.index = move[removed.index + dice];
                        }
                        // This requires one dice roll
                        newNode.dist = removed.dist + 1;
                        queue.add(newNode);
                    }
                }
            }
        }
        
        // No way to reach
        return -1;
    }
    
    // ==================end==================
}
'''
