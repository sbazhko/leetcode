# https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = slow.next
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


l1 = ListNode(3, ListNode(2, ListNode(0, ListNode(-4, None))))
l1.next.next.next.next = l1

s = Solution()
isCycle = s.hasCycle(l1)
