# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)

        dummy = head = ListNode(0)

        while heap:
            _, i, node = heapq.heappop(heap)

            dummy.next = node
            dummy = dummy.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next
