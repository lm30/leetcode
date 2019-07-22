# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        
        for i in xrange(len(lists)): # go through list
            if lists[i]:
                # put into heap, (val, list)
                heapq.heappush(heap, (lists[i].val, lists[i]))
        
        prehead = ListNode(None)
        ptr = prehead
        while heap:
            num, node = heapq.heappop(heap) # get smallest val from heap
            ptr.next = node # link it up to the linked list
            ptr = ptr.next
            if node.next: # if has a link to it, add that pt of the list to the heap
                heapq.heappush(heap,(node.next.val,node.next)) 
        return prehead.next