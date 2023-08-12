# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1 or list2:
            tail.next = list1 if list1 else list2
        return dummy.next


s = Solution()

mergedList1 = s.mergeTwoLists(list1=ListNode(1, ListNode(5, None)),
                              list2=ListNode(2, ListNode(3, ListNode(6, None))))
mergedList2 = s.mergeTwoLists(None, None)
mergedList3 = s.mergeTwoLists(None, ListNode(0, None))
mergedList4 = s.mergeTwoLists(ListNode(0, None), None)
mergedList5 = s.mergeTwoLists(ListNode(2, None), ListNode(1, None))
