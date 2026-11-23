# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None :
            return head
        len = 0
        curr = head
        while (curr):
            curr = curr.next
            len +=1

        target = len-n
        if target ==0:
            return head.next

        temp = 0
        curr = head
        while (curr):
            if temp == target-1:
                curr.next  = curr.next.next
                break
            temp +=1
            curr = curr.next
        return head