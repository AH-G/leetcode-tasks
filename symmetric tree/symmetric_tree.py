# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self,p, q):

        middle=False
        left=False
        right=False

        if not p and not q:
            return(True)
        elif not p or not q:
            return(False)
        if p.val == q.val:
            middle=True
            if p.left and q.right:
                left=self.isSameTree(p.left,q.right)
                if not left:
                    return(False)
            elif not p.left and not q.right:
                left=True
            elif p.left or q.right:
                left=False

            if p.right and q.left:
                right=self.isSameTree(p.right,q.left)
                if not right:
                    return(False)
            elif not p.right and not q.left:
                right=True
            elif p.right or q.left:
                right=False

        else:
            middle=False
        if middle and left and right:
            return(True)
        else:
            return(False)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return(False)
        else:
            return(self.isSameTree(root.left, root.right))
