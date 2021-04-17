# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    #classTreeList = [1,2,4]
    #currPosition = -1
    def __init__(self, root: TreeNode):
        self.treeList = self.inorderTraversal(root)
        self.currPosition = -1

    def next(self) -> int:
        self.currPosition +=1
        if self.currPosition<len(self.treeList):
            return self.treeList[self.currPosition]
        """
        @return the next smallest number
        """
        

    def hasNext(self) -> bool:
        if self.currPosition+1<len(self.treeList):
            return True
        else:
            return False
        """
        @return whether we have a next smallest number
        """
    def inorderTraversal(self, root: TreeNode) -> list:
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
        


# Your BSTIterator object will be instantiated and called as such:
#obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()