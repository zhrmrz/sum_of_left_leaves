class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False

def leftLeavesSum(root):
    res = 0
    if root is not None:
        if isLeaf(root.left):
            res += root.left.key
        else:
            res += leftLeavesSum(root.left)
        res += leftLeavesSum(root.right)
    return res

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.right.left = Node(23)
root.right.right = Node(52)
root.right.right.left = Node(50)
root.left.left = Node(5)
root.left.right = Node(12)
root.left.right.right = Node(12)
print(leftLeavesSum(root))
