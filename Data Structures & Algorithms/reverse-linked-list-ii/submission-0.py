# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        if left == right:
            return head
        
        count = right - left + 1
        curr = head
        prev = None

        while left > 1:
            prev = curr
            curr = curr.next
            left -=1


        def reverse(start, count):
            prev = None
            curr = start
            
            while count:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1

            start.next = curr

            return prev

        if prev:
            prev.next = reverse(curr, count)
        else:
            head = reverse(curr, count)


        return head
        

        
        