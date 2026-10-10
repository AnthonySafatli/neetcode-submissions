# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        result = None
        curr = None
        curr1 = list1
        curr2 = list2

        if curr1.val > curr2.val:
            result = ListNode(curr2.val)
            curr2 = curr2.next
        else:
            result = ListNode(curr1.val)
            curr1 = curr1.next

        curr = result
        while curr1 is not None or curr2 is not None:
            if curr1 is None or (curr2 is not None and curr1.val > curr2.val):
                curr.next = ListNode(curr2.val)
                curr = curr.next
                curr2 = curr2.next
            else:
                curr.next = ListNode(curr1.val)
                curr = curr.next
                curr1 = curr1.next

        return result

            


        