# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:33:40 2021

@author: Abeg
"""
#BST WITH PRE,POST,IN order traversal
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
 
# A utility function to insert 
# a new node with the given key
def minValueNode( node): 
    current = node 
  
    # loop down to find the leftmost leaf 
    while(current.left is not None): 
        current = current.left  
  
    return current  

def deleteNode(root, key): 
  
    # Base Case 
    if root is None: 
        return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    if key < root.key: 
        root.left = deleteNode(root.left, key) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    elif(key > root.key): 
        root.right = deleteNode(root.right, key) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
    else: 
          
        # Node with only one child or no child 
        if root.left is None : 
            temp = root.right  
            root = None 
            return temp  
              
        elif root.right is None : 
            temp = root.left  
            root = None
            return temp 
  
        temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        root.key = temp.key 
  
        # Delete the inorder successor 
        root.right = deleteNode(root.right , temp.key) 
  
  
    return root  

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 
# A utility function to do inorder tree traversal
def search(root,key):
     
    # Traverse untill root reaches  
    # to dead end  
    while root != None: 
          
        # pass right subtree as new tree  
        if key > root.key:  
            root = root.right 
  
        # pass left subtree as new tree 
        elif key < root.key: 
            root = root.left  
        else: 
            return True # if the key is found return 1  
    return False
 
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.key)
        inorder(root.left)
        inorder(root.right)
def postorder(root):
    if root:
        inorder(root.left)
        inorder(root.right)
        print(root.key)
 
 
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
r = Node(50)
r = insert(r, 75)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)
print(search(r,20))
print("\nDelete 20")
root = deleteNode(r, 20) 
print("Inorder traversal of the modified tree")
print("preorder")
preorder(root)
print("postorder")
postorder(root)
