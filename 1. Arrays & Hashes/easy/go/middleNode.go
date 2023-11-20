func middleNode(head *ListNode) *ListNode {
    fast := head
    slow := head
    for fast != nil {
        if fast.Next == nil {
            break;
        }
        slow = slow.Next
        fast = fast.Next.Next
    }
    return slow
}