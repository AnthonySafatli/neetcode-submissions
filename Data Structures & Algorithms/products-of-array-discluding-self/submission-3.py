class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_no_zero = 1
        
        for num in nums:
            if not num == 0:
                product_no_zero *= num
            else:
                if product_no_zero != product:
                    return [0] * len(nums)
            product *= num
        
        result = [None] * len(nums)
        for i, num in enumerate(nums):
            if num == 0:
                result[i] = product_no_zero
                continue
            result[i] = product // num
        
        return result
        