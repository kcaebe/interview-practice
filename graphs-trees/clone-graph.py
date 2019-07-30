"""
Given a reference of a node in a connected undirected graph, 
return a deep copy (clone) of the graph. 

Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

"""


class Node:
    def __init__(self, val, neighbors: List['Node']):
        self.val = val
        self.neighbors = neighbors

from typing import List
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned = {}
        head = Node(node.val, [])
        cloned[node] = head
        queue = deque([node])
        while queue:
            visiting = queue.popleft()
            if visiting not in cloned:
                cloned[visiting] = Node(visiting.val, [])
            for n in visiting.neighbors:
                if n in cloned:
                    cloned[visiting].neighbors.append(cloned[n])
                else:
                    cloned[n] = Node(n.val, [])
                    cloned[visiting].neighbors.append(cloned[n])
                    queue.append(n)
        return head
