# https://leetcode.com/problems/reverse-linked-list/description/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head = prev
        return head

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def reverse(currPtr, prevPtr):
            if not currPtr:
                return prevPtr
            tmp = currPtr.next
            currPtr.next = prevPtr
            prevPtr = currPtr
            return reverse(tmp, currPtr)
        return reverse(head, None)


head1 = ListNode(0, ListNode(1, ListNode(
    2, ListNode(3, ListNode(4, ListNode(5, None))))))
head2 = ListNode(1, ListNode(2, None))
newHead1 = Solution().reverseListRecursive(head1)
newHead2 = Solution().reverseListRecursive(head2)
