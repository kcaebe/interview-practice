"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from 
node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  
graph[i] is a list of all nodes j for which the edge (i, j) exists.


"""

from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if len(graph) <= 1:
            return graph
        return self.find_paths(graph, 0, [0])
            
    
    def find_paths(self, graph: List[List[int]], node: int, path: List[List[int]]) -> List[List[int]]:
        if node >= len(graph):
            return None
#         we are at the end of the 
        if len(graph[node]) == 0:
            return [path] if node == (len(graph) -  1) else None
        paths = []
        for n in graph[node]:
            p = self.find_paths(graph, n, path + [n])
            if p:
                paths += p
        return paths
        
obj = Solution()
print(obj.allPathsSourceTarget([[1,2], [3], [3], []])) # -> [[0,1,3],[0,2,3]] 