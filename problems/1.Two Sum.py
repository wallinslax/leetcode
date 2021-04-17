class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            #temp_nums = nums
            complement = target - val           
            if complement in nums[(idx+1):] :
                #if nums.index(x) != nums.index(complement):
                return [idx, nums[(idx+1):].index(complement)+(idx+1)]