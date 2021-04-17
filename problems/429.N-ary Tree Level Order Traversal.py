"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        l = []
        # level 1
        if root:
            nodeQueue = [root]
        else:
            nodeQueue = []
        while nodeQueue:
            # aggregate all value in the same level
            sameLevelList = [x.val  for x in nodeQueue]
            '''
            sameLevelList = []
            for x in nodeQueue:
                sameLevelList.append(x.val)
            '''
            l.append(sameLevelList)
            # jump to next level
            nodeQueue = [y for x in nodeQueue for y in x.children]
            '''
            nextNodeQueue = []
            for x in nodeQueue:
                for y in x.children:
                    nextNodeQueue.append(y)
            nodeQueue = nextNodeQueue
            '''
        return l
        
        