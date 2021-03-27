#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = 0
        window = []
        chars = set()
        p = 0
        while p < len(s):
            if s[p] in chars:
                window.add(s[p])
                chars
            else:
                window
        
# @lc code=end

