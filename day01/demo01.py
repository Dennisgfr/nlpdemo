import numpy as np
import numpy.matlib

#
# data = np.random.rand(10, 2)
#
# x = data[:, 0]
# y = data[:, 1]
#
# plt.plot(x, y, 'go', markersize=10)
# plt.show()
# 数组点积 1*11+2*12 ,1*13+2*14, 3*11+4*12, 3*13+4*14
# a = np.array([[1, 2], [3, 4]])
# print(a)
# b = np.array([[11, 12], [13, 14]])
# print(b)
# print(np.dot(a, b))

# 填充2*2 的矩阵
print(np.matlib.empty((2, 2)))
# 以0填充
print(np.matlib.zeros((2, 2)))
# 以1填充
print(np.matlib.ones((2, 2)))
# numpy.matlib.eye() 函数返回一个矩阵，对角线元素为 1，其他位置为零。
# n: 返回矩阵的行数
# M: 返回矩阵的列数，默认为 n
# k: 对角线的索引
# dtype: 数据类型
print(numpy.matlib.eye(n=3, M=4, k=0, dtype=float))
# numpy.matlib.identity() 函数返回给定大小的单位矩阵

print(np.matlib.identity(5, dtype=float))
