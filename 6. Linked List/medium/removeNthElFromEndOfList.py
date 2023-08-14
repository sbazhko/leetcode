# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            n -= 1
            right = right.next
        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


s = Solution()
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
head2 = ListNode(1, ListNode(2, None))
head3 = ListNode(1, None)
head1 = s.removeNthFromEnd(head1, 2)
head2 = s.removeNthFromEnd(head2, 1)
head3 = s.removeNthFromEnd(head3, 1)
print()
