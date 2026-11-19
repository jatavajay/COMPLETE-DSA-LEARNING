# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:

            # Connect odd nodes
            odd.next = even.next
            odd = odd.next

            # Connect even nodes
            even.next = odd.next
            even = even.next

        # Join odd list with even list
        odd.next = evenHead
        return head