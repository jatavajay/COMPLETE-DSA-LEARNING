# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        visited = {}
        curr = head
        pos = 0

        while curr:
            if curr in visited:
                return curr

            visited[curr] = pos
            curr = curr.next
            pos += 1

        return None
