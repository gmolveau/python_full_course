import functools
import operator


l = [1, 2, 3]
r = functools.reduce(operator.add, l)
print(r)
