from enum import IntEnum
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        class EdgeColor(IntEnum):
            UNVISITED = 0
            PROCESSING = 1
            VISITED = 2

        # Step 1: Initialize adjacency list for ALL n nodes safely
        A = {i: set() for i in range(n)}
        for n1, n2 in edges:
            A[n1].add(n2)
            A[n2].add(n1)
        
        D = {u: EdgeColor.UNVISITED for u in A}
        
        # Step 2: DFS to detect cycles
        def dfs(node, parent=None) -> bool:
            if D[node] != EdgeColor.UNVISITED:
                return False
                
            D[node] = EdgeColor.PROCESSING
            
            for nn in A[node]:
                if nn == parent:
                    continue
                    
                if D[nn] != EdgeColor.UNVISITED:
                    return False
                    
                if not dfs(nn, parent=node):
                    return False
                    
            D[node] = EdgeColor.VISITED            
            return True

        # Step 3: Start DFS from ANY arbitrary node (e.g., node 0)
        # If a cycle is detected, it's not a tree
        if not dfs(0, None):
            return False
            
        # Step 4: Ensure all n nodes were visited (graph is fully connected)
        return all(D[node] == EdgeColor.VISITED for node in range(n))
