# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def height(self,root):
        if root == None:
            return 0
        leftheight=self.height(root.left)+1
        rightheight=self.height(root.right)+1
        return(max(leftheight,rightheight))

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return(True)
        else:
            difference=abs(self.height(root.left)-self.height(root.right))
            if difference<=1:
                leftbalance=self.isBalanced(root.left)
                rightbalance=self.isBalanced(root.right)
                if not leftbalance or not rightbalance:
                    return(False)
                else:
                    return(True)
            else:
                return(False)
