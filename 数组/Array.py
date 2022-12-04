"""
Array
"""


class Array:
    # 初始化,默认填0
    def __init__(self, number):
        self.arr = [0] * number

    # 求数组的长度
    def size(self):
        return len(self.arr)

    # 下标查询
    def __getitem__(self, item):
        return self.arr[item]

    # 改
    def __setitem__(self, key, value):
        self.arr[key] = value

    def __str__(self):
        return str(self.arr)

    # 等等方法
    # 值得一提的是，Python的list是线性顺序存储结构，存储的是对各种数据对象的引用（指针）
    # 所以，如果存储的是相同数据类型，从某种意义上可以认为list就是一种数组。实质是指针数组：void*


if __name__ == '__main__':
    my_array = Array(5)
    for i in range(5):
        my_array[i] = i
    print(my_array)
    print(my_array.size())
