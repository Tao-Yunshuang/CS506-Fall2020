from math import sqrt
import random

def euclidean_dist(x, y):
    if len(x) == 0 or (len(y) == 0):
        return 'lengths must not be zero'
    if len(x) != len(y):
        return 'lengths must be equal'
    d = 0
    for i in range(len(x)):
        d = d + (x[i] - y[i]) ** 2
    return sqrt(d)

def manhattan_dist(x, y):
    if len(x) == 0 or (len(y) == 0):
        return 'lengths must not be zero'
    if len(x) != len(y):
        return 'lengths must be equal'
    d = 0
    for i in range(len(x)):
        d = d + abs(x[i] - y[i])
    return d

def jaccard_dist(x, y):
    if len(x) == 0 or (len(y) == 0):
        return 'lengths must not be zero'
    xx = set(x)
    yy = set(y)
    return 1 - len(xx.intersection(yy)) / len(xx.union(yy))

def cosine_sim(x, y):
    if len(x) == 0 or (len(y) == 0):
        return 'lengths must not be zero'
    if len(x) != len(y):
        return 'lengths must be equal'
    x_len = 0
    y_len = 0
    mul = 0
    for i in range(len(x)):
        x_len = x_len + x[i] ** 2
        y_len = y_len + y[i] ** 2
        mul = mul + x[i] * y[i]
    if x_len == 0 or y_len == 0:
        return 0
    return mul / sqrt(x_len * y_len)

# Feel free to add more
