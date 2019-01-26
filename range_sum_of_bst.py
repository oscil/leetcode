vals = [10, 5, 15, 3, 7, None, 18]
L = 7
R = 15


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def addVal(node: TreeNode, val):
    if val is None:
        return
    if node.val > val and (node.left is not None):
        addVal(node.left, val)
    elif node.val < val and (node.right is not None):
        addVal(node.right, val)
    else:
        if node.val < val:
            node.right = TreeNode(val)
        else:
            node.left = TreeNode(val)


def getSum(node: TreeNode, L, R):
    out = 0
    if (node.val >= L) and (node.val <= R):
        out += node.val
    if node.val >= L and node.left:
        out += getSum(node.left, L, R)
    if node.val <= R and node.right:
        out += getSum(node.right, L, R)
    return out



#-----------------------------------

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        out = 0
        if root is None:
            return out
        if (root.val >= L) and (root.val <= R):
            out += root.val
        if root.val >= L:
            out += self.rangeSumBST(root.left, L, R)
        if root.val <= R:
            out += self.rangeSumBST(root.right, L, R)
        return out


if __name__ == '__main__':
    root = TreeNode(vals[0])
    for v in vals[1:]:
        addVal(root, v)
    res = getSum(root, L, R)
    print(res)


