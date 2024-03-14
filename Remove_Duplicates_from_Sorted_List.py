'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.
Example 1:


Input: head = [1,1,2]
Output: [1,2]

Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def asList(self):
        current = self
        list = []
        while current != None:
            list.append(current.val)
            current = current.next
        return list

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        if(head == None):
            return head
        
        while current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
    
        return head
                

if __name__ == "__main__":
    s =  Solution()
    list = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))
    result = s.deleteDuplicates(None)
    if(result == None):
        print("Empty")
    else:
        print(result.asList())