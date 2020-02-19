#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (38.03%)
# Likes:    3726
# Dislikes: 238
# Total Accepted:    547K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l,r):
            dummy = cur = ListNode(0)
            while l and r:
                if l.val < r.val:
                    cur.next  = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next
            cur.next = l or r
            return dummy.next

        if not lists:
            return

        n = len(lists)
        if n == 1:
            return lists[0]
        
        mid = n//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return merge(l,r)
        
# @lc code=end
