# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root,root)
    def isMirror(self,leftNode: TreeNode,rightNode: TreeNode) -> bool:
        if leftNode == None and rightNode == None:
            return True
        elif leftNode == None or rightNode == None:
            return False
        else:
            return leftNode.val==rightNode.val and self.isMirror(leftNode.left,rightNode.right) and self.isMirror(leftNode.right,rightNode.left)

'''Two trees are a mirror reflection of each other if:
Their two roots have the same value.
The right subtree of each tree is a mirror reflection of the left subtree of the other tree.'''