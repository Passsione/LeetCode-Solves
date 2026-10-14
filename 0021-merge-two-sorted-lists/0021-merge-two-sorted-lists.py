# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        l1 = [list1.val]
        pos = list1.next
        while pos:
            l1.append(pos.val)
            pos = pos.next

        l2 = [list2.val]
        pos = list2.next
        while pos:
            l2.append(pos.val)
            pos = pos.next

        l1.extend(l2)
        
        l1.sort(reverse=True)
        last_node = ListNode(l1[0])
        l1.pop(0)
        for n in l1:
            temp = ListNode(n, last_node)
            last_node = temp


        return last_node

        