'''
Longest Path In Weighted DAG
Problem Statement:
Given a weighted DAG (directed acyclic graph), where weight of an edge denotes the length of that edge, a node from_node
 and a node to_node, you have to find longest path from from_node to to_node.
Nodes in the graph are numbered from 1 to dag_nodes, where dag_nodes denotes the total number of nodes in the graph.
Input/Output Format For The Function:
Input Format:
There are six arguments.
An integer dag_nodes
An integer array dag_from
An integer array dag_to
An integer array dag_weight
An integer from_node

An integer to_node
The first four arguments cumulatively describes the weighted DAG. dag_nodes describes the total number of nodes in the given
 graph and there is an edge from dag_from[i] node to dag_to[i] node with length dag_weight[i].
Output Format:
Return an array pathArr, describing longest path from from_node to to_node.
There can be multiple longest paths, so you are free to return any of them.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain two space separated integers dag_nodes and dag_edges, denoting no. of nodes and no.
 of edges in input DAG respectively. In next dag_edges lines, ith line should contain three space separated integers dag_from[i],
 dag_to[i], dag_weight[i], denoting values from node, to node and weight(length) for ith edge.
In next two lines, first line should contain an integer from_node and second line should contain to_node.
If dag_nodes = 4, dag_edges = 4, dag_from = [1, 1, 1, 3], dag_to = [2, 3, 4, 4], dag_weight =  [2, 2, 4, 3], from_node =
 1 and to_node = 4, then input should be:
4 4
1 2 2
1 3 2
1 4 4
3 4 3
1
4
Output Format:
Let’s denote m as length of pathArr, where pathArr is the array returned by solution function.
The first line of output contains a string (without quotes)   “<len> is the length of longest path in weighted DAG.”, where
 “<len>”would have been replaced with length of longest path described by pathArr.
In next line, there will be a string (without quotes) “Actual path is:”.
In next m lines, ith line contains an integer pathArr[i], denoting value at index i of pathArr.
For input dag_nodes = 4, dag_edges = 4, dag_from = [1, 1, 1, 3], dag_to = [2, 3, 4, 4], dag_weight =  [2, 2, 4, 3], from_node
 = 1 and to_node = 4, output will be:
5 is the length of longest path in weighted DAG.
Actual path is:
1
3
4
Constraints:
Given graph does not contain multi edges (there will not be more than one edge connecting same pair of vertices).
to_node
 is reachable from from_node.
1 <= dag_nodes <= 450
1 <= dag_from[i], dag_to[i], from_node, to_node <= dag_nodes
1 <= dag_weight[i]
 <= 2 * 10^9
Total number of edges in graph (dag_edges) <=
(dag_nodes * (dag_nodes - 1)) / 2
Sample Test Case:
Sample Input:
dag_nodes = 4
dag_from = [1 1 1 3]
dag_to = [2 3 4 4]
dag_weight =  [2 2 4 3]
from_node = 1
to_node = 4
Sample Output:
[1 3 4]
Explanation:
Total there are two paths from node 1 to node 4.
1) 1 -> 4 with length 4.
2) 1 -> 3 -> 4 with length 2 + 3 = 5.
So, Longest path from node 1 to node 4 is [1 3 4] with length 5.
Notes:
Maximum time allowed in interview: 20 Minutes.
When from_node = to_node, path contains only one node, so output should be [from_node] containing only one node.
It can be helpful to first store edges node wise and then use it.
Something like this:
vector<vector<pair<int, int>>> node_wise_edges(dag_nodes + 1, vector<pair<int, int>>(0));
for (int i = 0; i < dag_edges; i++)
{
node_wise_edges[dag_from[i]].push_back({dag_to[i], dag_weight[i]});
}
Now we have all the outgoing edges from node i in vector node_wise_edges[i]. And it will be easier to use.
'''
import sys
import os

# Complete the function below.

#
#	For the weighted graph:
#	1. The number of nodes is <name>_nodes.
#	2. The number of edges is <name>_edges.
#	3. An edge exists between <name>_from[i] to <name>_to[i] and the weight of the edge is <name>_weight[i].
#
def find_longest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node):
    pass


if __name__ == "__main__":
    f = sys.stdout
    dag_nodes, dag_edges = map(int, input().split())
    dag_from = [0] * dag_edges
    dag_to = [0] * dag_edges
    dag_weight = [0] * dag_edges
    for dag_i in range(dag_edges):
        dag_from[dag_i], dag_to[dag_i], dag_weight[dag_i] = map(int, input().split())
    from_node = int(input())
    to_node = int(input())
    res = find_longest_path(dag_nodes, dag_from, dag_to, dag_weight, from_node, to_node);
    for res_cur in res:
        f.write( str(res_cur) + "\n" )
    f.close()


