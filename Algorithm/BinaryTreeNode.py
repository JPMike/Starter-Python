class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "{}".format(self.data)


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    @staticmethod
    def create():
        pass
