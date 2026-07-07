class TreeNode:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = TreeNode(value)


        if self.root is None:
            self.root = new_node
            return
        
        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            elif value > current.value:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

            else:
                return
    def search(self, value):
        current = self.root


        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    
    def inorder(self, node):
        if node is None:
            return
        
        self.inorder(node.left)
        print(node.value, end="")
        self.inorder(node.right)


bst = BinarySearchTree()

for number in [10,5,15,3,7,20]:
    bst.insert(number)

print("inorder:")
bst.inorder(bst.root)
print("\nsearch 7:", bst.search(7))
print("search 12:", bst.search(12))
                
           

