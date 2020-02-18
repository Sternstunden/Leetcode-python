#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.79%)
# Likes:    2596
# Dislikes: 190
# Total Accepted:    524.2K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ret = f = s = ListNode(0)
        ret.next = head

        while f and n != 0:
            f = f.next
            n -= 1
        if not f or n!= 0:
            return ret.next
        while f.next and s.next:
            f = f.next
            s = s.next
        temp = s.next
        if temp:
            s.next = temp.next
        else:
            s.next = None
        return ret.next
        
# @lc code=end

