#coding=utf-8
'''
展示在Python中，如何操作数组
'''

#################################################
### 一维数组
squares = [1, 4, 9, 16, 25, 36]
print u"打印原数组："
print squares
'''
Python的编号可以为正负

 +---+---+---+---+---+---+
 | 1 | 4 | 9 | 16| 25| 36|
 +---+---+---+---+---+---+
 0   1   2   3   4   5      从第一个开始编号为0
-6  -5  -4  -3  -2  -1      从最后一个开始，编号为-1

'''
## 找到特定下标的元素
print u"打印下标为4的元素："
print squares[4]    # 从第一个开始数，指向25
print u"打印下标为-2的元素："
print squares[-2]   # 从最后一个开始数，指向25

## 找到特定下标范围的元素
print u"打印下标为2（包含）到4（不包含）之间的所有元素："
print squares[2:4]
print u"打印下标从4开始（包含）到数组最后的所有元素："
print squares[4:]
print u"打印第一个元素到第-2（不含）的元素："
print squares[:-2]

## 设置数组元素的值
print u"下标为2的元素乘以10："
squares[2] *= 10
print squares

