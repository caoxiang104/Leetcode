# -*- coding:utf-8 -*-
"""
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists1):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        temp_node = head
        lists = []
        for i in range(len(lists1)):
            if lists1[i]:
                lists.append(lists1[i])
        if not lists:
            return None
        lists.sort(key=lambda x: x.val, reverse=True)
        while lists:
            temp = lists.pop()
            temp_node.next = temp
            temp_node = temp_node.next
            if temp.next:
                temp = temp.next
                if lists and temp.val < lists[-1].val or not lists:
                    lists.append(temp)
                else:
                    i = len(lists) - 1
                    while i >= 0:
                        if temp.val > lists[i].val:
                            i -= 1
                        else:
                            break
                    lists.insert(i+1, temp)
        return head.next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
list3 = ListNode(2)
list3.next = ListNode(6)
s = Solution()
out = s.mergeKLists([list1, list2, list3])
while out:
    print(out.val, end=" ")
    out = out.next