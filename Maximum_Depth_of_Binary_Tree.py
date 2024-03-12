# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        lleft = self.maxDepth(root.left)
        lright = self.maxDepth(root.right)

        return max(lleft,lright) + 1
if __name__ == "__main__":
    s =  Solution()
    result = s.maxDepth(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7))))
    print(result) 