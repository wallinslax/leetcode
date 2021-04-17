class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        globalMax = float('-inf')
        localMax = float('-inf')
        for x in nums:
            '''
            localMax = localMax + x
            if  x > (localMax):
                localMax = x
            '''
            localMax = max(x, localMax+x)    
            globalMax = max(globalMax,localMax)
        return globalMax