'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:


Input: head = [1,1,2]
Output: [1,2]

Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]'''
# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while head:
            if current == current.next:
                


if __name__ == "__main__":
    s =  Solution()
    result = s.mergeTwoLists([1,2,4], [1,3,4])
    print(result)