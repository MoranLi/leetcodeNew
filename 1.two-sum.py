#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copy = {}
        for i in range(len(nums)):
            if nums[i] not in copy:
                copy[nums[i]] = [i]
            else:
                copy[nums[i]].append(i)
        for n in copy:
            x = target - n
            if x in copy:
                if n == x and len(copy[n]) > 1:
                    return [copy[x][0],copy[n][1]]
                if n != x:
                    return [min(copy[x][0],copy[n][0]),max(copy[x][0],copy[n][0])]
        return [-1,-1]

        
# @lc code=end

