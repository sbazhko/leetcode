# https://leetcode.com/problems/copy-list-with-random-pointer/description/

from typing import Optional
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodes = {}
        curr = head
        copy = dummy = Node(-1)
        while curr:
            newNode = Node(curr.val, None, None)
            if curr not in nodes:
                nodes[curr] = newNode
            copy.next = newNode
            copy = copy.next
            curr = curr.next
        curr = head
        copy = dummy.next
        while curr:
            if curr.random:
                copy.random = nodes[curr.random]
            copy = copy.next
            curr = curr.next
        return dummy.next


s = Solution()

node0 = Node(7, Node(13, Node(11, Node(10, Node(1, None)))))
node0.random = None
node0.next.random = node0
node0.next.next.random = node0.next.next.next.next
node0.next.next.next.random = node0.next.next
copy = s.copyRandomList(node0)
