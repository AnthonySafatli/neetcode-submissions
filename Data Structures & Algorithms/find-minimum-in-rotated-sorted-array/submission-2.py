class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if mid <= l or mid >= r:
                break

            if nums[l] > nums[r]:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] < nums[l]:
                    l = mid
                else:
                    r = mid
        
        if nums[l] < nums[r]:
            return nums[l]
        else:
            return nums[r]

                

        