'''
If you are getting wrong answer then first thing to check is that you are using appropriate data type to store the values.
 int will not work, need to use long long int. 
Given graph is dag. In dag we can divide our nodes in different levels, with "each edge" going from upper level to lower
 level. 
So we can start updating maximum length level wise, starting from upper level and then moving to level below it! 
To divide nodes level wise with each edge going from upper level to lower level, we can use topological sort! 
For more clear idea have a look at the solution provided by us. 
Time complexity of the solution is O(number of nodes in dag + number of edges in dag) and that can be re-written as O(number
 of edges in dag) from given constraints. 
Auxiliary space used by the solution is O(number of nodes in dag + number of edges in dag) and that can be re-written as
 O(number of edges in dag) from given constraints.
Space complexity of the solution is also O(number of nodes in dag + number of edges in dag) and that can be re-written as
 O(number of edges in dag) from given constraints.
Note that we should not write any of them as O(numberber of nodes in dag) because number of edges in dag can be way larger
 than number of nodes! 
'''
'''
#include<bits/stdc++.h>

using namespace std;

// ---- START ----

const int MAX_NODES = 450, MAX_WEIGHT = 2000000000;

/*
Note that we are passing vectors by reference. Passing vector by value will slow down solution. 
Either use pass by reference or use global vectors.
*/
void dfs(int from, vector<vector<pair<int, int>>> &node_wise_edges, 
	vector<int> &topological_order, vector<bool> &active, vector<bool> &visited)
{	
	/*
	Note that we are passing node_wise_edges, topological_order, active and visited by reference. 
	Either pass by reference or use global variables.  
	*/
	// Mark as visited.
	visited[from] = true;
	// This is just for our use you can ignore it. 
	active[from] = true;
	for (int i = 0; i < node_wise_edges[from].size(); i++)
	{
		int to = node_wise_edges[from][i].first;
		// This is just for our use you can ignore it. 
		assert(active[to] == false);
		// If the node is not visited then visit it and do dfs from that node. 
		if (visited[to] == false)
		{
			dfs(to, node_wise_edges, topological_order, active, visited);
		}
	}
	// This is just for our use you can ignore it. 
	active[from] = false;
	/*
	We could have added it at the front, but adding at the front is costly in vector type 
	container, so I have added at the end and then we will reverse this vector. 
	*/
	topological_order.push_back(from);
}

/*
I will quickly try to summarize how topological sorting works. In topological sorting we try to 
order nodes such that, nodes reachable from any ith node comes after the ith node. Suppose we have
only 2 nodes 1 and 2 and one edge 1 -> 2 then toplological order will be [1 2] because 2 is 
reachable from node 1, hence it should come after 1. We can use dfs to find the topological order.
In dfs we visit node then its children and then "come back" to that node "after" we have finished 
visiting all its reachable nodes. So when we have completed visiting all children nodes, then all 
children will have "already" finished visiting their children and will have pushed them self in 
topological order! So now if we add the current node then all its children will be already added! 
Try some examples and it will be more clear!    
*/
vector<int> topological_sort(int dag_nodes, vector<vector<pair<int, int>>>& node_wise_edges)
{
	vector<int> topological_order;
	/*
	You can ignore the active vector. This is for our use to check if given graph is a valid dag. 
	*/
	vector<bool> active(dag_nodes + 1, false);
	// Keeps track of visited nodes. 
	vector<bool> visited(dag_nodes + 1, false);
	for (int i = 1; i <= dag_nodes; i++)
	{
		// If the node is not visited then visit it and do dfs from that node. 
		if (visited[i] == false)
		{
			dfs(i, node_wise_edges, topological_order, active, visited);
		}
	}
	/*
	We have added the nodes at the end of topological_order vector that will give nodes in reverse
	order of topological order.
	*/
	reverse(topological_order.begin(), topological_order.end());
	return topological_order;
}

vector<int> find_longest_path(int dag_nodes, vector<int> dag_from, vector<int> dag_to, 
	vector<int> dag_weight, int from_node, int to_node)
{
	int dag_edges = dag_from.size();

	// Separate edges node-wise for quick access in future. 
	vector<vector<pair<int, int>>> node_wise_edges(dag_nodes + 1, vector<pair<int, int>>(0));
	for (int i = 0; i < dag_edges; i++)
	{
		node_wise_edges[dag_from[i]].push_back({dag_to[i], dag_weight[i]});
	}

	// Find topological order of given dag.
	vector<int> topological_order = topological_sort(dag_nodes, node_wise_edges);
	assert(topological_order.size() == dag_nodes);

	/*
	Longest_path[i] contains longest path from from_node to ith node (found till now). Here not 
	that we are using long long int! 
	*/
	vector<long long int> longest_path(dag_nodes + 1, -1);
	/*
	Parent[i] contains node through which Longest_path[i] updated last time. Suppose our final 
	answer is path (1 -> 5 -> 3) then Parent[3] will be 5. This is just to track the path. Using 
	this we will reconstruct the path. 
	*/
	vector<int> parent(dag_nodes + 1, 0);
	// Don't forget this. 
	longest_path[from_node] = 0;

	/*
	Iterate over each node in topological order and update nodes which are connected to the 
	current node. 
	*/
	for (int i = 0; i < dag_nodes; i++)
	{
		int from = topological_order[i];
		/*
		We initialized longest_path of node from_node as 0 and all other nodes as -1, hence update
		will start only at from_node. If you are confused then better to try some examples while 
		understanding this code. 
		*/
		if (longest_path[from] >= 0)
		{
			/*
			"each edge" goes from upper level to lower level hence once we have found our 
			destination node, it will not get updated by any other node so we can stop updating 
			here. This is just an optimization, if we remove this if then also code will work 
			fine. 
			*/
			if (from == to_node)
			{
				break;
			}
			for (int j = 0; j < node_wise_edges[from].size(); j++)
			{
				int to = node_wise_edges[from][j].first;
				long long int weight = node_wise_edges[from][j].second;
				// If longer path possible then update. 
				if (longest_path[to] <= longest_path[from] + weight)
				{
					longest_path[to] = longest_path[from] + weight;
					// Also keep track of node through which it gets updated. 
					parent[to] = from;
				}
			}
		}
	}

	// Find the path in reverse order! And then reverse it! 
	vector<int> path;
	path.push_back(to_node);
	while (to_node != from_node)
	{
		to_node = parent[to_node];
		path.push_back(to_node);
	}
	// Till now we have found the path in reverse order. 
	reverse(path.begin(), path.end());
	return path;
}

// ---- STOP ----


int main()
{
	//freopen("..//test_cases//sample_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//sample_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//handmade_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//handmade_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//generated_small_test_cases_input.txt", "r", stdin);
	//freopen("..//test_cases//generated_small_test_cases_expected_output.txt", "w", stdout);
	freopen("..//test_cases//generated_big_test_cases_input.txt", "r", stdin);
	freopen("..//test_cases//generated_big_test_cases_expected_output.txt", "w", stdout);
	//freopen("..//test_cases//ignore.txt", "w", stdout);

	int test_cases;
	cin >> test_cases;
	while(test_cases--)
	{
		int dag_nodes, dag_edges;
		cin >> dag_nodes >> dag_edges;
		assert(1 <= dag_nodes);
		assert(dag_nodes <= MAX_NODES);
		assert(dag_nodes - 1 <= dag_edges);
		assert(dag_edges <= (dag_nodes * (dag_nodes - 1)) / 2);

		vector<int> dag_from(dag_edges);
		vector<int> dag_to(dag_edges);
		vector<int> dag_weight(dag_edges);
		for (int i = 0; i < dag_edges; i++)
		{
			cin >> dag_from[i] >> dag_to[i] >> dag_weight[i];
			assert(1 <= dag_from[i]);
			assert(dag_from[i] <= dag_nodes);
			assert(1 <= dag_to[i]);
			assert(dag_to[i] <= dag_nodes);
			assert(1 <= dag_weight[i]);
			assert(dag_weight[i] <= MAX_WEIGHT);
		}

		int from_node, to_node;
		cin >> from_node >> to_node;
		assert(1 <= from_node);
		assert(from_node <= dag_nodes);
		assert(1 <= to_node);
		assert(to_node <= dag_nodes);

		vector<int> path = find_longest_path(dag_nodes, dag_from, dag_to, 
			dag_weight, from_node, to_node);

		map<pair<int, int>, int> weight;
		for (int i = 0; i < dag_edges; i++)
	    {
	    	// Ensure no multiple edges. 
	    	assert(weight.find({dag_from[i], dag_to[i]}) == weight.end());				
	        weight[{dag_from[i], dag_to[i]}] = dag_weight[i];
	    }

		long long int length = 0;						
		for (int i = 0; i < path.size() - 1; i++)
		{
			length += weight[{path[i], path[i + 1]}];				
		}
		cout << length << " is the length of longest path in weighted DAG." << endl;
		cout << "Actual path is:" << endl;
		for (int i = 0; i < path.size(); i++)
		{
			cout << path[i] << endl;	
		}
		cout << endl;
	}
	return 0;
}
'''
