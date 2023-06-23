class Solution:
    # While examing the children, 
    # We want to keep track of the 2 longest paths starting from this node,
    # So that we can compute the longest path going through this node 
    # in the sub-tree rooted at this node.
    # Update the result.
    # Again, max1+max2+1 means the length of the longest valid path 
    # going through this node in the sub-tree rooted at this node.
    def longestPath(self, parents: List[int], s: str) -> int:
        # parent[i] is the parent of ith node 
        tree = defaultdict(list)
        for child, parent in enumerate(parents):
            tree[parent].append(child)
        
        result = 1
        def dfs(node):
            nonlocal result
            ## keep top two paths in tree
            max1 = max2 = 0
            for child in tree[node]:
                child_length = dfs(child)
                if s[child] != s[node]:
                    if child_length > max1:
                        max2 = max1
                        max1 = child_length
                    elif child_length > max2:
                        max2 = child_length
            
            result = max(result, max1 + max2 + 1) # max when path is rooted at current node
            return max1 + 1 # return longest path + current node
        dfs(0)
        return result