
class BSTNode(object):
    # 二叉树的节点
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySortTree(object):
    # 基于二叉树节点的二叉排序树
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def clear(self):
        # 清除该树
        self._root = None

    def get_root(self):
        return self._root

    def insert(self, value):
        if self.is_empty():
            self._root = BSTNode(value)
            return
        rt = self._root
        while True:
            if value > rt.data:
                if rt.right is None:    
                    rt.right = BSTNode(value)
                    return
                rt = rt.right
            elif value < rt.data:
                if rt.left is None:
                    rt.left = BSTNode(value)
                    return
                rt = rt.left
            else:
                print('data existed !')
                return

    def search(self, value):
        # 查找，返回查询节点或者None
        rt = self._root
        while True:
            if rt.data == value:
                return rt
            elif rt.data > value:
                rt = rt.left
            else:
                rt = rt.right
            if rt is None:
                return None

    def __iter__(self, rt=None):
        # 遍历的非递归实现
        # 遍历中使用列表作为栈，来保存先后走过的路径
        if rt is None:
            rt = self._root
        stack = list()
        # 中序遍历
        # 将rt入栈，若rt的左孩子不为空，将其入栈，并将rt的左孩子设为当前rt
        #          若左孩子为空，取出栈顶元素，访问，然后将栈顶元素的右孩子设为当前节点
        while stack or rt:
            while rt:
                stack.append(rt)
                rt = rt.left
            rt = stack.pop()
            yield rt
            # 存在节点没有左孩子但是有右孩子的情况
            rt = rt.right

    def pre_travel(self, rt=None):
        # 前序遍历
        # 访问rt，并将rt入栈
        # 判断rt的左子树或者rt是否为空，若为空取栈顶元素，并将栈顶元素的右孩子设为rt
        #                            若不为空，将rt的左孩子设为rt
        # 直到 stack为空或者rt为空，结束遍历
        if rt is None:
            rt = self._root
        stack = list()
        while stack or rt:
            if rt is not None:
                yield rt
                stack.append(rt)
            if rt is None or rt.left is None:
                rt = stack.pop()
                rt = rt.right
            else:
                rt = rt.left

    def post_travel(self, rt=None):
        # 后序遍历
        # 将根节点入栈，设置pre为前一次访问的节点
        # 只有当栈顶元素没有左右孩子或者他的左右孩子已经被访问的情况下才能访问该节点
        # 否则依次将改节点的右孩子、左孩子入栈
        if rt is None:
            rt = self._root
        stack = list()
        stack.append(rt)
        pre = None
        while stack:
            rt = stack[-1]
            if (rt.left is None and rt.right is None) or (pre is not None and (pre is rt.left or pre is rt.right)):
                yield rt
                pre = stack.pop()
            else:
                if rt.right:
                    stack.append(rt.right)
                if rt.left:
                    stack.append(rt.left)

    def layer_travel(self, rt=None):
        # 层级遍历
        # 使用队列，先进先出
        # 将根节点推入队列，访问根节点，分别判断根节点的左右节点，并将其推入队列
        # 每次从队列中取出一个元素并访问，并判断其左右子节点是否为空，将子节点推入队列
        # 循环的退出条件为队列为空
        # from my_queue import Queue
        from queue import Queue
        if rt is None:
            rt = self._root
        qu = Queue()
        qu.put(rt)
        while qu.qsize() != 0:
            node = qu.get()
            yield node
            if node.left:
                qu.put(node.left)
            if node.right:
                qu.put(node.right)

    def delete(self, value):
        # todo 待优化
        # 如果存在则返回目标节点，否则返回None
        rt = self._root
        data_list = [i.data for i in self.__iter__()]
        if value not in data_list:
            # 不存在目标节点，返回None
            print('do not exist !')
            return None

        # 处理只有一个节点时的情况
        if len(data_list) == 1:
            if value == data_list[0]:
                self._root = None
                return rt

        # 如果目标节点是树的子节点，那么获取节点的元素列表，删除该元素，用剩下的元素新建二叉排序树，然后返回新的树
        data_list.remove(value)
        self.clear()
        new_tree = BinarySortTree()
        # node_list = list(map(new_tree.insert, data_list))
        for _item in data_list:
            new_tree.insert(_item)
        self._root = new_tree._root
        return value

    # 递归实现遍历
    def pre_order(self, node):
        if node is None:
            return
        pre_order_list.append(node.data)
        # print(node.data)
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)
    
    def in_order(self, node):
        if node is None:
            return
        if node.left:
            self.in_order(node.left)
        in_order_list.append(node.data)
        # print(node.data)
        # yield node.data
        if node.right:
            self.in_order(node.right)
    
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        post_order_list.append(node.data)
        # print(node.data)
        # yield node.data

    
if __name__ == '__main__':
    list1 = [46, 29, 12, 32, 59, 98, 57, 92]
    bin_sort = BinarySortTree()
    for item in list1:
        bin_sort.insert(item)
    # node_map = list((map(bin_sort.insert, list1)))
    item_list = [item.data for item in bin_sort]
    print('非递归中序遍历： {}'.format(item_list))
    print('非递归前序遍历： {}'.format([item.data for item in bin_sort.pre_travel()]))
    print('非递归后序遍历： {}'.format([item.data for item in bin_sort.post_travel()]))
    print('非递归层级遍历： {}'.format([item.data for item in bin_sort.layer_travel()]))

    # 递归遍历操作
    pre_order_list = list()
    bin_sort.pre_order(bin_sort.get_root())
    print('递归前序遍历: {}'.format(pre_order_list))
    in_order_list = list()
    bin_sort.in_order(bin_sort.get_root())
    print('递归中序遍历: {}'.format(in_order_list))
    post_order_list = list()
    bin_sort.post_order(bin_sort.get_root())
    print('递归后序遍历: {}'.format(post_order_list))

    delete_value = bin_sort.delete(92)
    print('删除元素: {}'.format(delete_value))

    item_list1 = [item.data for item in bin_sort]
    print('删除元素：{}'.format(item_list1))
