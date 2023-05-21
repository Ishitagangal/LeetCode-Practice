class Node:
	
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

# Function to find the Level  Order Successor of a given  Node in Binary Tree
def levelOrderSuccessor(root, key):
	if root == None:
		return None
	
	elif root == key:
		if root.left:
			return root.left
		elif root.right:
			return root.right
		else:
			return None
			
	# level order traversal
	queue = deque([root])

	while queue:
		node = queue.popleft()
		if node.left: queue.append(nd.left)
		if node.right: queue.append(nd.right)
		if node == key: # node found, top of queue is the successor
			break

	return q.popleft()

# Driver Code
if __name__ == "__main__":

	root = Node(20)
	root.left = Node(10)
	root.left.left = Node(4)
	root.left.right = Node(18)
	root.right = Node(26)
	root.right.left = Node(24)
	root.right.right = Node(27)
	root.left.right.left = Node(14)
	root.left.right.left.left = Node(13)
	root.left.right.left.right = Node(15)
	root.left.right.right = Node(19)

	key = root.right.left # node 24

	res = levelOrderSuccessor(root, key)

	if res:
		print("LevelOrder successor of " +
				str(key.value) + " is " +
				str(res.value))
	
	else:
		print("LevelOrder successor of " +
			str(key.value) + " is NULL")

# This code is contributed
# by Rituraj Jain
