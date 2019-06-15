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

    def print(self):
        tmp = self.head
        while tmp:
            print(tmp, end="")
            tmp = tmp.next
        print("")

    @classmethod
    def create(cls, node_num):
        head = LinkNode()
        # copy and reserve head
        curr = head
        for num in range(node_num):
            curr.next = LinkNode(num)
            curr = curr.next
        return LinkList(head.next)


if __name__ == "__main__":
    link_list = LinkList.create(10)
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
