import sys


def dict_size_test():
    ob = {'x': 1, 'y': 2, 'z': 3}
    print(sys.getsizeof(ob))


def class_instance_size_test():
    class Point(object):
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    point = Point(1, 2, 3)
    print(point.__dir__())
    print(point.__dict__)
    print(sys.getsizeof(point), sys.getsizeof(point.__dict__))


def class_instance_with_slot_size_test():
    class Point(object):
        __slots__ = 'x', 'y', 'z'

        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

    point = Point(1, 2, 3)
    print(point.__dir__())
    print(sys.getsizeof(point))


if __name__ == '__main__':
    dict_size_test()
    class_instance_size_test()
    class_instance_with_slot_size_test()
    pass
