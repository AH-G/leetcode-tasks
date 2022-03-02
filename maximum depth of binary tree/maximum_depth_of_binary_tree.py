# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepthCalculator(self,root,counter):
        leftcount=1
        rightcount=1
        if root.left:
            leftcount=self.maxDepthCalculator(root.left,counter)+1
        if root.right:
            rightcount=self.maxDepthCalculator(root.right,counter)+1
        counter=max(leftcount,rightcount)
        return(counter)
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return(0)
        else:
            counter=1
            return(self.maxDepthCalculator(root,counter))
