class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            return TreeNode(key)
        if key < self.root.val:
            self.root.left = self.insert(key)
        else:
            self.root.right = self.insert(key)
        return self.root

    def search(self, key):
        if self.root is None or self.root.val == key:
            return self.root
        if self.root.val < key:
            return self.search(key, self.root.right)
        return self.search(key, self.root.left)

    def delete(self, key):
        if self.root is None:
            return None
        if key < self.root.val:
            self.root.right = self.delete(key, self.root.right)
        elif key > self.root.val:
            self.root.left = self.delete(key, self.root.left)
        else:
            if self.root.left is None and self.root.right is None:
                return None
            elif self.root.left is None:
                return self.root.right
            elif self.root.right is None:
                return self.root.left
            else:
                min_val = min(self.root.left.val, self.root.right.val)
                if self.root.left.val == min_val:
                    self.root = self.delete_min(self.root.right)
                else:
                    self.root = self.delete_min(self.root.left)
                return self.root

    def delete_min(self, node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            min_node = self.find_min(node.right)
            min_node.right = self.delete_min(min_node.right)
            return min_node

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node



# Insertion
bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(5)

# Search
print(bst.search(bst.root, 2).val)  # Output: 2
print(bst.search(bst.root, 7).val)  # Output: None

# Deletion
bst.delete(bst.root, 3)
print(bst.search(bst.root, 3).val)  # Output: None
print(bst.root.right.val)  # Output: 6