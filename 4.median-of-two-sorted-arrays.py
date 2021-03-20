#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        p_sum = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                p_sum.append(nums1[p1])
                p1 += 1
            else:
                p_sum.append(nums2[p2])
                p2 += 1
        while p1 < len(nums1):
            p_sum.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            p_sum.append(nums2[p2])
            p2 += 1
        if len(p_sum) % 2 != 0:
            return p_sum[len(p_sum) // 2] * 1.0
        else:
            return (p_sum[len(p_sum) // 2 - 1] + p_sum[len(p_sum) // 2])/2



        
# @lc code=end

