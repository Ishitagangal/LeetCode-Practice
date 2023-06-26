"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node == '#':
                result.append("null")
            elif node == None:
                result.append("null")
            else:
                queue.append("#")
                result.append(node.val)
                for child in node.children:
                    queue.append(child)
        while result and result[-1] == "null":
            result.pop()
        print(result)
        return ",".join(str(s) for s in result)
	
    def deserialize(self, input: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        def createNode(s):
            if s == 'null': return None
            return Node(int(s))

        data = input.split(',')
        queue = deque()
        parent = root = None

        for item in data:
            if item == "null":
                parent = queue.popleft()
            elif item:
                child = createNode(item)
                queue.append(child)
                if root is None:
                    root = child
                else:
                    parent.children.append(child)
        return root




        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))