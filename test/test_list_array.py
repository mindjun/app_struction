# coding=utf-8
import pytest
import sys
sys.path.append('../Schrodinger')
from schrodinger.list_and_array import *


class TestDemoListCommon(object):
    def test_find_median_sorted_arrays_01(self):
        nums1 = [1, 2]
        nums2 = [3, 4]

        assert find_median_sorted_arrays(nums1, nums2) == 2.5

    def test_find_median_sorted_arrays_02(self):
        nums1 = 'adssa'
        nums2 = {'a': 1}

        with pytest.raises(TypeError):
            find_median_sorted_arrays(nums1, nums2)
