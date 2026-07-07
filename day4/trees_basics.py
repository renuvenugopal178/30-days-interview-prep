class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

print("Root:", root.value)
print("Left child:", root.left.value)
print("Right child:", root.right.value)
print("Left-left child:", root.left.left.value)

def inorder(node):
    if node is None: 
        return None
    
    inorder(node.left)
    print(node.value, end= "")
    inorder(node.right)

print("inorder traversal:")
inorder(root)