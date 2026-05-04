# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        def reverse(node):
            prev = None
            curr = node

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev
        
        list2 = reverse(slow.next)
        slow.next = None
        list1 = head
        dummy = temp = ListNode(0)

        while list1 and list2:
            dummy.next = list1
            dummy = dummy.next
            list1 = list1.next

            dummy.next = list2
            dummy = dummy.next
            list2 = list2.next
        
        if list1:
            dummy.next = list1
