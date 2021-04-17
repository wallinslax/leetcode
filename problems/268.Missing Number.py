class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N=len(nums)
        sumNums = (N+1)*N/2
        return int(sumNums - sum(nums))