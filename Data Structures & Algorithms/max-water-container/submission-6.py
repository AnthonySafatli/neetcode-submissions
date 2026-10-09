class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        temp_l, temp_r = l, r

        highest = 0
        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])

            if curr_area > highest:
                highest = curr_area

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return highest
        


