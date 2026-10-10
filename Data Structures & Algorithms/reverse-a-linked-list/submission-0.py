# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            return None

        result = ListNode(head.val)

        curr = head
        while curr.next is not None:
            next = ListNode(curr.next.val, result)
            result = next
            curr = curr.next

        return result

        