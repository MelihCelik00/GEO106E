# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 16:26:26 2018

@author: ITUGG
"""
import math
from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def distance(P1, P2):
	dist = math.sqrt((P1.x - P2.x)**2 + (P1.y - P2.y)**2)
	return dist

# Define points
A = Point(x = 7, y = 1)
B = Point(x = 9, y = 4)
C = Point(x = 1, y = 3)
D = Point(x = 9, y = 9)
E = Point(x = 1, y = 10)
F = Point(x = 8, y = 12)
G = Point(x = 5, y = 7)

graph = Graph() # create a graph instance
nodeList = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Add nodes to the graph instance
for node in nodeList:
    graph.add_node(node)
# Add edges to the graph instance
graph.add_edge('A', 'B', distance(A,B))
graph.add_edge('A', 'C', distance(A,C))
graph.add_edge('B', 'C', distance(B,C))
graph.add_edge('B', 'D', distance(B,D))
graph.add_edge('B', 'G', distance(B,G))
graph.add_edge('C', 'E', distance(C,E))
graph.add_edge('C', 'G', distance(C,G))
graph.add_edge('D', 'E', distance(D,E))
graph.add_edge('D', 'G', distance(D,G))
graph.add_edge('D', 'F', distance(D,F))
graph.add_edge('E', 'F', distance(E,F))
graph.add_edge('E', 'G', distance(E,G))

print(shortest_path(graph, 'A', 'F')) # output