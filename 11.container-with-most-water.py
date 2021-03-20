#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_cap = 0
        while left < right:
            cap = min(height[left], height[right]) * (right - left)
            if max_cap < cap:
                max_cap = cap
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_cap
        
# @lc code=end

