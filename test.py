# def tt(a = [], b = 1):
#     a.append(1)
#     b += 1
#     print(a, id(a), b ,id(b))
#
#
#
#
# tt()
#
#
# class Fab(object):
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             r = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
#
# for n in Fab(5):
#     print(n)
#
#
# def bar():
#     result = 0
#     for i in range(1000000):
#         result += i
#     return result
#
#
# def foo():
#     result = 0
#     for i in range(100000):
#         result += i
#     for i in range(5):
#         bar()
#     return result
#
#
# def main():
#     import cProfile
#
#     # 直接把分析结果打印到控制台
#     cProfile.run("foo()")
#
#     # 根据cumtime列排序后打印到控制台，
#     # 也就是说按包含子函数执行的时间顺序进行排序
#     cProfile.run("foo()", sort="cumulative")
#
# def insert_sort(lists):
#     # 插入排序
#     count = len(lists)
#     for i in range(1, count):
#         key = lists[i]
#         j = i - 1
#         while j >= 0:
#             if lists[j] > key:
#                 lists[j + 1] = lists[j]
#                 lists[j] = key
#             j -= 1
#     return lists
#
#
#
# if __name__ == '__main__':
#     # 测试
#     list = [10, 23, 1, 53, 654, 54, 16, 646, 65, 3155, 546, 31]
#     print(list)
#     insert_sort(list)
#     print(list)
#


import time
print(time.time())
# 格式化时间戳为标准格式
localtime = time.asctime( time.localtime(time.time()) )
print()
print(localtime)