# coding=utf-8
from numpy import *

arrayOne = arange(15).reshape(3,5)

matrixOne = matrix('1 2 3; 4 5 6; 7 8 9');

a1 = array([ [1, 2], [3, 4] ])
a2 = array([ [1, 3], [2, 4] ])
m1 = matrix('1 2; 3 4')
m2 = matrix('1 3; 2 4')

print 'array multiply\n', a1 * a2
print 'matrix multiply\n', m1 * m2

print 'dot arr multiply\n', dot(a1, a2)
print 'dot arr multiply\n', dot(m1, m2)

print 'transpose a1\n', a1.T
print 'inverse m1\n', m1.T

print 'iMatrix 5\n', eye(5)
