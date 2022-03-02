# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root=int(len(nums)/2)
        if not nums:
            return(None)
        tree=TreeNode(nums[root])

        if root==0:
            return(tree)
        else:
            tree.left=self.sortedArrayToBST(nums[:root])
            tree.right=self.sortedArrayToBST(nums[root+1:])
            return(tree)
