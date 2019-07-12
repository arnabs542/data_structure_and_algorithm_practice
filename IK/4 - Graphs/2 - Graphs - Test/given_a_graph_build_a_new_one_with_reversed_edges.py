'''
Given A Graph, Build A New One With Reversed Edges
Problem Statement:
Given a strongly connected directed graph G, containing n nodes and m edges, you have to build a new graph containing n
 nodes, where edges are reversed than the original graph G.
This is also called Transposing the graph.
Input/Output Format For The Function:
Input Format:
There is only one argument pointing to a random node of the graph G.
Output Format:
Return any node in the new graph.
As input is a strongly connected graph, you will be able to visit all the nodes, given any random node.
Also when we reverse all the edges of strongly connected graph it will remain strongly connected graph, hence returning
 any one node is sufficient.
Input/Output Format For The Custom Input:
Input Format:
The first line of input should contain two space separated integers n and m, denoting no. of nodes and no. of edges in input
 graph G. In next m lines, each line should contain two space separated integers fromNode and toNode, denoting that there
 is an edge from fromNode to toNode in G.
If n = 3, m = 3 and edges = [(1 -> 2), (2 -> 3), (3 -> 1)], then input should be:
3 3
1 2
2 3
3 1
Output Format:
There will be one line of output, containing a string "Wrong Answer!" OR "Correct Answer!", depending on the evaluation
 of your solution’s output.
For input n = 3, m = 3 and edges = [(1 -> 2), (2 -> 3), (3 -> 1)], if your solution is correct, output will be:
Correct Answer!
Constraints:
1 <= n <= 315
Given graph does not contain multi edges (there will not be more than one edge connecting same pair of vertices
 in the same direction) and self loops.
Each node contains distinct values.
1 <= value stored in node <= n
You are not allowed
 to modify the given graph. Return completely new graph.
Sample Test Case:
Sample Input:
Any node of the graph where:
For n = 3
nodes = [1 2 3]
edges = [(1 -> 2), (2 -> 3), (3 -> 1)]
you could be given any node (1, 2 or 3) as input.
Sample Output:
Any node of the new graph where:
For n = 3
nodes = [1 2 3]
edges = [(2 -> 1), (3 -> 2), (1 -> 3)]
you could return any node as output.
Notes:
Maximum time allowed in interview: 20 Minutes.
'''

import sys
import os

sys.setrecursionlimit(101000)

class Node:
    def __init__(self):
        self.val = 0
        self.neighbours = []

# Complete the function below.

# For your reference:
#
# class Node:
#     def __init__(self):
#         self.val = 0
#         self.neighbours = []

def build_other_graph(node):
    pass


reversed = {}


def helper_dfs(reversed_node):
    reversed[reversed_node.val] = reversed_node
    n = len(reversed_node.neighbours)
    for i in range(0, n):
        if not reversed_node.neighbours[i].val in reversed:
            helper_dfs(reversed_node.neighbours[i])


def helper_get_all_addresses_in_reversed_graph(reversed_node):
    helper_dfs(reversed_node)
    return reversed


def helper(graph_nodes, graph_from, graph_to):
    # ----
    MAX_NODES = 315
    # ----

    original = {}
    for i in range(1, graph_nodes + 1):
        node = Node()
        node.val = i;
        original[i] = node
    edges = {}

    graph_edges = len(graph_from)
    for i in range(0, graph_edges):
        original[graph_from[i]].neighbours.append(original[graph_to[i]])
        edges[MAX_NODES * (graph_from[i] - 1) + graph_to[i] - 1] = True

    # Student will return only one node. Do a dfs and get all the nodes.
    reversed = helper_get_all_addresses_in_reversed_graph(build_other_graph(original[1]))

    sys.stderr.write("In returned graph: \n")
    for val in reversed.keys():
        sys.stderr.write("Neighbours of node " + str(val) + " = [")
        node = reversed[val]
        n = len(node.neighbours)
        for i in range(0, n):
            _val = node.neighbours[i].val
            sys.stderr.write(str(_val))
            if i != n - 1:
                sys.stderr.write(", ")
        sys.stderr.write("]\n")

    if (len(reversed) != graph_nodes):
        sys.stderr.write("Wrong answer because no of nodes in returned graph != no of nodes in original graph.\n")
        return "Wrong Answer!"

    for val in reversed.keys():
        node = reversed[val]
        if 1 > val or val > graph_nodes:
            sys.stderr.write("Wrong answer because value of node is out of range.\n")
            return "Wrong Answer!"
        # New graph should not contain node from original graph.
        if original[val] == reversed[val]:
            sys.stderr.write(
                "Wrong answer because instead of creating new node, you have used node from original graph.\n")
            return "Wrong Answer!"
        n = len(node.neighbours)
        for i in range(0, n):
            _val = node.neighbours[i].val
            temp = MAX_NODES * (_val - 1) + val - 1
            if not temp in edges:
                sys.stderr.write(
                    "Wrong answer because returned graph contains edge that is not present in original graph.\n")
                return "Wrong Answer!"
            del edges[temp]
    # All the edges should be present in the new graph.
    if len(edges) > 0:
        sys.stderr.write(
            "Wrong answer because returned graph contains extra edge that is not present in original graph\n")
        return "Wrong Answer!"
    return "Correct Answer!"


