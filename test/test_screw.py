# coding=utf-8
# import pytest
import sys

sys.path.append('../Schrodinger')
from schrodinger.screw.binary_sort_tree import BinarySortTree
from schrodinger.screw.reverse_linked import Node, reverse_linked, every_two_reverse


class TestScrew(object):
    def test_reverse_linked(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))

        new_head = reverse_linked(head)
        temp_list = list()
        while new_head:
            temp_list.append(new_head.data)
            new_head = new_head.next

        assert temp_list == [7, 6, 5, 4, 3, 2, 1]

    def test_every_two_reverse_list(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))

        new_head = every_two_reverse(head)
        temp_list = list()
        while new_head:
            temp_list.append(new_head.data)
            new_head = new_head.next

        assert temp_list == [2, 1, 4, 3, 6, 5, 7]

    def test_every_two_reverse_list_02(self):
        head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

        new_head = every_two_reverse(head)
        temp_list = list()
        while new_head:
            temp_list.append(new_head.data)
            new_head = new_head.next

        assert temp_list == [2, 1, 4, 3, 6, 5]

    def test_bst(self):
        list1 = [46, 29, 12, 32, 59, 98, 57, 92]
        bin_sort = BinarySortTree()
        for item in list1:
            bin_sort.insert(item)
        item_list = [item.data for item in bin_sort]

        assert item_list == [12, 29, 32, 46, 57, 59, 92, 98]
        assert [item.data for item in bin_sort.pre_travel()] == [46, 29, 12, 32, 59, 57, 98, 92]
        assert [item.data for item in bin_sort.post_travel()] == [12, 32, 29, 57, 92, 98, 59, 46]
        assert [item.data for item in bin_sort.layer_travel()] == [46, 29, 59, 12, 32, 57, 98, 92]
