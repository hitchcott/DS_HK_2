# coding=utf-8
from numpy import array, dot
from numpy.linalg import inv
from pprint import pprint

X = array([[1,2],[1,2],[1,3],[1,4]]) # 2 x 4 matrix
y = array([[1],[2],[3],[4]])  # 1 x 4 matrix

print 'X\n', X
print 'y\n'

n = inv(dot(X.T, X)) # inverse and multiple same matrix
print 'inv(dot(X.T, X))\n', n

k = dot(X.T, y) # multiply matrix
print 'dot(X.T, y)\n', k


coef_ = dot(n,k)
print 'coef_ = dot(n,k)\n', coef_

