#!/env/python
#https://oj.leetcode.com/problems/binary-search-tree-iterator/

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.val:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.pushLeft(root)
        
    def hasNext(self):
        return self.stack
    
    def next(self):
        top = self.stack.pop()
        self.pushLeft(top.right)
        return top.val
        
    def pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left

if __name__ == "__main__":
    num = [2, 1, 5, 3, 4]
    root = TreeNode(num[0])
    for i in range(1, len(num)):
        root.insert(num[i])

    bsi = BSTIterator(root)
    while bsi.hasNext():
         print bsi.next()
