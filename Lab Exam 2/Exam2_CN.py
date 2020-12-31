# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 11:57:58 2020

@author: Naman
"""

nodes = []
edges = []

def connect( p1, p2, cost):
       global edges
       edges.append((p1, p2, cost))
       edges.append((p2, p1, cost))
       
def distance_vector_routing(condition):
        global edges, nodes
        import collections
        for node in nodes:
            dist = collections.defaultdict(int)
            next_hop = {node: node}
            for other_node in nodes:
                if other_node != node:
                    dist[other_node] = 99999 
            for i in range((nodes.__len__()-1)):
                for edge in edges:
                    src, dest, cost = edge
                    if dist[src] + cost < dist[dest]:
                        dist[dest] = dist[src] + cost
                        if src == node:
                            next_hop[dest] =dest
                        elif src in next_hop:
                            next_hop[dest] = next_hop[src]
            if condition == False:
                print_table(node, dist, next_hop)
                print()
            else:
                printing_table(node, dist, next_hop)
                
        
def print_table(node, dist, next_hop):
    if node == 'C':
        print(f'Routing table for Node: {node}')
        print('Dest \t Cost \t Next Hop')
        for dest, cost in dist.items():
            #if dest == 'D' or dest == 'F':
                print("  ",dest,"\t  ",cost,"  \t  ",next_hop[dest])

def printing_table(node, dist, next_hop):
    #if node == 'C':
        print(f'Routing table for Node: {node}')
        print('Dest \t Cost \t Next Hop')
        for dest, cost in dist.items():
            #if dest == 'D' or dest == 'F':
                print("  ",dest,"\t  ",cost,"  \t  ",next_hop[dest])
            
def addEdge():
     global edges
     p1 = input("Enter Node 1: ")
     p2 = input("Enter Node 2: ")
     cost = int(input("Enter the Cost: "))
     
     edges.append((p1, p2, cost))
     edges.append((p2, p1, cost))
     
def predifined():
    global nodes
    nodes = ['A', 'B', 'C', 'F', 'E', 'D', 'G']
    connect('A', 'B', 4)
    connect('A', 'C', 5)
    connect('A', 'D', 3)
    connect('B', 'C', 2)
    connect('B', 'F', 3)
    connect('B', 'G', 4)
    connect('C', 'D', 6)
    connect('C', 'E', 4)
    connect('C', 'F', 4)
    connect('D', 'E', 3)
    connect('E', 'F', 2)
    connect('F', 'G', 5)
    distance_vector_routing(False)
            
    
def main():
    global nodes, edges
    choice = input("Do You wish to find output of the already feeded values (Y/N): ")
    if choice == 'Y' or choice == 'y':
        predifined()
    else:
        
        number = int(input("Enter the Number of Nodes: "))
        for i in range(number):
            node = input("Enter Node: ")
            nodes.append(node)
            while(True):
                choice = input("Do You wish to enter an edge(Y/N): ")
                if choice == 'Y' or choice == 'y':
                    addEdge()
                else:
                    break
        distance_vector_routing(True)
main()
    
    
    
    
    
    