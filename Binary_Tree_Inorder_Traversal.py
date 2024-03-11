'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]'''
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

    
class Solution(object):
    
        
    def inorderTraversal(self, root):
        def helper(root, result):
            if(root == None): 
                return
            
            helper(root.left, result)
            result.append(root.val)
            helper(root.right, result)  

        result = []
        helper(root,result)
        return result
        """
        :type root: TreeNode
        :rtype: List[int]
        """
    
    

if __name__ == "__main__":
    s =  Solution()
    result = s.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3))))
    print(result)   