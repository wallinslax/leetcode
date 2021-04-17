class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if nums == []:
            return -1
        nums.sort()
        preValue = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == preValue:
                return nums[i]
            else:
                preValue = nums[i]