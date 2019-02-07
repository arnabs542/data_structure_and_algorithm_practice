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


