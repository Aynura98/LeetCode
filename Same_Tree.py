'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def helper(root1, root2):
            if(root1 == None and root2 == None): 
                return True
            elif (root1 == None):
                return False
            elif (root2 == None):
                return False
            
            left_result = helper(root1.left, root2.left)
            right_result = helper(root1.right, root2.right)
            return left_result and right_result and root1.val == root2.val
        
        result = helper(p,q)
        return result
    
if __name__ == "__main__":
    s =  Solution()
    result = s.isSameTree(TreeNode(1, TreeNode(2), None), TreeNode(1, None, TreeNode(3)))
    print(result)   
