

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def similar_tree(a,b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return a.data==b.data and similar_tree(a.left,b.left) and similar_tree(a.right,b.right)

    return False

root1=Node(1)
root1.left=Node(2)
root1.right=Node(3)

root2=Node(1)
root2.left=Node(2)
root2.right=Node(2)

print(similar_tree(root1,root2))