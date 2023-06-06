# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # BFS, O(n)
    def serialize(self, root):
        if root == None: return "#"
        bfs = deque([root])
        ans = []
        while bfs:
            curr = bfs.popleft()
            if curr == None:
                ans.append("#")
            else:
                ans.append(str(curr.val))
                bfs.append(curr.left)
                bfs.append(curr.right)
        return ",".join(ans)

    def deserialize(self, data):
        def createNode(strVal):
            if strVal == "#": return None
            return TreeNode(int(strVal))

        if data == "#": return None
        strs = data.split(",")
        root = createNode(strs[0])
        i = 1
        bfs = deque([root])
        while bfs:
            curr = bfs.popleft()
            curr.left = createNode(strs[i])
            curr.right = createNode(strs[i+1])
            i += 2

            if curr.left != None:
                bfs.append(curr.left)
            if curr.right != None:
                bfs.append(curr.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))