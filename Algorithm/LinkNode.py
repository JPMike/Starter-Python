import unittest


class LinkNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}->".format(self.data)


class DoublyLinkNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = LinkNode(data)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def search(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                break
            else:
                curr = curr.next
        if not curr:
            raise ValueError("Data not in list")
        return curr

    def delete(self, data):
        # delete first found data
        curr = self.head
        prev = None
        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                else:
                    # delete head
                    self.head = curr.next
                break
            else:
                prev = curr
                curr = curr.next
        if not curr:
            raise ValueError("Data not in list")

    def __str__(self):
        curr = self.head
        str_list = []
        while curr:
            str_list.append(str(curr.data))
            curr = curr.next
        return "->".join(str_list)

    @staticmethod
    def create(node_num):
        head = LinkNode()
        # copy and reserve head
        curr = head
        for num in range(1, node_num + 1):
            curr.next = LinkNode(num)
            curr = curr.next
        return LinkList(head.next)


class LinkListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.link_list = LinkList.create(3)

    def test_create(self):
        self.assertEqual(self.link_list.__str__(), "1->2->3")

    def test_size(self):
        self.assertEqual(self.link_list.size(), 3)

    def test_insert(self):
        self.link_list.insert(4)
        self.assertEqual(self.link_list.__str__(), "4->1->2->3")

    def test_search(self):
        found_node = self.link_list.search(3)
        self.assertEqual(found_node.data, 3)
        with self.assertRaises(ValueError):
            self.link_list.search(4)

    def test_delete(self):
        self.link_list.delete(1)
        self.assertEqual(self.link_list.__str__(), "2->3")


if __name__ == "__main__":
    unittest.main()
