# coding=utf-8


def find_median_sorted_arrays(nums1, nums2):
    """
    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2

    :param:
        * nums1: List[int]
        * nums2: List[int]

    :return:
        * median: (float) 数组的中位数

    代码示例::

    >>> nums1 = [1, 2]
    >>> nums2 = [2]
    >>> median = find_median_sorted_arrays(nums1, nums2)
    >>> median
    >>> 2.0

    """
    if not isinstance(nums1, list):
        raise TypeError('nums1 must be a list, but we got an {0}'.format(type(nums1)))
    elif not isinstance(nums2, list):
        raise TypeError('nums2 must be a list, but we got an {0}'.format(type(nums2)))

    # 先合并为一个列表，再求中位数
    len1 = len(nums1)
    len2 = len(nums2)
    len3 = len1 + len2

    nums3 = list()
    # index1, index2, index3 = 0, 0, 0
    #         while index1<len1 and index2<len2:
    #             if nums1[index1] < nums2[index2]:
    #                 nums3.append(nums1[index1])
    #                 index1 += 1
    #             else:
    #                 nums3.append(nums2[index2])
    #                 index2 += 1
    #             index3 += 1

    #         if index1<len1:
    #             nums3.extend(nums1[index1:])
    #         if index2<len2:
    #             nums3.extend(nums2[index2:])

    # 也可以使用如下方法合并两个有序数组
    while nums1 and nums2:
        if nums1[0] < nums2[0]:
            nums3.append(nums1.pop(0))
        else:
            nums3.append(nums2.pop(0))

    if nums1:
        nums3.extend(nums1)
    if nums2:
        nums3.extend(nums2)

    mid1 = int(len3 / 2)
    mid2 = int((len3 - 1) / 2)

    if len3 % 2 == 0:
        return float((nums3[mid1] + nums3[mid2]) / 2)
    else:
        return nums3[mid2]
