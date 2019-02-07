from graphs.graph import Vertex, Graph
from datetime import datetime, timedelta
from queue import deque
import unittest


def clone_graph(graph):
    new_graph = Graph()
    q = deque()


