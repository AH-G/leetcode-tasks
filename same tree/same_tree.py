# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        middle=False
        left=False
        right=False
        if not p and not q:
            return(True)
        elif not p or not q:
            return(False)
        if p.val == q.val:
            middle=True
            if p.left and q.left:
                left=self.isSameTree(p.left,q.left)
                if not left:
                    return(False)
            elif not p.left and not q.left:
                left=True
            elif p.left or q.left:
                left=False

            if p.right and q.right:
                right=self.isSameTree(p.right,q.right)
                if not right:
                    return(right)
            elif not p.right and not q.right:
                right=True
            elif p.right or q.right:
                right=False

        else:
            middle=False
        if middle and left and right:
            return(True)
        else:
            return(False)
