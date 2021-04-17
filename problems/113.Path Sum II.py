# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sums: int) -> List[List[int]]:
        sumPaths= []
        nodeStack = []
        pathRecordStack = []
        pathRecord = []
        while root or nodeStack:
            if not root:
                root = nodeStack.pop()
                pathRecord = pathRecordStack.pop()
                
            pathRecord.append(root.val)
            #print(pathRecord)
            if sum(pathRecord) == sums and not root.left and not root.right:
                sumPaths.append(pathRecord[:])

            if root.right:
                nodeStack.append(root.right)
                pathRecordStack.append(pathRecord[:])
                #print("pathRecordStack")
                #print(pathRecordStack)
            root = root.left
        
        return sumPaths
            
                