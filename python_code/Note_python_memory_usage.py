from sys import getsizeof

print(getsizeof(5))

print(getsizeof(5.3))

from decimal import Decimal
print(getsizeof(Decimal(5.3)))

print(getsizeof(""))
print(getsizeof("1"))
print(getsizeof("1234"))

print(getsizeof([]))
print(getsizeof([1]))
print(getsizeof([1,2,3,4,5,6,7]))
print(getsizeof(["a long longlong string"]))

print(getsizeof(()))
print(getsizeof((1,)))
print(getsizeof((1,2,3,4)))
print(getsizeof(('a long longlong string')))

print(getsizeof(set()))
print(getsizeof(set([1])))
print(getsizeof(set([1,2,3,4,5,6,7])))

print(getsizeof({}))
print(getsizeof(dict(a=1)))

