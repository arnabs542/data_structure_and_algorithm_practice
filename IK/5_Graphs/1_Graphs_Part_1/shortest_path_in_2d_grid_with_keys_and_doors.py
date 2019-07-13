'''
Shortest Path In 2D Grid With Keys And Doors
Problem Statement:
Given a 2D grid of size n * m, that represents a maze-like area, a start cell and a goal cell, you have to find the shortest
 path from start to the goal.
You can go up, down, left or right from a cell, but not diagonally.
Each cell in the grid can be either land or water or door or key to some doors.
You can only travel on land cells, key cells and door cells, and not on water cells.
Each type of key will open only one type of door. There can be multiple identical keys of the same type. There can also
 be multiple doors of the same type. You cannot travel through a door, unless you have picked up the key to that door before
 arriving there. If you have picked up a certain type of key, then it can be re-used on multiple doors of same kind.
It is allowed to revisit a cell.
Input/Output Format For The Function:
Input Format:
There is only one argument: String array rowStr.
rowStr describes the grid.
Cells in the grid can be described as:
'#' = Water.
'.' = Land.
'a' = Key of type 'a'. All lowercase letters are keys.
'A' = Door that opens with key 'a'. All uppercase letters are doors.
'@' = Starting cell.
'+' = Ending cell (goal).
Output Format:
Return a 2D integer array pathArr, containing the path from start cell to goal cell.
Suppose your path contains p cells, then output array should be of size p * 2, where (pathArr[i][0], pathArr[i][1]) describes
 a cell position.
Positioning of cells:
0-indexed.
Columns: Increasing from left to right.
Rows: Increasing from top to bottom.
There can be multiple shortest paths, so you are free to return any of them.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain an integer n, denoting no. of rows in input grid, which is also a size of array rowStr.
 In next n lines, ith line should contain a string rowStr[i], denoting value at index i of rowStr.
If n = 3, m = 4 and rowStr = [“...B”, “.b#.”, “@#+.”], then input should be:
3
...B
.b#.
@#+.
Output Format:
Let’s denote p * 2 as dimensions of pathArr, where pathArr is the 2D array returned by solution function.
The first line of output contains a string (without quotes)   “<len> cells will be visited in shortest path.”, where “<len>”would
 have been replaced with value of p.
In next line, there will be a string (without quotes) “Actual path is:”.
In next p lines, ith line contains two space separated integers pathArr[i][0] and pathArr[i][1], denoting value at index
 (i,0) and (i,1) of pathArr respectively.
For input n = 3, m = 4 and rowStr = [“...B”, “.b#.”, “@#+.”], output will be:
9 cells will be visited in shortest path.
Actual path is:
2 0
1 0
1 1
0 1
0 2
0 3
1 3
2 3
2 2
Constraints:
1 <= n, m <= 100
There will be exactly one starting point and one goal.
It is guaranteed that there exists a path from start
 to goal.
'a' <= key <= 'j'
'A' <= door <= 'J'
Sample Test Case:
Sample Input:
...B
.b#.
@#+.
Sample Output:
[
[2 0],
[1 0],
[1 1],
[0 1],
[0 2],
[0 3],
[1 3],
[2 3],
[2 2]
]
Explanation:
In order to pass through door 'B', we first need to collect key to open that door and that is 'b'.
'@' -> '.' -> 'b' -> '.' -> '.' -> 'B' -> '.' -> '.' -> '+'
Here position [2 0] is '@' in the grid above, which is the starting position.
Notes:
Maximum time allowed in interview: 20 Minutes.
'''
#!/bin/python3

import sys
import os

# Complete the function below.

def find_shortest_path(grid):
    pass


if __name__ == "__main__":
    f = sys.stdout

    grid_cnt = 0
    grid_cnt = int(input())
    grid_i = 0
    grid = []
    while grid_i < grid_cnt:
        try:
            grid_item = str(input())
        except:
            grid_item = None
        grid.append(grid_item)
        grid_i += 1


    res = find_shortest_path(grid);
    for res_x in res:
        for res_y in res_x:
            f.write(str(res_y) + " ")
        f.write("\n")

    f.close()

