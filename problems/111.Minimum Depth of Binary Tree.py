class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        return self.getDepth(root,0)
    
    def getDepth(self,root,depth):
        if not root:
            return float('inf') # return inf when the search reaches beyond node just not to impact minimum depths we need to get
        depth += 1
        if not root.left and not root.right:
            return depth # return depth for that leaf
        return min(self.getDepth(root.left,depth),self.getDepth(root.right,depth))
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        if not root.left and not root.right: 
            return 1
        if root.left:
            left = self.minDepth(root.left)
        else 
            left = float('inf')
        if root.right:
            right = self.minDepth(root.right)
        else 
            right = float('inf')
        
        return 1 + min(left,right)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = []
        queue.append(root)
        queue.append(1)
        
        while True:
            node = queue[0]
            m_min = queue[1]
            queue = queue[2:]
            
            if not node.left and not node.right: return m_min
            
            if node.left:
                queue.append(node.left)
                queue.append(m_min+1)
            if node.right:
                queue.append(node.right)
                queue.append(m_min+1)
        