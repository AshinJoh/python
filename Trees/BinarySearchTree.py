class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, root, val):
        if val < root.val:
            if root.left is None:
                root.left = Node(val)
            else:
                self._insert(root.left, val)
        
        if val > root.val:
            if root.right is None:
                root.right = Node(val)
            else:
                self._insert(root.right, val)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")

tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)

inorder(tree.root)
print("\n")
postorder(tree.root)
print("\n")
preorder(tree.root)