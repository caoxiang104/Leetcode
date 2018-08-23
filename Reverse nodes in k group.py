class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        pre_node = ListNode(0)
        pre_node.next = head
        out = pre_node
        next_node = head
        i = 0
        while next_node:
            i += 1
            if i % k == 0:
                pre_node = self.reverse(pre_node, next_node.next)
                next_node = pre_node.next
            else:
                next_node = next_node.next
        return out.next

    def reverse(self, pre_node, next_node):  # pre_node:a
        b = pre_node.next
        c = b.next
        while c != next_node:
            b.next = c.next
            c.next = pre_node.next
            pre_node.next = c
            c = b.next
        return b


s = Solution()
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list1.next.next.next = ListNode(6)
out = s.reverseKGroup(list1, 3)
while out:
    print(out.val, end=" ")
    out = out.next