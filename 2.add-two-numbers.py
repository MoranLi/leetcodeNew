#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        addon = 0
        head = ListNode()
        p = head
        while l1 and l2:
            sumx = l1.val + l2.val + addon
            if sumx >= 10:
                addon = 1
                sumx -= 10
            else:
                addon = 0
            p.next = ListNode()
            p.next.val = sumx
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            sumx = l1.val + addon
            if sumx >= 10:
                addon = 1
                sumx -= 10
            else:
                addon = 0
            p.next = ListNode()
            p.next.val = sumx
            p = p.next
            l1 = l1.next
        while l2:
            sumx = l2.val + addon
            if sumx >= 10:
                addon = 1
                sumx -= 10
            else:
                addon = 0
            p.next = ListNode()
            p.next.val = sumx
            p = p.next
            l2 = l2.next
        if addon > 0:
            p.next = ListNode()
            p.next.val = 1
        return head.next



        
# @lc code=end

