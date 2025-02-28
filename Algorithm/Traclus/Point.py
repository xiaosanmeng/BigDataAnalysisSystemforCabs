# -*- coding: utf-8 -*-
"""
@File            : Point.py
@Time            : 16.29 2021/8/13
@Author          : Horace, JoTer
"""

import math
import numpy as np


class Point(object):
    """对轨迹中的点进行封装, 可以进行比较, 一些常用的计算, 如距离计算, dot计算等, 本point主要对2维的point进行封装
    method
    ------
        str: 返回point的字符串格式
        +: 加号操作符, 实现两个point类型的相加操作
        -: 减号操作符, 实现两个point类型的减法运算
        distance(other): 实现两个Point类型的距离(欧式距离)计算
        dot(other): 实现两个Point对象的dot运算, 得到两个点的值: x**2 + y**2
    """

    def __init__(self, x, y, traj_id=None):
        self.trajectory_id = traj_id
        self.x = x
        self.y = y

    def __repr__(self):
        return "{0:.8f},{1:.8f}".format(self.x, self.y)

    def get_point(self):
        return self.x, self.y

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("The other type is not 'Point' type.")
        _add_x = self.x + other.x
        _add_y = self.y + other.y
        return Point(_add_x, _add_y, traj_id=self.trajectory_id)

    def __sub__(self, other):
        if not isinstance(other, Point):
            raise TypeError("The other type is not 'Point' type.")
        _sub_x = self.x - other.x
        _sub_y = self.y - other.y
        return Point(_sub_x, _sub_y, traj_id=self.trajectory_id)

    def __mul__(self, x):
        if isinstance(x, float):
            return Point(self.x * x, self.y * x, traj_id=self.trajectory_id)
        else:
            raise TypeError("The other object must 'float' type.")

    def __truediv__(self, x):
        if isinstance(x, float):
            return Point(self.x / x, self.y / x, traj_id=self.trajectory_id)
        else:
            raise TypeError("The other object must 'float' type.")

    def distance(self, other):
        """计算两个point之间的距离"""
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def as_array(self):
        return np.array((self.x, self.y))


def _point2line_distance(point, start, end):
    """
    通过向量的方式计算point到line的垂直距离
    :param point:
    :param start: 同point的格式一致, 都为numpy的array格式
    :param end: 同point的格式一致, 都为numpy的array格式
    :return: point点到start、 end两点连线的垂直距离（欧式距离）
    """
    if np.all(np.equal(start, end)):
        return np.linalg.norm(point - start)
    return np.divide(np.abs(np.linalg.norm(np.cross(end - start, start - point))),
                     np.linalg.norm(end - start))
