"""
列表的翻转
"""


class Node(object):
    def __init__(self, val, ne=None):
        self.data = val
        self.next = ne


def reverse_linked(head):
    """
    1 ==> 2 ==> 3 ==> 4 ==>5    5 ==>4 ==>3 ==>2 ==>1
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return
    he, cur, pre = head, head, None
    while cur:
        he = cur
        tmp = cur.next
        cur.next = pre
        cur, pre = tmp, cur
    return he


def every_two_reverse(head):
    """
    1 ==> 2 ==> 3 ==> 4 ==>5
    head  next  tmp
    2 ==> 1 ==> 4 ==> 5
          3 ==> 4
          3 is new_head
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return
    new_head = head.next
    while head is not None and head.next is not None:
        next = head.next
        tmp = next.next
        if tmp is None:
            # 节点数为偶数的情况
            next.next = head
            head.next = None
            break
        else:
            # 节点数为奇数的情况
            if tmp.next is None:
                head.next = tmp
            else:
                head.next = tmp.next
            next.next = head
            head = tmp
    return new_head


if __name__ == '__main__':
    h = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))

    every_two_reverse_list = list()
    new_h = every_two_reverse(h)
    while new_h:
        every_two_reverse_list.append(new_h.data)
        new_h = new_h.next

    h = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

    every_two_reverse_list = list()
    new_h = every_two_reverse(h)
    while new_h:
        every_two_reverse_list.append(new_h.data)
        new_h = new_h.next

    assert every_two_reverse_list == [2, 1, 4, 3, 6, 5]

    h = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    reverse_list = list()
    new_h_1 = reverse_linked(h)
    while new_h_1:
        reverse_list.append(new_h_1.data)
        new_h_1 = new_h_1.next

    assert reverse_list == [7, 6, 5, 4, 3, 2, 1]
