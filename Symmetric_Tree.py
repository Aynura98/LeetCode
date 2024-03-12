# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, left_root, right_root):
        if (left_root == None and right_root == None): 
            return True
        if (left_root == None or right_root == None):
            return False
        if left_root.val != right_root.val:
            return False
        
        return self.helper(left_root.left, right_root.right) and self.helper(left_root.right, right_root.left)
    
if __name__ == "__main__":
    s =  Solution()
    result = s.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))))
    print(result)   
