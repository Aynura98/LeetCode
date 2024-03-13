# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)
        result = left_sum or right_sum
        return result
if __name__ == "__main__":
    s =  Solution()
    result = s.hasPathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7, None, None),TreeNode(2, None, None)), None), TreeNode(8, TreeNode(13, None, None), TreeNode(4, None, TreeNode(1, None, None)))), 18)
    print(result) 