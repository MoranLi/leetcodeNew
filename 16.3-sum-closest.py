#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        copy = {}
        for n in nums:
            if n not in copy:
                copy[n] =0
            copy[n] += 1
        ans = set()
        cloest = -target
        for n in nums:
            for m in nums:
                o = target -  n  - m
                if o in copy:
                    return target
                else:
                    
        return ans
        
# @lc code=end

