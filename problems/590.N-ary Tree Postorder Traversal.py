"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        l = []
        if root:
            for x in root.children:
                l.extend(self.postorder(x))
            l.append(root.val)
        return l
            