if __name__ == "__main__":
    f = sys.stdout

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for graph_i in range(graph_edges):
        graph_from[graph_i], graph_to[graph_i] = map(int, input().split())

    res = helper(graph_nodes, graph_from, graph_to)
    f.write(res + "\n")

    f.close()


'''
To solve this problem simple DFS will work! 
Code provided by will be enough to understand the idea.
Time Complexity:
As we are doing normal DFS time complexity of our solution will be O(V + E). We are given n nodes and also given that it
 does not contain multiple edges and self loops hence maximum number of edges possible is n * (n - 1). So time complexity
 will be O(n + n^2) that is O(n^2).
Space complexity:
Given input contains O(n^2) edges and we are also creating new graph with O(n^2) edges hence space complexity will be O(n^2).
'''
'''
#!/bin/python3

import sys
import os

sys.setrecursionlimit(101000)

class Node:
    def __init__(self):
        self.val = 0
        self.neighbours = []

# ---- START ----

# In constraints we are given that each node contains distinct values, so we can keep track of node 
# address using that value. {value : node}.
reversed_graph = {}

def dfs(node):    
    # First create new node. 
    temp_node = Node()
    temp_node.val = node.val
    reversed_graph[node.val] = temp_node
    # Visit all the neighbours.
    for inode in node.neighbours:
        # If node is not visited then first visit it.
        if not inode.val in reversed_graph:
            dfs(inode)
        # Add the reverse edge. 
        reversed_graph[inode.val].neighbours.append(temp_node)

def build_other_graph(node):
    # Build the graph.
    dfs(node)
    # Return any node of the new graph.
    return reversed_graph[1]

# ---- STOP ----

reversed = {}

def helper_dfs(reversed_node):
    reversed[reversed_node.val] = reversed_node        
    n = len(reversed_node.neighbours)
    for i in range(0, n):
        if not reversed_node.neighbours[i].val in reversed:
            helper_dfs(reversed_node.neighbours[i])

def helper_get_all_addresses_in_reversed_graph(reversed_node):
    helper_dfs(reversed_node)
    return reversed

def helper(graph_nodes, graph_from, graph_to):

    # ----
    MAX_NODES = 315
    # ----
    
    original = {}
    for i in range(1, graph_nodes + 1):
        node = Node()
        node.val = i;
        original[i] = node
    edges = {}
    
    graph_edges = len(graph_from)
    for i in range(0, graph_edges):
        original[graph_from[i]].neighbours.append(original[graph_to[i]])
        edges[MAX_NODES * (graph_from[i] - 1) + graph_to[i] - 1] = True

    # Student will return only one node. Do a dfs and get all the nodes.
    reversed = helper_get_all_addresses_in_reversed_graph(build_other_graph(original[1]))

    sys.stderr.write("In returned graph: \n")
    for val in reversed.keys():
        sys.stderr.write("Neighbours of node " + str(val) + " = [")
        node = reversed[val]
        n = len(node.neighbours)
        for i in range(0, n):
            _val = node.neighbours[i].val
            sys.stderr.write(str(_val))
            if i != n - 1:
                sys.stderr.write(", ")
        sys.stderr.write("]\n")

    if (len(reversed) != graph_nodes):
        sys.stderr.write("Wrong answer because no of nodes in returned graph != no of nodes in original graph.\n")
        return "Wrong Answer!"

    for val in reversed.keys():
        node = reversed[val]
        if 1 > val or val > graph_nodes:
            sys.stderr.write("Wrong answer because value of node is out of range.\n")
            return "Wrong Answer!"
        # New graph should not contain node from original graph. 
        if original[val] == reversed[val]:
            sys.stderr.write("Wrong answer because instead of creating new node, you have used node from original graph.\n")
            return "Wrong Answer!"
        n = len(node.neighbours)
        for i in range(0, n):
            _val = node.neighbours[i].val
            temp = MAX_NODES * (_val - 1) + val - 1
            if not temp in edges:
                sys.stderr.write("Wrong answer because returned graph contains edge that is not present in original graph.\n")
                return "Wrong Answer!"
            del edges[temp]
    # All the edges should be present in the new graph. 
    if len(edges) > 0:
        sys.stderr.write("Wrong answer because returned graph contains extra edge that is not present in original graph\n")
        return "Wrong Answer!"
    return "Correct Answer!"

if __name__ == "__main__":
    f = sys.stdout

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for graph_i in range(graph_edges):
        graph_from[graph_i], graph_to[graph_i] = map(int, input().split())

    res = helper(graph_nodes, graph_from, graph_to)
    f.write(res + "\n")


    f.close()
'''
