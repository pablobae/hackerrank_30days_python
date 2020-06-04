import sys


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        nodes = [root]
        output = ""
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node.left is not None:
                nodes.append(node.left)

            if output != '':
                output += ' '
            output += str(node.data)

            if node.right is not None:
                nodes.append(node.right)
        print(output)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
