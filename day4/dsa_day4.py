def max_depth(root):
    if root is None:
        return 0
    
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return 1 +  max(left_depth, right_depth)


def is_same_tree(first, second):
    if first is None and second is None:
        return True

    if first is None or second is None:
        return False

    if first.value != second.value:
        return False

    return (
        is_same_tree(first.left, second.left)
        and is_same_tree(first.right, second.right)
    )

class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left  = TreeNode(3)

print("depth is:", max_depth(root))

def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root

def is_valid_bst(root, minimum=float("-inf"), maximum=float("inf")):
    if root is None:
        return True

    if root.value <= minimum or root.value >= maximum:
        return False

    return (
        is_valid_bst(root.left, minimum, root.value)
        and is_valid_bst(root.right, root.value, maximum)
    )

def lowest_common_ancestor(root, first, second):
    current = root

    while current is not None:
        if first < current.value and second < current.value:
            current = current.left
        elif first > current.value and second > current.value:
            current = current.right
        else:
            return current

    return None