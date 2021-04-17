"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        if root:
            l.append(root.val)
            for x in root.children:
                l.extend(self.preorder(x))
        return l
#-----------------------------------------------------
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        l = []
        if root:
            nodeStack = [root]
        else:
            nodeStack = []
        while nodeStack != []:
            currNode = nodeStack.pop()
            l.append(currNode.val)
            for x in reversed(currNode.children):
                print(x.val)
                nodeStack.append(x)
        return l