'''
If there are no keys and doors then solution would be a simple BFS. 
Now lets think about the original problem.
To solve the original problem also, we can use BFS, but with some modifications! 
There can be only 10 different keys ('a' to 'j'). So we can use bitmasking to store the keys. Specifically we can use int
 to store the keys that we already have (call that int as ring_of_keys). If we have only key of type 'a' then ring_ok_keys
 would be 000..000001 in binary representation, if we have two keys 'a' and 'd' then ring_of_keys would be 000..001001 in
 binary representation. Here we will use 10 least significant bits to store the keys. 
Now lets think about BFS when neighbour cell is:
1) Water: Simply return because we can not use water cell.
2) Land (not key and not door): Continue BFS. Visit(update/add/consider) its neighbours.
3) Start: Consider it as land cell.
4) Stop: Return and update ans.
5) Door: Check if corresponding key is present in the ring_of_keys or not, if yes then treat it as land cell else treat
 it as water cell. We can check it using 
if ((ring_of_keys >> (grid[r][c] - 'A')) & 1)
treat as land
else
treat as water
6) Key: This is the part where we need to pay attention. If we already have collected the same type of key then consider
 it as a land cell because it does not change anything, else we need to do something more. If we have found a new key then
 it might be possible that in past during BFS, somewhere we were not able to go thru door but now we can because that can
 be opended by this key. So we need to reconsider the visited cells "and" continue visiting unvisited cells also.
if ((ring_of_keys >> (grid[r][c] - 'a')) & 1)
treat as land
else
revisit visited cells and continue BFS
Now first have a look at the "exponential solution" provided by us (brute_force.java). That uses DFS but idea is almost
 same. This will help you understand the basic idea. 
This solution will only work for smaller constraints. Problem with this solution is that it does lots of recomputation.

Now let's think about optimized solution.
Let's take dp[r][c][ring_of_keys] as shortest path from starting point to current point denoted by (r, c), where we have
 already collected keys present in ring_of_keys.
Base case is dp[start_r][start_c][0] = 0. Set others as INFINITY, now do BFS!
During BFS when neighbour cell is:
1) Water: Simply return because we can not use water cell.
2) Land: Add that cell and update it. We can go to that neighbour cell by taking one more step! And we will also have all
 the keys. So that can be done as, 
dp[neighbout_r][neighbour_c][ring_of_keys] = dp[cur_r][cur_c][ring_of_keys] + 1. 
3) Start: Consider it as land cell.
4) Stop: Return and update ans.
5) Door: Check if corresponding key is present in the ring_of_keys or not, if yes then treat it as land cell else treat
 it as water cell.
6) Key: If we already have collected the same type of key then consider it as a land cell because it does not change anything,
 else update differently. Add the key to our ring_of_keys (let's say new_ring_of_keys). So that can be done as, 
dp[neighbout_r][neighbour_c][new_ring_of_keys] = dp[cur_r][cur_c][ring_of_keys] + 1. 
In normal BFS we do not visit previously visited cell again, here we will not visit previously visited "state" again, which
 means we will not visit dp[r][c][ring_of_keys] if it is already visited (but here it is possible that same node is visited
 again!). 
Lets take very small example. 
Grid = "a@A+" now initially we have, 
dp[0][1][0] = 0, (we are at the starting position and we don't have any key)
now from '@' 'a' will be updated hence, 
dp[0][0][1] = 1, (we are at 'a' and we have collected one key)
now this will update '@',  
dp[0][1][1] = 2, (again we are at the starting position and we have collected one key)
so '@' is visited again.
Now have a look at the optimal_solution.cpp. It will give more clear idea about the solution. 
Time complexity, auxiliary space used and space complexity of the solution is O(number of rows * number of cols * 2^(number
 of different keys possible that is 10 in our case)).  
'''
'''
BRUTE FORCE
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the function below.
     */
    static int[][] find_shortest_path(String[] grid) {
    	char [][] board = new char[grid.length][grid[0].length()];
    	for(int i = 0; i < grid.length; i++)
    	{
    		for (int j = 0; j < grid[0].length(); j++)
    		{
    			board[i][j] = grid[i].charAt(j);
                //System.out.println(board[i][j]);
    		}
    	}
        return (pathToString(solve(board)));
    }

    private static final class Coord {
		final int y, x;
		Coord(int y, int x) {
			this.y = y;
			this.x = x;
		}
		@Override public String toString() {
			return String.valueOf(this.y).concat(String.valueOf(this.x));
		}
	}
	private static int[][] pathToString(Iterable<Coord> path) {
        int sz = 0;
		for (Coord coord : path)
            sz++;
        //System.out.println(sz);
        int[][] ans = new int[sz][2];
        int i = 0;
        for (Coord coord : path)
        {
            ans[i][0] = coord.y;
            ans[i][1] = coord.x;
            i++;
        }
		return ans;
	}
	private static List<Coord> solve(char[][] board) {
		List<Coord> shortestPathToGoal = new ArrayList<>();
		for (int y = 0; y < board.length; y++)
			for (int x = 0; x < board[y].length; x++)
            {
                // System.out.println(board[y][x]);
				if (board[y][x] == '@'/*Start*/)
					walk(board, y, x, 0, 
                        initVisited(board), new ArrayDeque<>(), shortestPathToGoal);
            }
		return shortestPathToGoal;
	}
	private static void walk(char[][] board, int y, int x, int keyRing, boolean[][] visited,
	                         Deque<Coord> path, List<Coord> shortestPathToGoal) {
        //System.out.println(y);
		if (y < 0 || y >= board.length || x < 0 || x >= board[y].length || visited[y][x])
			return; // outside board or already visited
		char point = board[y][x];
		if (point == '#'/*Water*/)
			return; // cannot walk on water
		if (point == '+'/*Goal*/) {
			shortestPathToGoal.clear();
			shortestPathToGoal.addAll(path);
			shortestPathToGoal.add(new Coord(y, x));
            //System.out.println("---- ----");
			return; // return to look for alternate shorter path
		}
		if (! shortestPathToGoal.isEmpty() && path.size() + 2 >= shortestPathToGoal.size())
			return; // shorter (or equal) path already found
		if (point >= 'A' && point <= 'Z') { // Door
			if ((keyRing & (1 << (point - 'A'))) == 0)
				return; // missing key
		} else if (point >= 'a' && point <= 'z') { // Key
			if ((keyRing & (1 << (point - 'a'))) == 0) {
				keyRing |= (1 << (point - 'a')); // add key to keyring
				visited = initVisited(board); // may now revisit previous steps
			}
		}
		visited[y][x] = true;
		path.addLast(new Coord(y, x));
		walk(board, y    , x + 1, keyRing, visited, path, shortestPathToGoal); // right
		walk(board, y + 1, x    , keyRing, visited, path, shortestPathToGoal); // down
		walk(board, y    , x - 1, keyRing, visited, path, shortestPathToGoal); // left
		walk(board, y - 1, x    , keyRing, visited, path, shortestPathToGoal); // up
		path.removeLast();
		visited[y][x] = false;
	}
	private static boolean[][] initVisited(char[][] board) {
		boolean[][] visited = new boolean[board.length][];
		for (int y = 0; y < board.length; y++)
			visited[y] = new boolean[board[y].length];
		return visited;
	}

	public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        final String fileName = System.getenv("OUTPUT_PATH");
        BufferedWriter bw = null;
        if (fileName != null) {
            bw = new BufferedWriter(new FileWriter(fileName));
        }
        else {
            bw = new BufferedWriter(new OutputStreamWriter(System.out));
        }

        int[][] res;
        int grid_size = 0;
        grid_size = Integer.parseInt(in.nextLine().trim());

        String[] grid = new String[grid_size];
        for(int i = 0; i < grid_size; i++) {
            String grid_item;
            try {
                grid_item = in.nextLine();
            } catch (Exception e) {
                grid_item = null;
            }
            grid[i] = grid_item;
        }

        res = find_shortest_path(grid);
        int res_rowLength = res.length;
        int res_colLength = res[0].length;
        for(int res_i = 0; res_i < res_rowLength; res_i++) {
            for(int res_j = 0; res_j < res_colLength; res_j++) {
                bw.write(String.valueOf(res[res_i][res_j]) + " ");
            }
            bw.newLine();
        }

        bw.close();
    }
}
'''
'''
#include<bits/stdc++.h>

using namespace std;

// ---- START ----

const int MAX_ROWS = 100, MAX_COLS = 100, MAX_KEYS = 10, MAX_MASK = (1 << MAX_KEYS), 
	INF = MAX_ROWS * MAX_COLS * (MAX_KEYS + 1);
const int add_r[4] = {-1, 0, 1, 0};
const int add_c[4] = {0, -1, 0, 1};

vector<vector<int>> build_path(vector<vector<vector<int>>> &dp, 
	vector<vector<vector<pair<pair<int, int>, int>>>> &parent, int ring_of_keys, 
	pair<int, int> &start, pair<int, int> &stop)
{
	vector<vector<int>> ans;
	ans.push_back(vector<int>(0));
	ans[0].push_back(stop.first);
	ans[0].push_back(stop.second);

	/*
	stop only when ring_of_keys is 0. Both conditions are necessary. Consider input 1 5 "#a@A+#", 
	here @ -> a -> @ -> A -> + , so when reconstructing + -> A -> @ and still we need to continue! 
	*/
	while (stop != start || ring_of_keys != 0)
	{
		pair<pair<int, int>, int> par = parent[stop.first][stop.second][ring_of_keys];
		stop = par.first;
		ring_of_keys = par.second;
		ans.push_back(vector<int>(0));
		ans[ans.size() - 1].push_back(stop.first);
		ans[ans.size() - 1].push_back(stop.second);
	}
	reverse(ans.begin(), ans.end());
	return ans;
}

bool is_start(char ch)
{
	return ch == '@';
}

bool is_stop(char ch)
{
	return ch == '+';
}

bool is_water(char ch)
{
	return ch == '#';
}

bool is_land(char ch)
{
	return ch == '.';
}

bool is_key(char ch)
{
	return ('a' <= ch && ch < ('a' + MAX_KEYS));
}

bool is_door(char ch)
{
	return ('A' <= ch && ch < ('A' + MAX_KEYS));
}

bool can_open_door(char door, int ring_of_keys)
{
	return (ring_of_keys >> (door - 'A')) & 1;
}

void add_neighbour_to_queue(int to_r, int to_c, int to_ring_of_keys, 
	pair<pair<int, int>, int> from, vector<vector<vector<pair<pair<int, int>, int>>>> &parent, 
	vector<vector<vector<int>>> &dp, vector<vector<vector<bool>>> &visited, 
	queue<pair<pair<int, int>, int>> &q)
{
	parent[to_r][to_c][to_ring_of_keys] = from;
	dp[to_r][to_c][to_ring_of_keys] = dp[from.first.first][from.first.second][from.second] + 1;
	visited[to_r][to_c][to_ring_of_keys] = true;
	q.push({{to_r, to_c}, to_ring_of_keys});
}

// better to pass vectors by reference
void bfs(vector<string> &grid, pair<int, int> &start, vector<vector<vector<int>>> &dp, 
	vector<vector<vector<pair<pair<int, int>, int>>>> &parent, 
	vector<vector<vector<bool>>> &visited)		
{
	int rows = grid.size();
	int cols = grid[0].length();

	queue<pair<pair<int, int>, int>> q;
	// Starting point with no keys has 0 distance (itself). 
	q.push({start, 0});
	dp[start.first][start.second][0] = 0;
	visited[start.first][start.second][0] = true;

	while(q.empty() == false)
	{
		pair<pair<int, int>, int> from = q.front();
		q.pop();
		if (is_stop(grid[from.first.first][from.first.second]))
		{
			continue;
		}
		// Visit all four neighbours and update.
		for (int i = 0; i < 4; i++)
		{
			int to_r = from.first.first + add_r[i];
			int to_c = from.first.second + add_c[i];
			if (to_r < 0 || to_r >= rows || to_c < 0 || to_c >= cols)
			{
				continue;
			}
			if (is_water(grid[to_r][to_c]))
			{
				continue;
			}
			else if (is_land(grid[to_r][to_c]) || is_start(grid[to_r][to_c]) || 
				is_stop(grid[to_r][to_c]))
			{
				if (visited[to_r][to_c][from.second] == false)
				{
					add_neighbour_to_queue(to_r, to_c, from.second, from, parent, dp, visited, q);
				}
			}
			else if (is_key(grid[to_r][to_c]))
			{
				int new_ring_of_keys = from.second  | (1 << (grid[to_r][to_c] - 'a'));
				if (visited[to_r][to_c][new_ring_of_keys] == false)
				{
					add_neighbour_to_queue(to_r, to_c, new_ring_of_keys, from, parent, dp, 
						visited, q);
				}
			}
			else if (is_door(grid[to_r][to_c]))
			{
				// Can enter only if we have key for that door. 
				if (can_open_door(grid[to_r][to_c], from.second))
				{
					if (visited[to_r][to_c][from.second] == false)
					{
						add_neighbour_to_queue(to_r, to_c, from.second, from, parent, dp, 
							visited, q);
					}
				}
			}
		}
	}
}

// node that start and stop are passed by reference hence change will be reflected. 
void get_start_and_stop_positions(vector<string> &grid, pair<int, int> &start, 
	pair<int, int> &stop)	
{
	int rows = grid.size();
	int cols = grid[0].length();
	for (int r = 0; r < rows; r++)
	{
		for (int c = 0; c < cols; c++)
		{
			if (is_start(grid[r][c]))
			{
				start = {r, c};
			}
			else if(is_stop(grid[r][c]))
			{
				stop = {r, c};
			}
		}
	}
}

vector<vector<int>> find_shortest_path(vector<string> grid)
{
	int rows = grid.size();
	int cols = grid[0].length();
	pair<int, int> start, stop;
	// Get the starting and ending point.
	get_start_and_stop_positions(grid, start, stop);
	/*
	dp[r][c][ring] denotes length of shortest path from starting point to (r, c) and we have 
	already got keys in the ring. 
	*/
	vector<vector<vector<int>>> dp(rows, vector<vector<int>>(cols, vector<int>(MAX_MASK, INF)));
	/*
	parent[r][c][ring] denotes the last node through which dp[r][c][ring] is updated. This will 
	help to reconstruct the path.
	*/
	vector<vector<vector<pair<pair<int, int>, int>>>> parent(rows, 
		vector<vector<pair<pair<int, int>, int>>>(cols, vector<pair<pair<int, int>, int>>
			(MAX_MASK, {{-1, -1}, -1})));
	/*
	visited[r][c][ring] keeps track of dp[r][c][ring] is visited or not. Though parent is enough 
	to track this, but for readability purpose I have added this also. 
	*/
	vector<vector<vector<bool>>> visited(rows, 
		vector<vector<bool>>(cols, vector<bool>(MAX_MASK, false)));
	// Do bfs.
	bfs(grid, start, dp, parent, visited);
	/*
	As dp[r][c][ring] denotes shortest path from start point and we have already got keys in the 
	ring, we just need to find for which key path is shorter. 
	*/
	int length = INF;
	int ring_of_keys;
	for (int i = 0; i < MAX_MASK; i++)
	{
		if (length > dp[stop.first][stop.second][i])
		{
			length = dp[stop.first][stop.second][i];
			ring_of_keys = i;
		}
	}
	// cout << length << endl;

	// Build the path from using parent. 
	return build_path(dp, parent, ring_of_keys, start, stop);
}

// ---- STOP ----


int main()
{
	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	while (test_cases--)
	{
		int rows, cols;
		// cin >> rows >> cols;
		cin >> rows;
		/* assert(1 <= rows);
		assert(rows <= MAX_ROWS);
		assert(1 <= cols);
		assert(cols <= MAX_COLS);*/

		vector<string> grid (rows);
		int start = 0, stop = 0;
		for (int r = 0; r < rows; r++)
		{
			cin >> grid[r];
			cols = grid[r].length();
			for (int c = 0; c < cols; c++)
			{
				assert(
					is_start(grid[r][c]) ||
					is_stop(grid[r][c])  ||
					is_water(grid[r][c]) ||
					is_land(grid[r][c])  ||
					is_key(grid[r][c])   ||
					is_door(grid[r][c])
				);
				if (is_start(grid[r][c]))
				{
					start++;
				}
				else if (is_stop(grid[r][c]))
				{
					stop++;
				}
			}
		}
		assert(start == 1);
		assert(stop == 1);

		vector<vector<int>> ans = find_shortest_path(grid);

		cout << ans.size() << " cells will be visited in shortest path." << endl;
		cout << "Actual path is:" << endl;
		assert(ans.size() != 0);
		for (int i = 0; i < ans.size(); i++)
		{
			cout << ans[i][0] << " " << ans[i][1] << endl;
		}
		cout << endl;
	}

	return 0;
}
'''





