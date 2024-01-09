#Python code for the above approach
# Binary Tree Node
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

# Returns new Node with data as
# input to below function.
def new_node(d):
	temp = Node(d)
	return temp

# Function to store the leaf nodes of the tree
def collect_leaf_nodes(root, store_leaf):
	if not root.left and not root.right:
		store_leaf.append(root.data)
	if root.left:
		collect_leaf_nodes(root.left, store_leaf)
	if root.right:
		collect_leaf_nodes(root.right, store_leaf)

# iterative function.
# returns true if leaf traversals
# are same, else false.
def is_same(root1, root2):
	store_leaf_tree1, store_leaf_tree2 = [], []
	collect_leaf_nodes(root1, store_leaf_tree1)
	collect_leaf_nodes(root2, store_leaf_tree2)
	return store_leaf_tree1 == store_leaf_tree2

# Driver Code
if __name__ == "__main__":
	root1 = new_node(1)
	root1.left = new_node(2)
	root1.right = new_node(3)
	root1.left.left = new_node(4)
	root1.right.left = new_node(6)
	root1.right.right = new_node(7)

	root2 = new_node(0)
	root2.left = new_node(1)
	root2.right = new_node(5)
	root2.left.right = new_node(4)
	root2.right.left = new_node(6)
	root2.right.right = new_node(7)

	if is_same(root1, root2):
		print("Same")
	else:
		print("Not Same")
