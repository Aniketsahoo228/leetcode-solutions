class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)      # handles removing the head itself
        fast = slow = dummy

        for _ in range(n + 1):         # make a gap of n nodes between slow and fast
            fast = fast.next

        while fast:                    # move both until fast falls off the end
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next     # skip the nth node from the end
        return dummy.next