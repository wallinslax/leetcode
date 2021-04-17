# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Follow up: Recursive solution is trivial, could you do it iteratively?
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        stack = []
        currNode = root
        while currNode or stack != []:
            while currNode:
                print(currNode.val)
                l.append(currNode.val)
                if currNode.right:
                    stack.append(currNode.right)
                currNode = currNode.left
            if stack != []:
                currNode = stack.pop()
        return l