class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        size = len(heights)
        l, r = 0, size - 1
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            largest = max(largest, height * width)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return largest

        # for i in range(size):
        #     for j in range(size):
        #         height = min(heights[i], heights[j])
        #         width = abs(i - j)
        #         largest = max(largest, height * width)
        # return largest


        