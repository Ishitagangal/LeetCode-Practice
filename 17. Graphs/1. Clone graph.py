"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        # DFS
        if not node:
            return node
        
        if node in self.visited:
            return self.visited[node]
        
        clone = Node(node.val, [])
        
        self.visited[node] = clone
        
        if node.neighbors:
            clone.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        
        return clone
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        # BFS
        if not node:
            return node
        
        visited = {}
        
        q = []
        q.append(node)
        
        visited[node] = Node(node.val, [])
        
        while q:
            n = q.pop()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
    