import os
import sys
import csv
from Airport import Airport

class bst:
    global inOrderNodes, preOrderNodes, postOrderNodes
    inOrderNodes = []
    preOrderNodes = []
    postOrderNodes = []
    root=None
    
    def createTree(self, a): 
        for x in a:
            n = x.split(":")
            self.put(n[0], n[1])


    # searches for node with the same key value as given key
    def search(self, key):
        temp = self.root
        while temp is not None:
            if temp.key == key:
                return temp
            elif key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        return None


    def put(self, key, val):
        self.root = self.put2(self.root, key, val)
        

    def put2(self, node, key, val):
        if node is None:
            #key is not in tree, create node and return node to parent
            return Node(key, val)
        if key < node.key:
            # key is in left subtree
            node.left = self.put2(node.left, key, val)
        elif key > node.key:
            # key is in right subtree
            node.right = self.put2(node.right, key, val)
        else:
            # key exists in tree, update node value to given value
            node.val = val
        return node
    
    
    # for a right-right imbalance
    def rotateLeft(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        
        self.update_height(x)
        self.update_height(node)
        
        return x
                
    
    # for a left-left imbalance
    def rotateRight(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        
        self.update_height(node)
        self.update_height(x)
        
        return x
        
        
    # # for a left-right imbalance, first rotate left to become LL-imbalance, then rotate right
    # def rotateLeftRight(self, node):
    #     node.left = self.rotateLeft(node.left)
    #     node = self.rotateRight(node)
    #     return node
        
        
    # #for a right-left imbalance, first rotate right to become RR-imbalance, then rotate left
    # def rotateRightLeft(self, node):
    #     node.right = self.rotateRight(node.right)
    #     node = self.rotateLeft(node)
    #     return node
    
    
    # def rotate(self, node, balFactor):
    #     leftSubTreeBalFactor = self.calculateBalanceFactor(node.left)
    #     rightSubTreeBalFactor = self.calculateBalanceFactor(node.right)
    #     # if node balance factor 2 and above and node.left balance factor is 1, means left-left imbalance
    #     if balFactor == 2 and leftSubTreeBalFactor == 1:
    #         node = self.rotateRight(node)
    #     # if node balance factor 2 and above node.left balance factor is -1, means left-right imbalance
    #     elif balFactor == 2 and leftSubTreeBalFactor == -1:
    #         node = self.rotateLeftRight(node)
    #     # if node balance factor is -2 and node.right balance is 1, means right-left imbalance
    #     elif balFactor == -2 and rightSubTreeBalFactor == 1:
    #         node = self.rotateRightLeft(node)
    #     # if node balance factor is -2 and node.right balance is -1, means right-right imbalance
    #     elif balFactor == -2 and rightSubTreeBalFactor == -1:
    #         node = self.rotateLeft(node)
    #     return node
            
        
    # # finds balance factor of a node by taking left subtree height - right subtree height
    # def calculateBalanceFactor(self, node):
    #     if node is None:
    #         return 0
    #     leftSubTreeHeight = self.altHeight(node.left)
    #     rightSubTreeHeight = self.altHeight(node.right)
    #     return leftSubTreeHeight - rightSubTreeHeight
    
    
    def balance(self, node):
        # update height of current node
        self.update_height(node)
        
        # check balance factor
        balance = self.balance_factor(node)
        
        # left-left imbalance
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.rotateRight(node)
        
        # right-right imbalance
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.rotateLeft(node)
        
        # Left-Right Case
        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        # Right-Left Case
        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node
    
    
    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)
        
    
    # AVL insert recursive helper function
    def AVLInsert2(self, node, key, val):
        if node is None:
            return Node(key, val)
        
        if key < node.key:
            node.left = self.AVLInsert2(node.left, key, val)
        elif key > node.key:
            node.right = self.AVLInsert2(node.right, key, val)     
        else:
            return node
        
        return self.balance(node)
    
    
    # AVL tree insertion
    def AVLInsert(self, key, val):
        self.root = self.AVLInsert2(self.root, key, val)
        
    
    #Create a AVL Tree, you are allowed to create other helper functions
    def createBalancedTree(self, a):
        self.clearTraverseArrays()
        self.root = None
        for x, y in a.items():
            # n = x.split(":")
            self.AVLInsert(x, y)

            
    #preOrder Traversal, this should be a recursive function
    def preOrder(self, root):
        if root is None:
            return
        preOrderNodes.append(root.key + ":" + root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)
        return preOrderNodes
    
        
    #inOrder Traversal, this should be a recursive function
    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        inOrderNodes.append(root.key + ":" + root.val)
        self.inOrder(root.right)
        return inOrderNodes
                     
             
    #postOrder Traversal, this should be a recursive function
    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        postOrderNodes.append(root.key + ":" + root.val)
        return postOrderNodes
        
      
    #given a key, obtain its value
    def get(self, key):
        temp = self.root
        while temp is not None:
            if temp.key == key:
                return temp.val
            elif key < temp.key:
                temp = temp.left
            else:
                temp = temp.right
        return None
         
         
    #given a key, find the node and obtain the depth, you are allowed to create other helper functions
    def depth(self, key):
        depth = 0
        temp = self.root
        while temp is not None:
            if temp.key == key:
                return depth
            elif key < temp.key:
                depth += 1
                temp = temp.left
            else:
                depth += 1
                temp = temp.right
        return None
    
    
    #update height helper function
    def update_height(self, node):    
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    
    #given a node, return height
    def height(self, node):
        if not node:
            return 0
        else:
            return node.height
        
    
    # given a node, find it's height
    def altHeight(self, node):
        if node is None:
            return -1
        else:
            height = self.findHeight(node)
            return height
    
    
    def findSize(self, node):
        if node is None:
            return 0
        else:
            return (self.findSize(node.left) + 1 + self.findSize(node.right))
    
         
    #given a key, find the node and obtain the size, you are allowed to create other helper functions
    def size(self, key):
        # find the node with key equal to given key
        temp = self.search(key)
        # if temp is none means no node exist with key equal to given key
        if temp is None:
            return None
        else:
            # call findSize recursive helper function with temp node, returns size of temp node
            size = self.findSize(temp)
            return size
        
        
    def delete2(self, node, key):
        if node is None:
            return None
        # search for node that has key equal to given key
        if key < node.key:
            node.left = self.delete2(node.left, key)
        elif key > node.key:
            node.right = self.delete2(node.right, key)
        else:
            # case 0 & case 1, where node has 1 or no edges/child
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            # case 2, where node has 2 edges/child
            t = node
            node = self.min(t.right)
            node.right = self.deleteMin2(t.right)
            node.left = t.left
        return node
        

    #given a key, delete the node, you are allowed to create other helper functions
    def delete(self, key):
        # find the node with key equal to given key
        node = self.delete2(self.root, key)
        if node is None:
            return False
        else:
            self.clearTraverseArrays()
            return True
          
       
    # finds the node with smallest key in tree
    def min(self, node):
        while node is not None:
            if node.left is None:
                return node
            node = node.left
            
            
    def deleteMin(self):
        self.root = self.deleteMin2(self.root)
        
    
    def deleteMin2(self, node):
        if node.left is None:
            return node.right
        node.left = self.deleteMin2(node.left)
        return node
       
       
    def clearTraverseArrays(self):
        global inOrderNodes, preOrderNodes, postOrderNodes
        inOrderNodes = []
        preOrderNodes = []
        postOrderNodes = []
        
       
class Node:
    left = None
    right = None
    key = ''
    val = None
    height = 0

    def __init__(self, key, val):
        self.key = key
        self.val = val


# # Create a list of Airport objects
# airport_objects = create_airport_objects()

# # Create a list of strings in the desired format
# airport_data_list = [f"{airport.IATA}: {airport.longitude}, {airport.latitude}" for airport in airport_objects]

# # print("Data:", data)
# # # Print the resulting list
# print(airport_data_list)

# bst = bst()
# bst.createTree(airport_data_list)

# key1 = input("Input key for the IATA:\n")
# key2 = input("Input key for the IATA:\n")

# if key1 != '-':
#     print("The longitude & latitude of", key1, "is", bst.get(key1))

# if key2 != '-':
#     print("The longitude & latitude of", key2, "is", bst.get(key2))
