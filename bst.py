class bst:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# A utility function to insert
# a new node with the given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return bst(key)
 
    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
 
    # Return the (unchanged) node pointer
    return node
 
# Utility function to search a key in a BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root
 
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
 
    # Key is smaller than root's key
    return search(root.left, key)
 
# Driver Code
if __name__ == '__main__':
    root = None
    root = insert(root, "singapore")
    insert(root, "jakarta")
    insert(root, "paris")
    insert(root, "warsaw")
    insert(root, "berlin")
    insert(root, "london")
    insert(root, "us")
 
    # Key to be found
    key = "us"
 
    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")
 
    key = "kellyland"
 
    # Searching in a BST
    if search(root, key) is None:
        print(key, "not found")
    else:
        print(key, "found")