class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        
        def getHeightHelper(node, level):
            if not node:
                return level - 1
            result = level
            if node.right:
                result = max(result, getHeightHelper(node.right, level+1))
            if node.left:
                result = max(result, getHeightHelper(node.left, level+1))
            return result
        
        if not root:
            return 0
        return getHeightHelper(root, 0)


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height) 