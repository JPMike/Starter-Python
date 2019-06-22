import unittest


def get_appear_twice_num(lst):
    # num in lst will appear twice or once, but only one num will appear once, find it if exists
    result = lst[0]
    for i in range(1, len(lst)):
        # use the fact that num^num=0 0^num=num
        result ^= lst[i]

    for num in lst:
        if num == result:
            return result

    return None


def get_appear_twice_num_plus(lst):
    # num in lst will appear twice or once, but two of the nums will appear once, find all of it if exists
    result = lst[0]
    for i in range(1, len(lst)):
        result ^= lst[i]

    # find one of bit 1 position in result
    mark = 1
    while mark <= result:
        if (result & mark) == mark:
            break
        mark *= 2

    # separate num depend on bit 1 position
    lst1 = list()
    lst2 = list()
    for num in lst:
        if (num & mark) == mark:
            lst1.append(num)
        else:
            lst2.append(num)

    # XOR again
    result1 = lst1[0]
    for i in range(1, len(lst1)):
        result1 ^= lst1[i]

    result2 = lst2[0]
    for i in range(1, len(lst2)):
        result2 ^= lst2[i]

    # sort the result
    if result1 < result2:
        return result1, result2
    else:
        return result2, result1


class Test(unittest.TestCase):
    def test_get_appear_twice_num(self):
        lst1 = [2, 2, 1]
        self.assertEqual(get_appear_twice_num(lst1), 1)
        lst2 = [4, 1, 2, 1, 2]
        self.assertEqual(get_appear_twice_num(lst2), 4)
        lst3 = [2, 2]
        self.assertEqual(get_appear_twice_num(lst3), None)

    def test_get_appear_twice_num_plus(self):
        lst1 = [1, 2, 2, 1, 3, 4]
        self.assertEqual(get_appear_twice_num_plus(lst1), (3, 4))
        lst2 = [2, 1]
        self.assertEqual(get_appear_twice_num_plus(lst2), (1, 2))


if __name__ == '__main__':
    unittest.main()
