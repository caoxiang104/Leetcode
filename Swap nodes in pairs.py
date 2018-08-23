# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp


s = Solution()
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list1.next.next.next = ListNode(6)
out = s.swapPairs(list1)
while out:
    print(out.val, end=" ")
    out = out.next