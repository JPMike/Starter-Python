import unittest
import queue


class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    NULL_SYMBOL = 'null'
    DELIMITER = ','

    def serialize(self, root):
        if root is None:
            return Codec.NULL_SYMBOL + Codec.DELIMITER
        else:
            return str(root.val) + Codec.DELIMITER + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        lst = data.split(",")
        q = queue.Queue()
        for ele in lst:
            if ele:
                q.put(ele)
        return self.deserialize_helper(q)

    def deserialize_helper(self, q):
        ele = q.get()
        if ele == Codec.NULL_SYMBOL:
            return None
        node = TreeNode(int(ele), None, None)
        node.left = self.deserialize_helper(q)
        node.right = self.deserialize_helper(q)
        return node

    def is_same_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 and root2:
            return root1.val == root2.val and self.is_same_tree(root1.left, root2.left) and self.is_same_tree(
                root1.right, root2.right)
        return False


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.codec = Codec()
        self.root = TreeNode(1,
                             TreeNode(2, None, None),
                             TreeNode(3,
                                      TreeNode(4, None, None),
                                      TreeNode(5, None, None)))

    def test_is_same_tree(self):
        self.assertEqual(self.codec.is_same_tree(self.root, self.root), True)

    def test_serialize(self):
        self.assertEqual(self.codec.serialize(self.root), "1,2,null,null,3,4,null,null,5,null,null,")

    def test_deserialize(self):
        self.assertEqual(
            self.codec.is_same_tree(self.codec.deserialize("1,2,null,null,3,4,null,null,5,null,null,"), self.root),
            True)


if __name__ == '__main__':
    unittest.main()
