# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        result = []
        n=set(nums)
        current = head
        while current:
            if current.val not in n:
                result.append(current.val)
            current = current.next
        if not result:
            return None
        new_head = ListNode(result[0])
        current = new_head
        for val in result[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return new_head
        


####Optimised approach####
class Solution(object):
    def modifiedList(self, nums, head):
        num_set = set(nums)
        dummy = ListNode(0)
        current = dummy
        while head:
            if head.val not in num_set:
                current.next = head
                current = current.next
            head = head.next
        current.next = None
        return dummy.next