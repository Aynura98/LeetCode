# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        lleft = self.minDepth(root.left)        
        lright = self.minDepth(root.right)
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return lright + 1
        if root.right == None:
            return lleft + 1

        return min(lleft, lright) + 1
    
if __name__ == "__main__":
    s =  Solution()
    result = s.minDepth(TreeNode(1,TreeNode(2, None, None), None))
    print(result) 