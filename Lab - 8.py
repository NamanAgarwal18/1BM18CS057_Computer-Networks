# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:31:13 2020

@author: Naman
"""

class Graph:
    def __init__(self,n):
        self.matrix=[]
        self.n = n

    def addEdge(self,u,v,w):
        self.matrix.append((u,v,w))

    def printGraph(self,dist,src):
        print("Vector table of {}".format(chr(ord('A')+src)))
        for i in range(self.n):
            print("{0}\t{1}".format(chr(ord('A')+i),dist[i]))

    def pathCal(self,src):
        dist = [99]*self.n
        dist[src] = 0

        for _ in range(self.n - 1):
            for u,v,w in self.matrix:
                if dist[u]!=99 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        self.printGraph(dist,src)

matrix = []
print("Enter no of nodes")
n = int(input())

print("Enter adjacency matrix")

for i in range(n):
    g = list(map(int,input().split(" ")))
    matrix.append(g)
    
x = Graph(n)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            x.addEdge(i,j,1)

for _ in range(n):
    x.pathCal(_)