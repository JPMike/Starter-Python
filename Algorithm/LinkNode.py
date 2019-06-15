import random


class LinkNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return "{}->".format(self.get_data())

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


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
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        return count

    def search(self, data):
        curr = self.head
        if not curr:
            raise ValueError("Data not in list")
        found = False
        while curr and not found:
            if curr.get_data() == data:
                found = True
            else:
                curr = curr.get_next()
        return curr

    def delete(self, data):
        curr = self.head
        if not curr:
            raise ValueError("Data not in list")
        prev = None
        while curr:
            if curr.get_data() == data:
                if prev:
                    prev.set_next(curr.get_next())
                else:
                    self.head = curr.get_next()
                break
            else:
                prev = curr
                curr = curr.get_next()

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp, end="")
            tmp = tmp.get_next()
        print("")

    @classmethod
    def create(cls, node_num):
        head = LinkNode()
        tmp = head
        for _ in range(node_num):
            tmp.set_next(LinkNode(random.randint(1, node_num)))
            tmp = tmp.get_next()
        return LinkList(head.get_next())


if __name__ == "__main__":
    link_list = LinkList.create(9)
    print("origin:")
    link_list.print()
    print("size: {}".format(link_list.size()))
    print("insert: 10")
    link_list.insert(10)
    link_list.print()
    print("size: {}".format(link_list.size()))
    print("search: 5")
    print(link_list.search(5))
    print("delete first found: 5")
    link_list.delete(5)
    print("after: ")
    link_list.print()
    print("size: {}".format(link_list.size()))
