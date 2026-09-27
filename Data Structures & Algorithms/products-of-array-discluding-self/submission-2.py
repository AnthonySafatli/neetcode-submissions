class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref = [1] * n
        suff = [1] * n

        for i in range(n):
            if i == 0:
                continue
            pref[i] = pref[i-1] * nums[i-1]

        
        for i in reversed(range(n)):
            if i == (n-1):
                continue
            suff[i] = suff[i+1] * nums[i+1]

        result = [None] * n
        for i in range(n):
            result[i] = pref[i] * suff[i]

        return result

        