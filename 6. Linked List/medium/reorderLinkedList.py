# https://leetcode.com/problems/reorder-list/description/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        slow.next = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        first, second = head, prev
        while second:
            firstNxt = first.next
            secondNxt = second.next

            first.next = second
            second.next = firstNxt

            first = firstNxt
            second = secondNxt


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head_even = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
s = Solution()
s.reorderList(head)
s.reorderList(head_even)
