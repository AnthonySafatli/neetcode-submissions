class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for num in nums:
            if not counts.get(num, False):
                counts[num] = True
            else:
                return True

        return False
            
        