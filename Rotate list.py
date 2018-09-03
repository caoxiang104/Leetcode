# Definition for singly-linked list.
"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL

示例 2:
输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        k = k % n
        if n == 1:
            return head
        pre_node = head
        if k == 0:
            return head
        k = n - k - 1
        while k > 0:
            pre_node = pre_node.next
            k -= 1
        node = pre_node.next
        pre_node.next = None
        temp2 = node
        while temp2.next:
            temp2 = temp2.next
        temp2.next = head
        return node


link = ListNode(1)
link.next = ListNode(2)
# link.next.next = ListNode(3)
# link.next.next.next = ListNode(4)
# link.next.next.next.next = ListNode(5)
s = Solution()
res = s.rotateRight(link, 0)
while res:
    print(res.val)
    res = res.next

