class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, num in enumerate(nums):
            try:
                i2 = nums[i1 + 1:].index(target - num) + i1 + 1
                return [i1, i2]
            except:
                continue
        