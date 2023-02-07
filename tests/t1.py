import collections
import os.path
import re
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            mid = left if left > right else right
            return mid + 1

        if not root:
            return True
        l = dfs(root.left)
        r = dfs(root.right)
        mid = l - r
        mid = mid if mid > 0 else -mid
        return mid <= 1


if __name__ == '__main__':
    # r = [3, 9, 20, None, None, 15, 7]
    # s = Solution()
    # s.isBalanced(r)
    print(max(1, 2, 3, 444))
    rs=[1,2,3,4,5]
    print(max(rs))
    dict0={'a':1,'b':2}
    print(1 in dict0.values())
    a,b=1,2
    print(a,b)
    a=[1,2,3]
    tel = {'jack': 4098, 'sape': 4139}
    tel1 = {'jack': 4098, 'sape': 4139}
    tel2 = {'jack': 4098, 'sape': 41392}

    print(tel1==tel)
    print(tel2==tel)
    c=collections.Counter(tel)

    # tel['a'] += 1
    print(tel)
    lst=[111,0,1,2,3,4,5,6]
    lst.pop(2)
    print(lst)
    print(lst[1:])
    deges=[[] for x in range(3)]
    print(deges)
    l=len([1,2,3])
    visits = [False * l]
    print(visits,l)
    lst0=[3,4,5]
    print(lst0.pop(0),lst0)
    re.compile()

