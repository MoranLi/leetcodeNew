#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        copy = {}
        for n in nums:
            if n not in copy:
                copy[n] =0
            copy[n] += 1
        ans = set()
        for n in nums:
            for m in nums:
                o = 0 -  n  - m
                if o in copy:
                    if o == m and m == n:
                        if copy[n] > 2:
                            ans.add((n, o, m))
                    if o == m and m != n:
                        if copy[o] > 1:
                            res = sorted([n,m,o])
                            ans.add(tuple(res))
                    if o == n and m != n:
                        if copy[n] > 1:
                            res = sorted([n,m,o])
                            ans.add(tuple(res))
                    if n == m and o != n:
                        if copy[m] > 1:
                            res = sorted([n,m,o])
                            ans.add(tuple(res))
                    if o != m and m != n and o != n: 
                        res = sorted([n,m,o])
                        ans.add(tuple(res))
        return ans


                    

        
# @lc code=end

