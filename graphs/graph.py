from datetime import datetime, timedelta
from queue import deque
import unittest

class Vertex:
    def __init__(self, v=None, n=None):
        self.val = v
        if n == None:
            self.neighbors = []

class Graph():
    def __init__(self):
        self.vertices = []

    def bfs(self):
        visited = set()
        for vertex in self.vertices:
            if vertex not in visited:
                self.explore(vertex, visited)
        print()

    def explore(self, vertex, visited):
        q = deque()
        q.appendleft(vertex)
        visited.add(vertex)
        print("Components are: ", end="")
        while len(q) > 0:
            cur = q.pop()
            print(cur.val, end=" ")
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.appendleft(neighbor)

# O(degree of each vertex) which ends up being 2E = O(E)
def get_connected_components(cur_vertex, seen, cur_component_list):
    seen.add(cur_vertex.val) # add to visited set so that we don't come here again
    cur_component_list.append(cur_vertex.val) # add to current component list

    for neighbor in cur_vertex.neighbors:
        if neighbor not in seen:
            get_connected_components(neighbor, seen, cur_component_list)

    return cur_component_list

# O(V) not including the get_connected_components function
def dfs(adjList):
    seen = set()
    for vertex in adjList:
        if vertex.val not in seen:
            component = get_connected_components(vertex, seen, [])
            print(component)

