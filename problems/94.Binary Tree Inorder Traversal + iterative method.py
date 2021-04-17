# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        if root:
            l.extend(self.inorderTraversal(root.left))
            l.append(root.val)
            l.extend(self.inorderTraversal(root.right))
        return l
#--------------------------------------------------------------
# iterative method
# Inordeer is LCR
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        stack = []
        currNode = root
        while currNode or stack!=[]:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
            currNode = stack.pop()
            l.append(currNode.val)
            currNode = currNode.right
        return l
            
    		

        