'''sample_list=[5,4,1,67,45,23,11]
min=5
max=15
add=0
for i in sample_list:
    if i>=min and i<=max:
        add=add+i
print(add)
'''
# class for node of the tree
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None
     
# function to create a new BST node
def newNode(item):
    return Node(item)

add=0
 
def rangeSumBST(root, low, high):
    
    if root is not None:
        if root.val >= low and root.val <= high:
            global add
            add += root.val
         
        # giving a call to the left and right subtree
        rangeSumBST(root.left, low, high)
        rangeSumBST(root.right, low, high)
 
 
# function to insert a new node
# into the binary search tree
def insert(node, data):
    # base case
    if(node is None):
        return newNode(data)
     
    # if the data is less than the
    # value of the current node
    if(data <= node.val):
        # recur for left subtree
        node.left = insert(node.left, data)
    #otherwise
    else:
        # recur for the right subtree
        node.right = insert(node.right, data)
    # return the node
    return node
  
root = None
root = insert(root, 10)
insert(root, 5)
insert(root, 15)
insert(root, 3)
insert(root, 7)
insert(root, 18)
 
L = 7
R = 15
rangeSumBST(root, L, R)
print(add)
        