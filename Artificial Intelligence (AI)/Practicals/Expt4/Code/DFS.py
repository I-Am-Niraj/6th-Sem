# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 09:42:11 2023

@author: Niraj Surve
"""
# ABCEHGDXYFZWPQR
# graph = {
#   'A' : set(['B','D', 'F']),
#   'B' : set(['C']),
#   'D' : set(['X', 'F']),
#   'F' : set(['D', 'Z', 'R']),
#   'C' : set(['E', 'H']),
#   'X' : set(['H', 'Y']),
#   'Z' : set(['W', 'P', 'Q']),
#   'R' : set(['Q']),
#   'E' : set([]),
#   'H' : set(['G']),
#   'Y' : set([]),
#   'W' : set([]),
#   'P' : set([]),
#   'Q' : set([]),
#   'G' : set([])
# }

n = int(input("Enter the number of vertices: "))
m = int(input("Enter the number of edges: "))
graph = [None] * n
visited = [False] * n
for i in range(n):
    graph[i] = []
for i in range(m):
    u, v = [int(x) for x in input("Enter the edge (u v): ").split()]
    graph[u].append(v)
start = int(input("Enter the starting vertex: "))
print("Depth First Traversal:")

def DFS(graph, visited, vertex):
    visited[vertex] = True
    print(vertex, end=' ')
    for i in graph[vertex]:
        if not visited[i]:
            DFS(graph, visited, i)

DFS(graph, visited, start)